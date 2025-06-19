import yt_dlp
import tkinter as tk
from tkinter import filedialog

# Function to download a YouTube video using yt-dlp
def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save the video using its title as filename
            'format': 'best[ext=mp4]/best',  # Prefer best quality in MP4 format
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
        print("✅ Video downloaded successfully")
    except Exception as e:
        print(f"❌ Error: {e}")

# Function to open folder selection dialog
def open_file_dialog(): 
    folder = filedialog.askdirectory()  # Let user choose directory
    if folder: 
        print(f"Selected folder: {folder}")
    return folder

# Main execution starts here
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    video_url = input("Enter the YouTube video URL: ")
    save_path = open_file_dialog()  # Ask user to pick a download location

    if not save_path:
        print('❌ Invalid folder location. Download cancelled.')
    else: 
        download_video(video_url, save_path)
