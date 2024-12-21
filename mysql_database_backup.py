import os
import time
import subprocess

# MySQL database credentials
MYSQL_USER = 'roo'
MYSQL_PASSWORD = ''
MYSQL_HOST = ''
MYSQL_DATABASE = ''

# Backup directory
BACKUP_DIR = '/root/db_backup/'

# Get current date and time to create a unique backup filename
current_time = time.strftime("%Y%m%d_%H%M%S")
backup_filename = f"{MYSQL_DATABASE}_backup_{current_time}.sql"

# Full path to backup file
backup_path = os.path.join(BACKUP_DIR, backup_filename)

# Command to create a backup using mysqldump
command = f"mysqldump -u {MYSQL_USER} -p{MYSQL_PASSWORD} -h {MYSQL_HOST} {MYSQL_DATABASE} > {backup_path}"

# Run the backup command
try:
    subprocess.run(command, shell=True, check=True)
    print(f"Backup successfully created at {backup_path}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while taking the backup: {e}")
