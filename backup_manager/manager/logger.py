from datetime import datetime
from utils.constants import *

def log_message(message):
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    formatted_message = f"{timestamp} {message.strip()}"
    
    
    try:
        with open(MANAGERE_LOG, "a") as f:
            f.write("\n" + formatted_message + "\n")
    except Exception as e:
        print(f"Critical Error: Could not write to log file. {e}")