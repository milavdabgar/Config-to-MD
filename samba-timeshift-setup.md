# Timeshift Backup Setup with TP-Link Samba Share

## 1. Install Required Packages
```bash
# Install CIFS utils for mounting Samba shares
sudo apt install cifs-utils
```

## 2. Create Mount Point and Credentials
```bash
# Create mount point
sudo mkdir -p /mnt/backup-drive

# Create credentials file (more secure than putting credentials in fstab)
sudo nano /root/.smbcredentials
```

Add to `.smbcredentials`:
```plaintext
username=milav
password=seagate@123
```

```bash
# Secure the credentials file
sudo chmod 600 /root/.smbcredentials
```

## 3. Configure Automatic Mounting

```bash
# Create backup directory
sudo mkdir -p /mnt/backup-drive

# Add mount entry to fstab
sudo nano /etc/fstab
```

Add this line to `/etc/fstab`:
```plaintext
//tp-share/g/Backups/rpi /mnt/backup-drive cifs credentials=/root/.smbcredentials,iocharset=utf8,file_mode=0777,dir_mode=0777,noperm 0 0
```

## 4. Test and Mount
```bash
# Test fstab entry
sudo mount -a

# Verify mount
df -h /mnt/backup-drive
ls -la /mnt/backup-drive
```

## 5. Configure Timeshift

### 5.1 Create Base Configuration
```bash
# Configure Timeshift
sudo timeshift --configure
```

Settings to use:
- Snapshot Type: RSYNC
- Snapshot Location: /mnt/backup-drive
- Schedule: Enable scheduled snapshots
- Levels: Monthly-2, Weekly-3, Daily-5
- Users: Include all users

### 5.2 Configure Exclusions
```bash
sudo nano /etc/timeshift/timeshift.json
```

Add these exclusions:
```json
{
  "exclude": {
    "folders": [
      "/var/lib/docker/**",
      "/home/*/docker/**",
      "/var/cache/apt/archives/**",
      "/home/*/code/**",
      "/home/*/.cache/**",
      "/var/log/**",
      "/tmp/**",
      "/mnt/backup-drive/**"
    ]
  }
}
```

## 6. Backup Scripts

### 6.1 Create Backup Check Script
```bash
sudo nano /usr/local/bin/check-backup-mount.sh
```

Add:
```bash
#!/bin/bash

# Check if backup drive is mounted
if ! mountpoint -q /mnt/backup-drive; then
    echo "Backup drive not mounted, attempting to mount..."
    sudo mount -a
    
    # Check if mount successful
    if ! mountpoint -q /mnt/backup-drive; then
        echo "Failed to mount backup drive!"
        exit 1
    fi
fi

# Check available space
SPACE=$(df -h /mnt/backup-drive | awk 'NR==2 {print $4}')
USAGE=$(df -h /mnt/backup-drive | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$USAGE" -gt 85 ]; then
    echo "Warning: Backup drive usage at ${USAGE}%"
    echo "Available space: ${SPACE}"
fi
```

### 6.2 Create Backup Script
```bash
sudo nano /usr/local/bin/run-backup.sh
```

Add:
```bash
#!/bin/bash

# Source directory for logging
LOG_DIR="/var/log/timeshift-backups"
mkdir -p $LOG_DIR

# Current date for logging
DATE=$(date '+%Y-%m-%d_%H-%M-%S')
LOG_FILE="$LOG_DIR/backup_$DATE.log"

# Check mount
/usr/local/bin/check-backup-mount.sh >> "$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "Mount check failed, aborting backup" >> "$LOG_FILE"
    exit 1
fi

# Create snapshot
echo "Starting backup at $(date)" >> "$LOG_FILE"
sudo timeshift --create --comments "Auto backup $DATE" >> "$LOG_FILE" 2>&1

# Clean old snapshots (keep last 10)
echo "Cleaning old snapshots" >> "$LOG_FILE"
sudo timeshift --delete --snapshots-to-keep 10 >> "$LOG_FILE" 2>&1

echo "Backup completed at $(date)" >> "$LOG_FILE"
```

```bash
# Make scripts executable
sudo chmod +x /usr/local/bin/check-backup-mount.sh
sudo chmod +x /usr/local/bin/run-backup.sh
```

## 7. Schedule Automated Backups

### 7.1 Create Systemd Timer
```bash
sudo nano /etc/systemd/system/timeshift-backup.timer
```

Add:
```ini
[Unit]
Description=Daily Timeshift Backup

[Timer]
OnCalendar=*-*-* 02:00:00
RandomizedDelaySec=1800
Persistent=true

[Install]
WantedBy=timers.target
```

### 7.2 Create Systemd Service
```bash
sudo nano /etc/systemd/system/timeshift-backup.service
```

Add:
```ini
[Unit]
Description=Timeshift Backup Service
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/run-backup.sh
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

### 7.3 Enable Services
```bash
sudo systemctl enable timeshift-backup.timer
sudo systemctl start timeshift-backup.timer
```

## 8. Recovery Process

### 8.1 Manual Recovery Steps
1. Mount the backup drive:
```bash
sudo mount -a
```

2. List available snapshots:
```bash
sudo timeshift --list
```

3. Restore selected snapshot:
```bash
sudo timeshift --restore --snapshot '2024-03-03_02-00-01'
```

### 8.2 Emergency Recovery
If system won't boot:
1. Boot from Ubuntu Live USB
2. Install Timeshift on Live USB:
```bash
sudo apt install timeshift
```

3. Mount backup drive:
```bash
sudo mkdir /mnt/backup
sudo mount -t cifs //tp-share/g/Backups/rpi /mnt/backup -o username=milav,password=seagate@123
```

4. Restore using Timeshift from Live USB
