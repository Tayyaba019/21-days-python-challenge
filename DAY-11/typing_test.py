import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target, curses.color_pair(3))  # Display target text
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
def load_text(): 
    with open("text.txt",'r') as f: 
        lines = f.readlines()
        return random.choice(lines).strip()
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []

    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # Non-blocking input

    while True:
        time_elapsed = max(time.time() - start_time, 1e-6)  # Avoid division by zero
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if key in ('\x1b',):  # ESC key to exit
            break
        elif key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Correct char
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Incorrect char
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Default text

    start_screen(stdscr)
    wpm_test(stdscr)

    stdscr.addstr(3, 0, "You completed the text. Press any key to continue...")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
