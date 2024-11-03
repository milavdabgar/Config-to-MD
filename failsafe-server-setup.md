# Failsafe Server Setup Guide
## Level 1: Initial System Setup and Protection

### 1.1 Basic System Configuration
```bash
# System updates
sudo apt update && sudo apt dist-upgrade -y

# Set hostname and timezone
sudo hostnamectl set-hostname rpi
sudo timedatectl set-timezone Asia/Kolkata

# Create user
sudo adduser milav
sudo usermod -aG sudo milav

# Edit /etc/hosts
sudo nano /etc/hosts
```
Add:
```plaintext
127.0.0.1 localhost
127.0.1.1 rpi.planetmilav.com rpi
192.168.0.50 mail.planetmilav.com
```

### 1.2 Install Timeshift
```bash
# Install Timeshift
sudo apt install timeshift

# Create base snapshot
sudo timeshift --create --comments "Fresh system install"

# Configure automated snapshots
sudo timeshift --create --schedule --weekly 3 --monthly 2
```

### 1.3 Setup SSH and Firewall
```bash
# Install and configure SSH
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh

# Setup UFW
sudo apt install ufw
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### 1.4 Network Configuration
```bash
# Edit netplan configuration
sudo nano /etc/netplan/50-cloud-init.yaml
```
Add your network configuration as in your original setup.

```bash
# Apply configuration
sudo netplan apply
```

## Level 2: Native Services Setup

### 2.1 Samba Share (Native Installation)
```bash
# Install Samba
sudo apt install samba

# Create timeshift snapshot
sudo timeshift --create --comments "Before Samba setup"

# Create share directory
sudo mkdir -p /srv/samba/share
sudo chown -R milav:milav /srv/samba/share
sudo chmod -R 770 /srv/samba/share

# Configure Samba
sudo nano /etc/samba/smb.conf
```
Add:
```ini
[share]
    path = /srv/samba/share
    browseable = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = milav
```

```bash
# Set Samba password
sudo smbpasswd -a milav

# Restart Samba
sudo systemctl restart smbd
```

## Level 3: Docker Setup

### 3.1 Install Docker and Docker Compose
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose

# Add user to docker group
sudo usermod -aG docker $USER

# Create timeshift snapshot
sudo timeshift --create --comments "After Docker installation"
```

### 3.2 Create Docker Networks
```bash
# Create networks
docker network create web-network
docker network create mail-network
```

### 3.3 Create Directory Structure
```bash
# Create directories
mkdir -p ~/docker/{nginx-proxy,wordpress,mysql,mail,portfolio}
```

## Level 4: Web Services Setup

### 4.1 MySQL/MariaDB Container
Create `~/docker/mysql/docker-compose.yml`:
```yaml
version: '3'

services:
  db:
    image: mariadb:latest
    container_name: mariadb
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: seagate
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - web-network

volumes:
  mysql_data:

networks:
  web-network:
    external: true
```

```bash
# Start MariaDB
cd ~/docker/mysql
docker-compose up -d

# Create databases
docker exec -it mariadb mysql -u root -pseagate -e "
CREATE DATABASE planetmilav_com;
CREATE DATABASE texeg_planetmilav_com;
CREATE USER 'wordpress'@'%' IDENTIFIED BY 'seagate';
GRANT ALL PRIVILEGES ON planetmilav_com.* TO 'wordpress'@'%';
GRANT ALL PRIVILEGES ON texeg_planetmilav_com.* TO 'wordpress'@'%';
FLUSH PRIVILEGES;"
```

### 4.2 Nginx Proxy Setup
Create `~/docker/nginx-proxy/docker-compose.yml`:
```yaml
version: '3'

services:
  nginx-proxy:
    image: nginx:latest
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./sites:/etc/nginx/sites-enabled:ro
      - /etc/letsencrypt:/etc/letsencrypt:ro
      - web_root:/var/www/html
    networks:
      - web-network
    restart: unless-stopped

volumes:
  web_root:

networks:
  web-network:
    external: true
```

Create nginx configuration files in `~/docker/nginx-proxy/sites/`.

### 4.3 WordPress Sites
Create `~/docker/wordpress/docker-compose.yml`:
```yaml
version: '3'

services:
  wordpress-planetmilav:
    image: wordpress:latest
    container_name: wordpress-planetmilav
    environment:
      WORDPRESS_DB_HOST: mariadb
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: seagate
      WORDPRESS_DB_NAME: planetmilav_com
    volumes:
      - wp_planetmilav:/var/www/html
    networks:
      - web-network
    restart: unless-stopped

  wordpress-texeg:
    image: wordpress:latest
    container_name: wordpress-texeg
    environment:
      WORDPRESS_DB_HOST: mariadb
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: seagate
      WORDPRESS_DB_NAME: texeg_planetmilav_com
    volumes:
      - wp_texeg:/var/www/html
    networks:
      - web-network
    restart: unless-stopped

volumes:
  wp_planetmilav:
  wp_texeg:

networks:
  web-network:
    external: true
```

