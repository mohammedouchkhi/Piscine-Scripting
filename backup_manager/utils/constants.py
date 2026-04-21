

SCHEDULES_FILE = "backup_schedules.txt"
LOGS_DIR = "logs"
MANAGERE_LOG_FILE = "backup_manager.log"
SERVICE_LOG_FILE = "backup_service.log"
MANAGERE_LOG = LOGS_DIR + "/" + MANAGERE_LOG_FILE
SERVICE_LOG = LOGS_DIR + "/" + SERVICE_LOG_FILE
BACKUPS_DIR = "backups"
SCHEDULES_PATTERN = r"^([^;]+);(([01][0-9]|2[0-3]):[0-5][0-9]);([^;/]+)$"
TARGET_SCRIPT = "backup_service.py"