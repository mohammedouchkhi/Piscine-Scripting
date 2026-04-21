#### General

##### Check Submission Structure

```
backup-manager/
├── backup_manager.py              # CLI script for managing schedules and service
├── backup_service.py              # Background service that performs scheduled backups
├── logs/                          # Directory for log files (created at runtime)
│   ├── backup_manager.log         # Logs from backup_manager.py
│   └── backup_service.log         # Logs from backup_service.py
├── backups/                       # Directory for backup .tar files (created at runtime)
├── backup_schedules.txt           # Schedule file (created at runtime)
└── README.md                      # Project documentation
```

###### Are `backup_manager.py` and `backup_service.py` present in the submission?

##### Play the Role of a Stakeholder

The auditor plays the role of an engineering manager at a small company. Spend 10-15 minutes with the learners asking these questions:

1. How does `backup_manager.py` communicate with `backup_service.py`?
2. How does the background service detect when a scheduled backup time arrives?
3. How are past-due schedules handled by the service?
4. What approach did they take for process management (start/stop)?
5. How does the logging system work across both scripts?

###### Can the learners explain the architecture and flow of the backup system clearly?

###### Can the learners justify their technical decisions?

###### Do the learners demonstrate understanding of process management, file I/O, and error handling?

##### Part 1: Schedule Management

Run `rm -dr logs backups backup_schedules.txt` to start with a clean environment.

###### After running `python3 ./backup_manager.py create "test2;18:15;backup_test2"`, is the `backup_schedules.txt` file created with the correct schedule entry?

##### Create a couple more schedules and run `python3 ./backup_manager.py list`.

###### Does the list command display all schedules with an index at the beginning of each entry?

##### Run `python3 ./backup_manager.py delete 1` and then `python3 ./backup_manager.py list`.

###### Is the schedule at index 1 removed from the list?

###### Did the remaining schedules reindex correctly after deletion?

##### Part 2: Service Control

Run `python3 ./backup_manager.py start`.

###### Does the `backup_service.py` process start and run in the background?

##### Run `python3 ./backup_manager.py start` again while the service is already running.

###### Does the log file contain an error stating that the service is already running?

##### Run `python3 ./backup_manager.py stop`.

###### Does the service stop successfully?

##### Run `python3 ./backup_manager.py stop` again while the service is already stopped.

###### Does the log file contain an error stating that the service cannot be stopped?

##### Part 3: Backup Execution

Run `rm -dr logs backups backup_schedules.txt` to reset. Then run the following:

```bash
mkdir testing; touch testing/file1 testing/file2 testing/file3
python3 ./backup_manager.py create "testing;[Current_hour];backup_test"
python3 ./backup_manager.py create "testing;13:11;passed_time_backup"
python3 ./backup_manager.py start
```

Wait for the service to process, then run `python3 ./backup_manager.py backups`.

###### Is the `backup_test.tar` file created in the `./backups` directory?

###### Does the `.tar` file contain the correct files matching the original directory?

###### Is the past-due schedule (`passed_time_backup`) correctly not created or removed from `backup_schedules.txt`?

##### Part 4: Logging and Error Handling

###### Does `./logs/backup_manager.log` contain timestamped entries for all actions performed?

###### Does `./logs/backup_service.log` contain timestamped entries for completed backups?

##### Run `python3 ./backup_manager.py invalid_command`.

###### Does the log file contain an error for the unknown command?

##### Run `python3 ./backup_manager.py create "wrong_format"`.

###### Does the log file contain an error for the malformed schedule?

##### Run `python3 ./backup_manager.py backups` before any backups directory exists.

###### Does the log file contain an error stating that the backups directory cannot be found?

##### Examine the source code of both scripts.

###### Do the learners use `try` and `except` blocks to handle errors in both scripts?

##### Submission Completeness

###### Does the project include a README.md file with project documentation?

#### Bonus

###### + Does the project exceed the requirements in any other meaningful way?