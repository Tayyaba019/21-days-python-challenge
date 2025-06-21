import os
import shutil
from datetime import datetime
import schedule
import time

# Define source and destination directories
source_dir = 'C:/Users/Tayyaba/Pictures/screenshots'
destination_dir = 'C:/Users/Tayyaba/Desktop/Backups'

# Function to copy the entire folder to a destination with today's date
def copy_folder_to_directory(source, dest):
    today = datetime.today().strftime("%Y-%m-%d")
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)  # Copy source folder to dated destination
        print(f"✅ Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"⚠️ Folder already exists in {dest}")

# Schedule the backup every day at 6:55 PM
schedule.every().day.at("18:55").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# Continuously check and run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
