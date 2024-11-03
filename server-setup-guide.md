# Comprehensive Server Setup Guide

## 1. Initial System Setup
Basic system configuration including updates, hostname setup, and user management.
```bash
sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y
sudo hostnamectl set-hostname rpi
sudo nano /etc/hosts
sudo timedatectl set-timezone Asia/Kolkata
sudo adduser milav
sudo usermod -aG sudo milav
```

## 2. SSH Server Setup
Install and configure SSH server with firewall rules.
```bash
sudo apt install openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh
sudo ufw allow ssh
sudo ufw allow "OpenSSH"
sudo ufw enable
sudo ufw status
```

## 3. Network Configuration
Configure network settings using netplan.
```bash
sudo nano /etc/netplan/50-cloud-init.yaml 
sudo netplan apply 
ip a
```

## 4. Git and SSH Key Setup
Generate SSH keys and clone repositories.
```bash
ssh-keygen -t ed25519 -C "milav.dabgar@gmail.com"
cat ~/.ssh/id_ed25519.pub
mkdir code
cd code
git clone git@github.com:milavdabgar/ipEmail.git
git clone git@github.com:milavdabgar/gppLMSv1.git
sudo cp milavdabgar.github.io /var/www/portfolio.planetmilav.com -r
```

## 5. PHP Installation
Install PHP and required extensions.
```bash
sudo apt install php-fpm php-mysql php-curl php-gd php-xml php-mbstring php-dom php-imagick php-zip php-intl -y
```

## 6. MariaDB Setup
Install and configure MariaDB server with databases and users.
```bash
sudo apt install mariadb-server mariadb-client -y
sudo mysql_secure_installation
sudo mysql -u root -p
sudo mysql -e "CREATE DATABASE planetmilav_com;"
sudo mysql -u root -p
sudo mysql -e "CREATE DATABASE texeg_planetmilav_com;"
sudo mysql -e "CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'seagate';"
sudo mysql -e "GRANT ALL PRIVILEGES ON planetmilav_com.* TO 'wordpress'@'localhost';"
sudo mysql -e "GRANT ALL PRIVILEGES ON texeg_planetmilav_com.* TO 'wordpress'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"
```

## 7. Nginx Web Server Setup
Install and configure Nginx with virtual hosts.
```bash
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo ufw allow "Nginx Full"

sudo nano /etc/nginx/sites-available/default 
sudo nano /etc/nginx/sites-available/planetmilav.com 
sudo nano /etc/nginx/sites-available/texeg.planetmilav.com
sudo nano /etc/nginx/sites-available/portfolio.planetmilav.com
sudo nano /etc/nginx/sites-available/postfixadmin.planetmilav.com
sudo nano /etc/nginx/sites-available/gpplmsv1.planetmilav.com
sudo nano /etc/nginx/sites-available/roundcube 
sudo nano /etc/nginx/sites-available/nextcloud

sudo ln -s /etc/nginx/sites-available/planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/texeg.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/portfolio.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/postfixadmin.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/gpplmsv1.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/roundcube /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/

sudo nginx -t
```

## 8. SSL Certificate Setup
Install and configure Let's Encrypt SSL certificates.
```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d planetmilav.com -d www.planetmilav.com -d gpplmsv1.planetmilav.com -d mail.planetmilav.com -d portfolio.planetmilav.com -d postfixadmin.planetmilav.com -d texeg.planetmilav.com -d roundcube.planetmilav.com -d nextcloud.planetmilav.com
```

## 9. Cron Jobs Setup
Configure automated tasks for SSL renewal and DNS updates.
```bash
sudo crontab -e
# 0 */12 * * * certbot renew --nginx --quiet
crontab -e
# */1 * * * * /usr/bin/python /home/milav/code/ipEmail/cloudflare-dns-update-api.py >/dev/null 2>&1
```

## 10. WordPress Installation
Download and configure WordPress installations.
```bash
sudo wget https://wordpress.org/latest.tar.gz
sudo tar -xzvf latest.tar.gz
sudo cp wordpress /var/www/texeg.planetmilav.com -r
sudo cp wordpress /var/www/planetmilav.com -r
sudo rm -rf wordpress/
sudo rm latest.tar.gz 
sudo chown -R www-data:www-data /var/www/planetmilav.com/
sudo chown -R www-data:www-data /var/www/texeg.planetmilav.com/
sudo chmod -R 755 /var/www/planetmilav.com/
sudo chmod -R 755 /var/www/texeg.planetmilav.com/
```

## 11. Git Repository Setup
Configure Git and clone necessary repositories.
```bash
mkdir code
cd code
git config --global user.name "Milav Dabgar"
git config --global user.email "milav.dabgar@gmail.com"
ssh-keygen -t ed25519 -C "milav.dabgar@gmail.com"
cat ~/.ssh/id_ed25519.pub  
git clone git@github.com:milavdabgar/ipEmail.git
git clone https://github.com/milavdabgar/milavdabgar.github.io.git
git clone git@github.com:milavdabgar/gppLMSv1.git
sudo cp milavdabgar.github.io /var/www/portfolio.planetmilav.com -r
```

## 12. Mail Server Installation
Install and configure mail server components.
```bash
sudo apt install postfix postfix-mysql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql mariadb-server nginx php-fpm php-mysql postfixadmin roundcube roundcube-mysql roundcube-plugins opendkim opendkim-tools
sudo ufw app list
sudo ufw allow "Dovecot IMAP"
sudo ufw allow "Dovecot Secure IMAP"
sudo ufw allow "Postfix"
sudo ufw allow "Postfix SMTPS"
sudo ufw allow "Postfix Submission"  
sudo groupadd -g 5000 vmail
sudo useradd -g vmail -u 5000 vmail -d /var/mail
sudo mkdir -p /var/mail/vhosts
sudo chown -R vmail:vmail /var/mail/vhosts
sudo chmod -R 770 /var/mail/vhosts
```

## 13. Mail Server Configuration
Configure mail server components and web interfaces.
```bash
### Postfix
sudo nano /etc/postfix/main.cf
sudo nano /etc/postfix/master.cf
sudo nano /etc/postfix/mysql-virtual-mailbox-domains.cf
sudo nano /etc/postfix/mysql-virtual-mailbox-maps.cf
sudo nano /etc/postfix/mysql-virtual-alias-maps.cf

### Dovecot
sudo nano /etc/dovecot/conf.d/10-auth.conf
sudo nano /etc/dovecot/conf.d/10-mail.conf
sudo nano /etc/dovecot/conf.d/10-master.conf
sudo nano /etc/dovecot/conf.d/10-ssl.conf

## Mail Web Interfaces
### Roundcube
sudo nano /etc/roundcube/config.inc.php
sudo nano /etc/roundcube/debian-db.php

### PostfixAdmin
sudo nano /etc/postfixadmin/config.inc.php
sudo nano /etc/postfixadmin/dbconfig.inc.php
```

## 14. Mail Server Testing
Test mail server functionality.
```bash
telnet localhost 25
telnet localhost 143
telnet localhost 587
telnet localhost 993
sudo postfix check
sudo dovecot -n
doveadm auth test admin@planetmilav.com
sudo apt install mailutils
echo "Mail Test" | mail -s "Mail Test" milav.dabgar@gmail.com 
```
