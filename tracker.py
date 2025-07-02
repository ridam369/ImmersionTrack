import pandas as pd
import plotext as plt
from datetime import datetime, timedelta
import os
import shutil
import calendar




CSV_FILE = 'immersion.csv'

# Ensure file exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w') as f:
        f.write('Date,Video,Time\n')

def load_data():
    df = pd.read_csv(CSV_FILE, quotechar='"')
    df.columns = df.columns.str.strip()  # ✅ Removes whitespace from column names
    return df

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

def parse_time(time_str):
    """Convert HH:MM to timedelta"""
    return timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]))

def total_time_per_day(df):
    df['TimeDelta'] = df['Time'].apply(parse_time)
    summary = df.groupby('Date')['TimeDelta'].sum().reset_index()
    summary['TotalMinutes'] = summary['TimeDelta'].dt.total_seconds() / 60
    return summary

def visualize(df):
    summary = total_time_per_day(df)

    if summary.empty:
        print("⚠️ No data to visualize.")
        return

    # Limit to recent 30 days
    summary = summary.tail(30)

    dates = summary['Date'].tolist()
    minutes = summary['TotalMinutes'].tolist()

    max_height = 10  # max blocks in terminal bar height
    max_value = max(minutes)
    if max_value == 0:
        max_value = 1  # avoid division by zero

    # Scale minutes to max_height blocks
    heights = [int((m / max_value) * max_height) for m in minutes]

    # Determine fixed width per column
    # Width is max of 3 or length of largest minute number + 1 space padding
    max_min_len = max(len(str(int(m))) for m in minutes)
    col_width = max(3, max_min_len + 1)

    # Print bars vertically
    print("\n📊 30-Day Immersion History (Anki-style)\n")
    for level in range(max_height, 0, -1):
        for h in heights:
            block = "█" if h >= level else " "
            print(block.center(col_width), end='')
        print()

    # Print baseline
    print("―" * (col_width * len(heights)))

    # Print dates (day of month)
    for d in dates:
        day_str = str(d)[-2:]  # last two chars of date string YYYY-MM-DD
        print(day_str.center(col_width), end='')
    print()

    # Print immersion minutes under dates
    for m in minutes:
        print(str(int(m)).center(col_width), end='')
    print("\n")



def append_entry():
    date = input("Enter date (YYYY-MM-DD): (default = today)").strip()
    video = input("Enter video title: ").strip()
    
    try:
        # Try parsing input with expected format
        time = input("Enter time watched (HH:MM): ").strip()
        datetime.strptime(time, "%H:%M")
    except ValueError:
        print("❌ Invalid time format. Please enter time as HH:MM (e.g., 10:30).")
        return
    # Default to today if date is blank
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_input, '%Y-%m-%d')
            date = date_input
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return

    df = load_data()
    new_row = pd.DataFrame([[date, video, time]], columns=['Date', 'Video', 'Time'])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)
    print("✅ Entry added.")
    show_progress()


def delete_entry():
    df = load_data()
    today_str = datetime.today().strftime('%Y-%m-%d')
    
    # Filter rows from today
    df_today = df[df['Date'] == today_str].reset_index()

    if df_today.empty:
        print("⚠️ No entries to delete for today.")
        return
    
    print("Entries you can delete (only today's):")
    print(df_today[['index', 'Date', 'Video', 'Time']])
    try:
        choice = int(input("Enter the number of the row to delete (0-based): "))
    except Exception as e:
        print("❌ Invalid number.")
        return
    if choice < 0 or choice >= len(df_today):
        print("❌ Invalid number.")
        return

    # Get original index from df_today's 'index' column
    actual_index = df_today.loc[choice, 'index']
    
    df = df.drop(index=actual_index)
    save_data(df)
    print("✅ Entry deleted.")
    show_progress()

def menu():
    global goal
    backup_csv()
    show_yearly_ascii_heatmap()
    while True:
        print("\n=== Immersion Tracker ===")
        print("1. View Chart")
        print("2. Add Entry")
        print("3. Delete Entry")
        print("4. Stats")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            df = load_data()
            if df.empty:
                print("No data available.")
            else:
                visualize(df)
        elif choice == '2':
            append_entry()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            show_summary()
            show_yearly_ascii_heatmap()
        elif choice =='5':
            break
        else:
            print("Invalid option.")
def backup_csv():
    os.makedirs("backups", exist_ok=True)
    today = datetime.now().strftime("%Y%m%d")
    backup_file = f"backups/immersion_{today}.csv"

    if not os.path.exists(backup_file):
        shutil.copyfile("immersion.csv", backup_file)
        print(f"✅ Backup created: {backup_file}")

