import os
from .logger import log_message
from utils.constants import *


def list_schedules():
    try:
        with open(SCHEDULES_FILE) as fd:
            for index, schedule in enumerate(fd):
                if schedule != "\n":
                    print(f"{index}: {schedule}", end="")
                else:
                    log_message(f"Error: Empty schedule at index {index}")
            log_message("TRACE: Show schedules list")
    except Exception as e:
        log_message(f"Error: Unexpected error while list a schedules: {e}")


def list_backups():
    try:
        if not os.path.exists(BACKUPS_DIR):
            log_message("Error: can't find backups directory")
            return
        
        files = os.listdir(BACKUPS_DIR)
        
        for file in files:
            print(file)
        
        log_message("Trace: Show backups list")

    except Exception as e:
        log_message(f"Error: Unexpected error while listing backups: {e}")
