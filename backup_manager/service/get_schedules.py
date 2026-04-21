from utils.constants import *
from .format import format
def get_schedules() -> list[str]:
    try:
        with open(SCHEDULES_FILE) as fd:
            return fd.readlines()
    except Exception as e:
        print(format(e))
        return None