def show_progress():
    df = load_data()
    summary = total_time_per_day(df)
    today_str = datetime.today().strftime('%Y-%m-%d')
    today_total = summary[summary["Date"] == today_str]["TotalMinutes"].sum() if not summary.empty else 0
    percent = int((today_total / goal) * 100)
    bar = "█" * (percent // 10) + "-" * (10 - (percent // 10))
    print(f"🎯 Progress: [{bar}] {percent}%")
    
def show_summary():
    df = load_data()
    if df.empty:
        print("No data to summarize.")
        return

    df['Date'] = pd.to_datetime(df['Date'])
    df['TimeDelta'] = df['Time'].apply(parse_time)

    today = datetime.today()
    one_week_ago = today - timedelta(days=7)
    start_of_month = today.replace(day=1)

    # Filter for weekly and monthly data
    last_week = df[df['Date'] >= one_week_ago]
    this_month = df[df['Date'] >= start_of_month]

    # Weekly summary
    weekly_total = last_week['TimeDelta'].sum()
    weekly_minutes = weekly_total.total_seconds() / 60
    weekly_days = last_week['Date'].nunique()
    weekly_avg = weekly_minutes / weekly_days if weekly_days else 0

    # Monthly summary
    monthly_total = this_month['TimeDelta'].sum()
    monthly_minutes = monthly_total.total_seconds() / 60
    monthly_days = this_month['Date'].nunique()
    monthly_avg = monthly_minutes / monthly_days if monthly_days else 0

    # Best day overall
    daily_totals = df.groupby(df['Date'].dt.date)['TimeDelta'].sum()
    best_day = daily_totals.idxmax()
    best_day_minutes = daily_totals.max().total_seconds() / 60

    print("\n📊 Summary:\n")
    print(f"🗓️  Weekly Total: {weekly_minutes:.0f} mins over {weekly_days} day(s) (avg: {weekly_avg:.1f} mins/day)")
    print(f"📅 Monthly Total: {monthly_minutes:.0f} mins over {monthly_days} day(s) (avg: {monthly_avg:.1f} mins/day)")
    print(f"🏆 Best Day: {best_day} — {best_day_minutes:.0f} mins")

def show_yearly_ascii_heatmap():
    df = load_data()
    if df.empty:
        print("No immersion data found.")
        return

    df['Date'] = pd.to_datetime(df['Date'])
    df['Minutes'] = df['Time'].apply(lambda t: parse_time(t).total_seconds() / 60)

    # Aggregate total minutes per date
    totals = df.groupby(df['Date'].dt.date)['Minutes'].sum()

    today = datetime.today().date()
    start_date = today - timedelta(days=364)  # ~52 weeks

    # Align start_date to previous Sunday (GitHub style)
    start_date -= timedelta(days=(start_date.weekday() + 1) % 7)

    # Build all dates for 52 weeks
    all_dates = [start_date + timedelta(days=i) for i in range(52 * 7)]
    heatmap_data = {date: totals.get(date, 0) for date in all_dates}

    def block(minutes):
        global goal
        if minutes == 0:
            return ' '
        elif minutes < goal/4:
            return '░'
        elif minutes < goal/2:
            return '▒'
        elif minutes < goal:
            return '▓'
        else:
            return '█'

    # Build rows for each day of the week (Sun to Sat)
    rows = [[] for _ in range(7)]
    for day_of_week in range(7):
        for week in range(52):
            date = start_date + timedelta(days=week * 7 + day_of_week)
            val = heatmap_data.get(date, 0)
            cell = block(val)
            if date == today:
                cell = f"*{cell}*"
            rows[day_of_week].append(cell)

    days_header = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    print("\n📅 Yearly Heatmap\n")

    # Print heatmap grid with weekday labels
    for i, day in enumerate(days_header):
        print(f"{day:>3} ", end='')
        print(' '.join(rows[i]))

    # --- Print corrected month labels ---
    # Detect first day of each month in all_dates
    month_positions = {}
    for i, date in enumerate(all_dates):
        if date.day == 1:
            week_index = (date - start_date).days // 7
            if week_index not in month_positions:
                month_positions[week_index] = calendar.month_abbr[date.month]

    # Print month names spaced under the right weeks
    print("\n    ", end='')  # padding for weekday labels
    last_week = 0
    for week in sorted(month_positions.keys()):
        spaces = (week - last_week) * 2  # 2 spaces per week
        print(' ' * spaces + month_positions[week], end='')
        last_week = week + len(month_positions[week]) // 2
    print("\n")



if __name__ == "__main__":
    goal = 60 # set your daily goal in minutes
    menu()
