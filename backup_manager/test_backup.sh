#!/bin/bash
# Test script for Backup Manager
# Usage: bash test_backup.sh

cd "$(dirname "$0")"

echo "=== CLEANING UP ==="
rm -f backup_schedules.txt
rm -rf backups/ logs/
rm -rf test test1 test2
mkdir -p test test1 test2

# Get the NEXT minute for scheduling
NEXT_MIN=$(date -d "+1 minute" +%H:%M 2>/dev/null || date -v+1M +%H:%M 2>/dev/null)
echo "Scheduling backups for: $NEXT_MIN"

echo ""
echo "=== CREATING SCHEDULES ==="
python3 ./backup_manager.py create "test;${NEXT_MIN};backup_test"
python3 ./backup_manager.py create "test1;${NEXT_MIN};personal_data"
python3 ./backup_manager.py create "test2;${NEXT_MIN};office_docs"
python3 ./backup_manager.py create "test;"

echo ""
echo "=== LISTING SCHEDULES ==="
python3 ./backup_manager.py list

echo ""
echo "=== STARTING SERVICE ==="
python3 ./backup_manager.py start

echo "Waiting for scheduled time ($NEXT_MIN) to arrive..."
echo "(This may take up to 90 seconds)"
sleep 90

echo ""
echo "=== STOPPING SERVICE ==="
python3 ./backup_manager.py stop

echo ""
echo "=== LISTING BACKUPS ==="
python3 ./backup_manager.py backups

echo ""
echo "=== MANAGER LOG ==="
cat ./logs/backup_manager.log

echo ""
echo "=== SERVICE LOG ==="
cat ./logs/backup_service.log

echo ""
echo "=== SCHEDULES FILE (should be empty after processing) ==="
cat backup_schedules.txt 2>/dev/null || echo "(file is empty or missing)"

echo ""
echo "=== BACKUP FILES ==="
ls ./backups 2>/dev/null || echo "(no backups directory)"
