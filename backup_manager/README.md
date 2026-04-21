# Backup Manager

A Python-based backup system that schedules and performs automated backups from the command line. It allows users to create, list, and delete backup schedules, control a background service, and generate compressed `.tar` backup files.

## Project Structure

```
backup_manager/
├── backup_manager.py         # CLI script for managing schedules and service
├── backup_service.py         # Background service that performs scheduled backups
├── manager/                  # Manager module
│   ├── command.py            # Command routing and service control (start/stop)
│   ├── schedules.py          # Schedule creation and deletion
│   ├── display.py            # List schedules and backups
│   └── logger.py             # Logging for backup_manager
├── service/                  # Service module
│   ├── event_loop.py         # Main loop that checks schedules
│   ├── backup.py             # Parse schedules and create .tar archives
│   ├── get_schedules.py      # Read schedules from file
│   └── format.py             # Log formatting for the service
├── utils/                    # Shared utilities
│   ├── constants.py          # Shared constants and paths
│   └── create_dir.py         # Directory creation helper
├── logs/                     # Log files (created at runtime)
│   ├── backup_manager.log
│   └── backup_service.log
├── backups/                  # Backup .tar files (created at runtime)
├── backup_schedules.txt      # Schedule file (created at runtime)
└── README.md
```

## Requirements

- Python 3.10+

## Usage

### Create a backup schedule

The schedule format is `"path_to_save;HH:MM;backup_name"`.

```bash
python3 ./backup_manager.py create "my_folder;14:30;my_backup"
```

### List scheduled backups

```bash
python3 ./backup_manager.py list
```

### Delete a schedule by index

```bash
python3 ./backup_manager.py delete 0
```

### Start the backup service

Launches `backup_service.py` in the background. The service checks schedules every 45 seconds and creates `.tar` backups when the current time matches a scheduled time. Processed and past-due schedules are automatically removed.

```bash
python3 ./backup_manager.py start
```

### Stop the backup service

```bash
python3 ./backup_manager.py stop
```

### List completed backups

```bash
python3 ./backup_manager.py backups
```

## Example

```bash
# Create test directories to back up
mkdir -p project_files documents

# Schedule backups (replace 14:30 with the desired time)
python3 ./backup_manager.py create "project_files;14:30;project_backup"
python3 ./backup_manager.py create "documents;14:30;docs_backup"

# Verify schedules
python3 ./backup_manager.py list
# Output:
# 0: project_files;14:30;project_backup
# 1: documents;14:30;docs_backup

# Start the service and let it run until the scheduled time
python3 ./backup_manager.py start

# After the scheduled time has passed, stop and check
python3 ./backup_manager.py stop
python3 ./backup_manager.py backups
# Output:
# project_backup.tar
# docs_backup.tar
```

## Logging

All actions and errors are logged with timestamps in `[dd/mm/yyyy HH:MM]` format:

- `backup_manager.py` logs to `./logs/backup_manager.log`
- `backup_service.py` logs to `./logs/backup_service.log`