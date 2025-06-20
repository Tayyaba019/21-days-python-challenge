import os 
import shutil
from datetime import datetime
import schedule
import time

source_dir = 'C:/Users/Tayyaba/Pictures/screenshots'
destination_dir = 'C:/Users/Tayyaba/Desktop/Backups'

def copy_folder_to_directory(source,dest): 
    today = datetime.today()
    dest_dir = os.path.join(dest,str(today))

    try: 
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError: 
        print(f"Folder already exist in {dest}")

copy_folder_to_directory(source_dir,destination_dir)
