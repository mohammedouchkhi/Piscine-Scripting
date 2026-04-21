import re
import time
from .get_schedules import get_schedules
from .backup import check_and_extract_info, make_backup
from .format import format
from datetime import datetime
from utils.constants import *



def run():
    last_processed_minute = ""
    while True:
        schedules = get_schedules()
        if schedules is None:
            exit(1)
        now = datetime.now()
        current_time_str = now.strftime("%H:%M")
        if current_time_str != last_processed_minute: 
            remaining = []
            for schedule in schedules:
                stripped = schedule.strip()
                if not stripped:
                    continue
                info = check_and_extract_info(schedule)
                if info is not None:
                    path, backup_name = info
                    make_backup(path, backup_name)
                else:
                    m = re.match(SCHEDULES_PATTERN, stripped)
                    if m:
                        sched_time = m.group(2)
                        if sched_time > current_time_str:
                            remaining.append(schedule)
                    else:
                        remaining.append(schedule)

            try:
                with open(SCHEDULES_FILE, "w") as f:
                    f.writelines(remaining)
            except Exception as e:
                print(format(f"Error: Could not update schedules file: {e}"))

        last_processed_minute = current_time_str
            
        
        time.sleep(45)