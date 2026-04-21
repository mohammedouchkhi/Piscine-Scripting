from datetime import datetime

def format(message):
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    return f"{timestamp} {message}\n"