### 4.4 Portfolio Site
Create `~/docker/portfolio/docker-compose.yml`:
```yaml
version: '3'

services:
  portfolio:
    image: nginx:alpine
    container_name: portfolio
    volumes:
      - ./site:/usr/share/nginx/html:ro
    networks:
      - web-network
    restart: unless-stopped

networks:
  web-network:
    external: true
```

## Level 5: Mail Server Setup

### 5.1 Mail Server Components
Create `~/docker/mail/docker-compose.yml`:
```yaml
version: '3'

services:
  mailserver:
    image: docker-mailserver/docker-mailserver:latest
    container_name: mailserver
    hostname: mail.planetmilav.com
    ports:
      - "25:25"
      - "587:587"
      - "993:993"
    volumes:
      - mail_data:/var/mail
      - mail_state:/var/mail-state
      - mail_logs:/var/log/mail
      - ./config:/tmp/docker-mailserver
      - /etc/letsencrypt:/etc/letsencrypt:ro
    environment:
      - ENABLE_SPAMASSASSIN=1
      - ENABLE_CLAMAV=1
      - ENABLE_FAIL2BAN=1
      - SSL_TYPE=manual
      - SSL_CERT_PATH=/etc/letsencrypt/live/planetmilav.com/fullchain.pem
      - SSL_KEY_PATH=/etc/letsencrypt/live/planetmilav.com/privkey.pem
    networks:
      - mail-network
    restart: unless-stopped

  roundcube:
    image: roundcube/roundcubemail:latest
    container_name: roundcube
    depends_on:
      - mailserver
    volumes:
      - roundcube_data:/var/www/html
    environment:
      - ROUNDCUBEMAIL_DEFAULT_HOST=tls://mail.planetmilav.com
      - ROUNDCUBEMAIL_SMTP_SERVER=tls://mail.planetmilav.com
    networks:
      - mail-network
      - web-network
    restart: unless-stopped

  postfixadmin:
    image: postfixadmin/postfixadmin:latest
    container_name: postfixadmin
    depends_on:
      - mailserver
    volumes:
      - postfixadmin_data:/var/www/html
    networks:
      - mail-network
      - web-network
    restart: unless-stopped

volumes:
  mail_data:
  mail_state:
  mail_logs:
  roundcube_data:
  postfixadmin_data:

networks:
  mail-network:
    external: true
  web-network:
    external: true
```

## Level 6: SSL Certificates

### 6.1 Install Certbot
```bash
# Install certbot
sudo apt install python3-certbot-nginx

# Create timeshift snapshot
sudo timeshift --create --comments "Before SSL setup"

# Get certificates
sudo certbot --nginx -d planetmilav.com -d www.planetmilav.com \
  -d mail.planetmilav.com -d portfolio.planetmilav.com \
  -d texeg.planetmilav.com -d roundcube.planetmilav.com \
  -d postfixadmin.planetmilav.com
```

## Level 7: Backup Strategy

### 7.1 Create Backup Scripts
Create `~/scripts/backup-docker.sh`:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
BACKUP_DIR="/backup/docker"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup docker volumes
docker run --rm \
  -v wordpress_planetmilav:/source:ro \
  -v $BACKUP_DIR:/backup \
  alpine tar czf /backup/wordpress-planetmilav-$DATE.tar.gz /source

docker run --rm \
  -v mail_data:/source:ro \
  -v $BACKUP_DIR:/backup \
  alpine tar czf /backup/mail-data-$DATE.tar.gz /source

# Backup MariaDB
docker exec mariadb mysqldump -u root -pseagate --all-databases \
  | gzip > $BACKUP_DIR/databases-$DATE.sql.gz
```

### 7.2 Setup Cron Jobs
```bash
# Edit crontab
crontab -e
```
Add:
```bash
0 2 * * * /home/milav/scripts/backup-docker.sh
0 */12 * * * certbot renew --quiet
```

## Level 8: Recovery Procedures

### 8.1 Docker Volume Recovery
```bash
# Stop affected containers
docker-compose down

# Restore volume
docker run --rm \
  -v wordpress_planetmilav:/target \
  -v /backup/docker:/backup \
  alpine sh -c "cd /target && tar xzf /backup/wordpress-planetmilav-20240303.tar.gz --strip 1"

# Restart containers
docker-compose up -d
```

### 8.2 System Recovery
```bash
# List snapshots
sudo timeshift --list

# Restore snapshot
sudo timeshift --restore --snapshot '2024-03-03_00-00-01'
```

## Level 9: Monitoring and Maintenance

### 9.1 Install Monitoring Tools
```bash
# Install tools
sudo apt install htop iotop nethogs

# Monitor docker
docker stats

# View logs
docker-compose logs -f
```

### 9.2 Regular Maintenance Tasks
1. Check system logs daily
2. Monitor disk space
3. Update containers weekly
4. Test backups monthly
5. Verify SSL certificates monthly

Would you like me to:
1. Provide more detailed configuration for any specific service?
2. Add monitoring and alert setup?
3. Create automated deployment scripts?