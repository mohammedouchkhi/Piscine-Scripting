import re
import os
from .logger import log_message
from utils.constants import *


def create(schedule):
    try:
        if re.match(SCHEDULES_PATTERN, schedule):
            with open(SCHEDULES_FILE, "a+") as fd:
                fd.write(f"{schedule}\n")
                log_message(f"INFO: New schedule added => {schedule}")
        else:
            log_message(f"Error: malformed schedule: {schedule}")
    except Exception as e:
        log_message(f"Error: Unexpected error while adding a schedule: {e}")


def delete_schedule(index_str):
    try:
        try:
            index = int(index_str)
        except ValueError:
            log_message(f"Error: index '{index_str}' is not a valid number")
            return

        if not os.path.exists(SCHEDULES_FILE):
            log_message(f"Error: can't find backup_schedules.txt")
            return

        with open(SCHEDULES_FILE, "r") as fr:
            lines = fr.readlines()

        if index < 0 or index >= len(lines):
            log_message(f"Error: can't find schedule at index {index}")
            return

        removedLine = lines.pop(index)

        with open(SCHEDULES_FILE, "w") as f:
            f.writelines(lines)

        log_message(f"Trace: Schedule at index {index} deleted => {removedLine}")
    except Exception as e:
        log_message(f"Error: Unexpected error while deleting: {e}")
