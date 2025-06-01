# ⌨️ Day 11 - Speed Typing Test

This project is a **Speed Typing Test** built using Python's `curses` module.  
The program measures how fast you can type a given sentence and displays your **Words Per Minute (WPM)** in real-time.

---

## 🚀 Features

- Terminal-based UI using the `curses` library
- Real-time WPM (Words Per Minute) calculation
- Color-coded character display:
  - ✅ Green: Correctly typed character
  - ❌ Red: Incorrectly typed character
- Backspace support
- Auto-completion when text matches the target
- Escape key to exit at any time

---

## 🛠️ How It Works

- The user is shown a target sentence.
- As they type, each character is checked against the target text.
- WPM is updated in real time based on how many characters are typed.
- The game ends when the entire sentence is typed correctly.

---

## 📦 Requirements

- Python 3
- A terminal or command prompt that supports the `curses` module  
  *(Note: `curses` works natively on Unix/Linux/macOS. On Windows, you may need to install `windows-curses`:)*

```bash
pip install windows-curses
