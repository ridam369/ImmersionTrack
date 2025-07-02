# ImmersionTrack

**ImmersionTrack** is a minimalist terminal-based tool that helps you **track**, **log**, and **visualize** your daily immersion or study time. It’s perfect for language learners, self-learners, or anyone who wants to stay consistent and see their learning journey over time — right from the command line.

---

## 📌 Features

- 📊 **Anki-style 30-day bar chart** to visualize recent immersion.
- 📅 **GitHub-style yearly ASCII heatmap** to track your consistency.
- ✅ Add and delete entries easily.
- 🔁 Daily progress bar with a configurable time goal.
- 🗃️ Auto-backups for your data.
- 🧠 Designed for terminal lovers and productivity nerds.

---

## 📂 File Format

The data is stored in a simple CSV file called `immersion.csv`.

### CSV Structure:

Date,Video,Time
2025-06-01,Shingeki no Kyojin Episode 1,00:45
2025-06-02,Nihongo no Mori - N4 Grammar,00:30

- `Date` – In `YYYY-MM-DD` format.
- `Video` – Title or source of your immersion.
- `Time` – Time spent, in `HH:MM` format.

---

## 🚀 How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/ridam369/ImmersionTrack.git
cd ImmersionTrack

2. Install Dependencies

Only required dependency:

pip install pandas plotext

    plotext is used to draw terminal-based charts.

3. Run the Tracker

python3 immersiontrack.py

4. Menu Options

=== Immersion Tracker ===
1. View Chart        → View 30-day bar chart
2. Add Entry         → Add a new immersion session
3. Delete Entry      → Delete today's entry
4. Stats             → Weekly and monthly summaries
5. Exit              → Quit the tracker

📈 Visualizations

📅 Yearly Immersion Heatmap

Sun   █ ░ █ █ █ █ █ █ ░ ░ ▓ ▓ █ █ ▓ ▒ █ ░ ▓ ▓ █ ▓ ▒ ▒ █ ▓ ░ █ ░ █ ░ █ ░ ░ ░ █ ░ ▓ ▒ █ ▒ █ █ ▓ ▓ █ ▓ █ ▓ ░ ▓
Mon █ ▓ ░ ░ ░ ▓ ░ █ █ █   █ ▓ ░ ▒ █ ▓ █ ▒ █ █ ▒ █ █ ░   ░ █ ░ █ █ █ █ █ ▒ █ █ ▓ ░ ▓ █ ░   ▒ ░ ▓ ▒ ▒ █   █ ▓
Tue █ ▓ ▓ █ █ █ █ ░ ▒ █ ▓ █ ░ ░ █ █ ░   █ ▓ ▓ ░ ▓ ▓ █ █ ▒ ░ █ █ ▒ ▓ █ ▒ ▒ █ ▓ ▓ █ ▓   ░ ▓ ▒ █   ▓ █ █ █ █ █
Wed ▓ █ █ █ ▓ █ ▓ ▓ ▒ ▓ ░ ▓ █ █ ▓ █ ▓ █ █ ▒ ▒ ░ █ ░ ▓ █   █ █ █ ░ █ █ ░ █ █ ▒ █ ░ ▒ ░ █ ░ █ ▓ █ █ ░ █ ▓ █ █
Thu ▓ ░ ▓ █ █ ▓ █ █ ▒ █ █ █ █ █ ░ ▒ █   █ ▓ ▓ █ █ ▓ ▓ █ ▓ █ █ ░ █ █ █ █ █ ▓ ░ █ ▓ ▓ ▓ █ ▒     █ ░ ▓ ▒ █ ░ ▒
Fri █ █ █ █ ▒ █ ▓ ▓   ▒ ░ ▓ ▓ █ ▓ █ █ ▒ █ █ ▓ █ ░ ▒ ░ ▒ ▒ █ █ █ █ ░ █ █ █ █ ▓ █ █ ░ ▒ ▓ █ █ █ █ ░ █ ▓ ▓ ▓ ▓
Sat █ █ █ █ █ ▓ █ █ ▒ ▓ █ ▓ ▒ █ █ █ ▒ ▓ ▓ ▓ █ █ █   █ █ ▓ ▓ █ █ ░ █ █ ░ ▓ ▒ ▓ ▓ ▒ █ ▓ ▓   █ █ █ ░ ▒ █ ▒ █ ░

📊 30-Day Immersion History (Anki-style)

                                                                                                                     █  
                                     █                                                                               █  
                                     █                           █   █                                               █  
     █                               █                           █   █                                               █  
     █                               █                           █   █           █           █   █                   █  
     █                               █                           █   █           █           █   █                   █  
 █   █   █   █                       █       █               █   █   █           █           █   █                   █  
 █   █   █   █           █           █   █   █               █   █   █       █   █   █   █   █   █               █   █  
 █   █   █   █       █   █           █   █   █   █           █   █   █       █   █   █   █   █   █       █       █   █  
 █   █   █   █   █   █   █   █       █   █   █   █   █       █   █   █       █   █   █   █   █   █   █   █       █   █  
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 
 70 125  75  75  20  45  60  30  0  150  50  80  45  20  10  80 135 135  5   50 105  55  50 110 110  20  45  10  60 165


📊 Immersion Summary:
🗓️  Weekly Total: 280 mins over 4 day(s) (avg: 70.0 mins/day)
📅 Monthly Total: 0 mins over 0 day(s) (avg: 0.0 mins/day)
🏆 Best Day: 2024-07-21 — 175 mins

💾 Backups

    Automatically saves backups of your CSV in a /backups folder.

    Backup filenames follow this format: immersion_YYYYMMDD.csv.

🛠 Customization

You can change the following easily in the code:

    🔁 goal for daily progress (default: 60 minutes)

    📦 CSV_FILE name if you want a custom data file

    🎨 Characters for block styles in the heatmap

📘 License

This project is released under the MIT License.
Feel free to fork, modify, and use it in your own projects.

✨ Credits

Built by Ridam — inspired by Anki and GitHub's visual tracking systems.

    Jul      Aug        Sep      Oct      Nov        Dec      Jan      Feb      Mar        Apr      May        Jun
