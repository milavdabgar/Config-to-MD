# Server Management and Deployment Strategy Guide

## 1. System Level Protection (Timeshift)

```bash
# Install Timeshift
sudo apt install timeshift

# Create base snapshot after fresh OS install
sudo timeshift --create --comments "Fresh OS Install"

# Create snapshot before major system changes
sudo timeshift --create --comments "Before Mail Server Setup"

# Setup automated snapshots
sudo timeshift --create --schedule --weekly 3 --monthly 2
```

Important Timeshift Strategy:
- Create snapshots before installing any system-level services
- Keep at least 3 weekly and 2 monthly backups
- Store snapshot list in a text file with descriptions

## 2. Docker-based Services Setup

### 2.1 Install Docker and Docker Compose
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose

# Add user to docker group
sudo usermod -aG docker $USER
```

### 2.2 Create Docker Network
```bash
# Create network for all containers
docker network create web-network
```

### 2.3 Directory Structure
```
/home/milav/docker/
├── nginx-proxy/
│   ├── docker-compose.yml
│   └── nginx.conf
├── nextcloud/
│   ├── docker-compose.yml
│   └── data/
├── wordpress/
│   ├── docker-compose.yml
│   ├── wp-content/
│   └── database/
└── mail-server/
    ├── docker-compose.yml
    └── data/
```

### 2.4 Sample Docker Compose Files

1. Nginx Reverse Proxy (`nginx-proxy/docker-compose.yml`):
```yaml
version: '3'
services:
  nginx-proxy:
    image: nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - /etc/letsencrypt:/etc/letsencrypt:ro
    networks:
      - web-network
    restart: unless-stopped

networks:
  web-network:
    external: true
```

2. NextCloud (`nextcloud/docker-compose.yml`):
```yaml
version: '3'
services:
  nextcloud:
    image: nextcloud
    volumes:
      - ./data:/var/www/html
    networks:
      - web-network
    restart: unless-stopped

  nextcloud-db:
    image: mariadb
    environment:
      - MYSQL_ROOT_PASSWORD=seagate
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=seagate
    volumes:
      - ./database:/var/lib/mysql
    networks:
      - web-network
    restart: unless-stopped

networks:
  web-network:
    external: true
```

3. Flask+Vue Application Template (`webapp/docker-compose.yml`):
```yaml
version: '3'
services:
  frontend:
    build: ./frontend
    volumes:
      - ./frontend:/app
    networks:
      - web-network

  backend:
    build: ./backend
    command: gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
    volumes:
      - ./backend:/app
    networks:
      - web-network

networks:
  web-network:
    external: true
```

## 3. Samba Share Setup (System Level)
```bash
# Install Samba
sudo apt install samba

# Create share directory
sudo mkdir -p /srv/samba/share

# Configure Samba
sudo nano /etc/samba/smb.conf
```

Add to `smb.conf`:
```ini
[share]
    path = /srv/samba/share
    browseable = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = milav
```

## 4. Backup Strategy

### 4.1 Docker Volumes Backup
```bash
# Create backup script
nano ~/scripts/backup-docker.sh
```

Content of `backup-docker.sh`:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR="/backup/docker"

# Stop containers
docker-compose -f /home/milav/docker/nextcloud/docker-compose.yml down

# Backup volumes
tar -czf $BACKUP_DIR/nextcloud-$DATE.tar.gz /home/milav/docker/nextcloud/data

# Restart containers
docker-compose -f /home/milav/docker/nextcloud/docker-compose.yml up -d
```

### 4.2 System Configuration Backup
```bash
# Create backup script
nano ~/scripts/backup-config.sh
```

Content of `backup-config.sh`:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR="/backup/config"

# Backup important configs
tar -czf $BACKUP_DIR/configs-$DATE.tar.gz \
    /etc/nginx \
    /etc/samba \
    /home/milav/docker
```

## 5. Recovery Procedures

### 5.1 Docker Container Recovery
```bash
# Stop affected container
docker-compose down

# Remove container and volume
docker-compose rm -v

# Restore from backup if needed
tar -xzf /backup/docker/nextcloud-20240303.tar.gz -C /

# Recreate container
docker-compose up -d
```

### 5.2 System Level Recovery
```bash
# List snapshots
sudo timeshift --list

# Restore specific snapshot
sudo timeshift --restore --snapshot '2024-03-03_00-00-01'
```

## 6. Monitoring

### 6.1 Install Monitoring Tools
```bash
# Install monitoring tools
sudo apt install htop iotop nethogs
```

### 6.2 Docker Monitoring
```bash
# Monitor container resources
docker stats

# View container logs
docker-compose logs -f
```

## 7. Best Practices

1. System Level:
   - Use Timeshift before any system-level changes
   - Keep configuration files in version control
   - Regular security updates

2. Docker:
   - Use docker-compose for all containers
   - Never store secrets in docker-compose files
   - Use .env files for configurations
   - Regular image updates

3. Backups:
   - Automated daily backups
   - Regular backup testing
   - Off-site backup copies

4. Security:
   - Regular security audits
   - Keep SSL certificates updated
   - Monitor system logs
