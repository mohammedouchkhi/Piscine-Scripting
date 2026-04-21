import re
import os
import tarfile
from datetime import datetime
from .format import format
from utils.constants import *


def check_and_extract_info(schedule):
    m = re.match(SCHEDULES_PATTERN, schedule)
    if m is None:
        return None

    path,  time_string, _, backup_name = m.groups()
    backup_time = datetime.strptime(time_string, "%H:%M").strftime("%H:%M")
    current_time = datetime.now().strftime("%H:%M")
    
    if backup_time != current_time:
        return None
    
    return path, backup_name.strip()


def make_backup(path: str, backup_name: str):
    try:
        if not backup_name.endswith(".tar"):
            backup_name = f"{backup_name}.tar"
            
        destination = BACKUPS_DIR + "/" + backup_name
        
        with tarfile.open(destination, "w") as tar:
            tar.add(path) 

        print(format(f"INFO: Backup done for {path} in backups/{backup_name}"))
            
    except Exception as e:
        print(format(f"Error: Failed to create backup for {path}: {e}"))
