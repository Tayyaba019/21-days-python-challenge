# 🗃️ Automatic Daily Folder Backup Script

This Python script automatically backs up a folder (`screenshots`) to your desktop at a scheduled time every day. It uses the current date to create a new backup folder.

---

## ✅ Features

- 🕒 Automatically runs every day at 6:55 PM
- 📂 Copies entire contents of the source folder
- 🗓️ Creates a dated backup folder in the destination
- ⚠️ Skips backup if the folder for that date already exists

---

## 🛠️ Requirements

Install required libraries using:

```bash
pip install schedule
