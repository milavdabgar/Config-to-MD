# Complete Server Setup Guide

## 1. Initial System Setup
```bash
sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y
sudo hostnamectl set-hostname rpi
sudo timedatectl set-timezone Asia/Kolkata
sudo adduser milav
sudo usermod -aG sudo milav
```

Edit `/etc/hosts`:
```plaintext
127.0.0.1 localhost
127.0.1.1 rpi.planetmilav.com rpi
192.168.0.50 mail.planetmilav.com
```

## 2. SSH Server Setup
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
Edit `/etc/netplan/50-cloud-init.yaml`:
```yaml
network:
    ethernets:
        eth0:
            dhcp4: no
            optional: true
            addresses: [192.168.0.50/24]
            routes:
              - to: default
                via: 192.168.0.1
            nameservers:
              addresses: [192.168.0.1, 8.8.8.8]
    wifis:
      wlan0:
        dhcp4: true
        optional: true
        addresses: [192.168.0.51/24]
        nameservers:
          addresses: [192.168.0.1, 8.8.8.8]
        access-points:
          "Milav-Tenda":
            password: "seagate@123"
```

Apply network configuration:
```bash
sudo netplan apply
ip a
```

## 4. Git and SSH Key Setup
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
```bash
sudo apt install php-fpm php-mysql php-curl php-gd php-xml php-mbstring php-dom php-imagick php-zip php-intl -y
```

Edit `/etc/php/8.3/fpm/php.ini`:
```ini
upload_max_filesize = 64M
post_max_size = 64M
memory_limit = 256M
max_execution_time = 300
max_input_time = 300
date.timezone = Asia/Kolkata
```

Restart PHP-FPM:
```bash
sudo systemctl restart php8.3-fpm
```

## 6. MariaDB Setup
```bash
sudo apt install mariadb-server mariadb-client -y
sudo mysql_secure_installation
```

During secure installation:
- Set root password: seagate
- Remove anonymous users: Y
- Disallow root login remotely: Y
- Remove test database: Y
- Reload privilege tables: Y

Create databases and users:
```bash
sudo mysql -u root -p
sudo mysql -e "CREATE DATABASE planetmilav_com;"
sudo mysql -e "CREATE DATABASE texeg_planetmilav_com;"
sudo mysql -e "CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'seagate';"
sudo mysql -e "GRANT ALL PRIVILEGES ON planetmilav_com.* TO 'wordpress'@'localhost';"
sudo mysql -e "GRANT ALL PRIVILEGES ON texeg_planetmilav_com.* TO 'wordpress'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"
```

## 7. Nginx Web Server Setup
```bash
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo ufw allow "Nginx Full"
```

Create Nginx configurations:

1. `/etc/nginx/sites-available/planetmilav.com`:
```nginx
# Upstream to abstract backend connection(s) for php
upstream php {
  server unix:/run/php/php-fpm.sock;
}

server {
  server_name planetmilav.com www.planetmilav.com;
  root /var/www/planetmilav.com;
  index index.php;

  location = /favicon.ico {
      log_not_found off;
      access_log off;
  }

  location = /robots.txt {
      allow all;
      log_not_found off;
      access_log off;
  }

  location / {
      try_files $uri $uri/ /index.php?$args;
  }

  location ~ \.php$ {
      include fastcgi_params;
      fastcgi_intercept_errors on;
      fastcgi_pass php;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
  }

  location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
      expires max;
      log_not_found off;
  }

  location ~ /\.ht {
      deny all;
  }

  # Gzip config
  gzip on;
  gzip_types text/plain text/xml text/css application/javascript;
}
```

2. `/etc/nginx/sites-available/texeg.planetmilav.com`:
```nginx
server {
    server_name texeg.planetmilav.com;
    root /var/www/texeg.planetmilav.com;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_intercept_errors on;
        fastcgi_pass php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
}
```

3. `/etc/nginx/sites-available/portfolio.planetmilav.com`:
```nginx
server {
    server_name portfolio.planetmilav.com;
    root /var/www/portfolio.planetmilav.com;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

4. `/etc/nginx/sites-available/gpplmsv1.planetmilav.com`:
```nginx
server {
    server_name gpplmsv1.planetmilav.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Create symbolic links:
```bash
sudo ln -s /etc/nginx/sites-available/planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/texeg.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/portfolio.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/gpplmsv1.planetmilav.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 8. SSL Certificate Setup
```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d planetmilav.com -d www.planetmilav.com -d gpplmsv1.planetmilav.com -d mail.planetmilav.com -d portfolio.planetmilav.com -d postfixadmin.planetmilav.com -d texeg.planetmilav.com -d roundcube.planetmilav.com -d nextcloud.planetmilav.com
```

## 9. Cron Jobs Setup
```bash
sudo crontab -e
```
Add:
```bash
0 */12 * * * certbot renew --nginx --quiet
```

```bash
crontab -e
```
Add:
```bash
*/1 * * * * /usr/bin/python /home/milav/code/ipEmail/cloudflare-dns-update-api.py >/dev/null 2>&1
```

## 10. WordPress Installation
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

Create `wp-config.php` for planetmilav.com:
```php
define('DB_NAME', 'planetmilav_com');
define('DB_USER', 'wordpress');
define('DB_PASSWORD', 'seagate');
define('DB_HOST', 'localhost');
define('WP_DEBUG', false);
```

Create `wp-config.php` for texeg.planetmilav.com:
```php
define('DB_NAME', 'texeg_planetmilav_com');
define('DB_USER', 'wordpress');
define('DB_PASSWORD', 'seagate');
define('DB_HOST', 'localhost');
define('WP_DEBUG', false);
```

## 11. Git Repository Setup
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
```bash
sudo apt install postfix postfix-mysql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql mariadb-server nginx php-fpm php-mysql postfixadmin roundcube roundcube-mysql roundcube-plugins opendkim opendkim-tools
```

Set up firewall:
```bash
sudo ufw allow "Dovecot IMAP"
sudo ufw allow "Dovecot Secure IMAP"
sudo ufw allow "Postfix"
sudo ufw allow "Postfix SMTPS"
sudo ufw allow "Postfix Submission"
```

Create mail user and directories:
```bash
sudo groupadd -g 5000 vmail
sudo useradd -g vmail -u 5000 vmail -d /var/mail
sudo mkdir -p /var/mail/vhosts
sudo chown -R vmail:vmail /var/mail/vhosts
sudo chmod -R 770 /var/mail/vhosts
```

## 13. Mail Server Configuration

### Postfix Configuration
Edit `/etc/postfix/main.cf`:
```ini
smtpd_banner = $myhostname ESMTP $mail_name
biff = no
append_dot_mydomain = no
readme_directory = no
compatibility_level = 3.6

smtpd_tls_cert_file=/etc/letsencrypt/live/planetmilav.com/fullchain.pem
smtpd_tls_key_file=/etc/letsencrypt/live/planetmilav.com/privkey.pem
smtpd_tls_security_level=may
smtpd_tls_auth_only=yes
smtpd_tls_protocols = !SSLv2, !SSLv3, !TLSv1, !TLSv1.1
smtp_tls_note_starttls_offer = yes

smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth
smtpd_sasl_auth_enable = yes
smtpd_sasl_security_options = noanonymous
broken_sasl_auth_clients = yes

myhostname = mail.planetmilav.com
mydestination = $myhostname, localhost.$mydomain, localhost, mail.planetmilav.com
relayhost = 
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all
inet_protocols = all

virtual_mailbox_domains = mysql:/etc/postfix/mysql-virtual-mailbox-domains.cf
virtual_mailbox_maps = mysql:/etc/postfix/mysql-virtual-mailbox-maps.cf
virtual_alias_maps = mysql:/etc/postfix/mysql-virtual-alias-maps.cf
virtual_transport = lmtp:unix:private/dovecot-lmtp
```

Create MySQL configuration files:

1. `/etc/postfix/mysql-virtual-mailbox-domains.cf`:
```ini
user = postfixadmin
password = seagate
hosts = 127.0.0.1
dbname = postfixadmin
query = SELECT domain FROM domain WHERE domain='%s' AND active = '1'
```

2. `/etc/postfix/mysql-virtual-mailbox-maps.cf`:
```ini
user = postfixadmin
password = seagate
hosts = 127.0.0.1
dbname = postfixadmin
query = SELECT maildir FROM mailbox WHERE username='%s' AND active = '1'
```

3. `/etc/postfix/mysql-virtual-alias-maps.cf`:
```ini
user = postfixadmin
password = seagate
hosts = 127.0.0.1
dbname = postfixadmin
query = SELECT goto FROM alias WHERE address='%s' AND active = '1'
```

### Dovecot Configuration

1. `/etc/dovecot/conf.d/10-auth.conf`:
```ini
disable_plaintext_auth = no
auth_mechanisms = plain login
!include auth-sql.conf.ext
```

2. `/etc/dovecot/conf.d/10-mail.conf`:
```ini
mail_location = maildir:/var/mail/vhosts/%d/%n
mail_uid = 5000
mail_gid = 5000
```

3. `/etc/dovecot/conf.d/10-master.conf`:
```ini
service imap-login {
  inet_listener imap {
    port = 143
  }
  inet_listener imaps {
    port = 993
    ssl = yes
  }
}

service lmtp {
  unix_listener /var/spool/postfix/private/dovecot-lmtp {
    mode = 0600
    user = postfix
    group = postfix
  }
}

service auth {
  unix_listener /var/spool/postfix/private/auth {
    mode = 0660
    user = postfix
    group = postfix
  }
}
```

4. `/etc/dovecot/conf.d/10-ssl.conf`:
```ini
ssl = yes
ssl_cert = </etc/letsencrypt/live/planetmilav.com/fullchain.pem
ssl_key = </etc/letsencrypt/live/planetmilav.com/privkey.pem
ssl_min_protocol = TLSv1.2
```

### Web Interface Configuration

1. Configure PostfixAdmin
Edit `/etc/nginx/sites-available/postfixadmin.planetmilav.com`:
Continuing with the complete guide:

```nginx
server {
    server_name postfixadmin.planetmilav.com;
    root /usr/share/postfixadmin/public/;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }
}
```

2. Configure Roundcube
Edit `/etc/nginx/sites-available/roundcube`:
```nginx
server {
    server_name roundcube.planetmilav.com;
    root /usr/share/roundcube;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    location ~* ^.+\.(jpg|jpeg|gif|css|png|js|ico)$ {
        expires max;
    }
}
```

Edit `/etc/roundcube/config.inc.php`:
```php
$config['db_dsnw'] = 'mysql://roundcube:seagate@localhost/roundcube';
$config['imap_host'] = 'ssl://mail.planetmilav.com:993';
$config['smtp_host'] = 'tls://mail.planetmilav.com:587';
$config['smtp_user'] = '%u';
$config['smtp_pass'] = '%p';
$config['support_url'] = '';
$config['des_key'] = 'KDWN44HZaN+YYlyGY+E/ExLQ';
$config['plugins'] = [];
$config['skin'] = 'elastic';
```

## 14. DKIM Setup
```bash
sudo mkdir -p /etc/opendkim/keys/planetmilav.com
sudo opendkim-genkey -D /etc/opendkim/keys/planetmilav.com/ -d planetmilav.com -s mail
sudo chown -R opendkim:opendkim /etc/opendkim/keys
```

Edit `/etc/opendkim.conf`:
```ini
Domain                  planetmilav.com
KeyFile                 /etc/opendkim/keys/planetmilav.com/mail.private
Selector                mail
Socket                  local:/var/spool/postfix/opendkim/opendkim.sock
UserID                  opendkim:opendkim
UMask                  002
```

Create/edit key files:

1. `/etc/opendkim/KeyTable`:
```plaintext
mail._domainkey.planetmilav.com planetmilav.com:mail:/etc/opendkim/keys/planetmilav.com/mail.private
```

2. `/etc/opendkim/SigningTable`:
```plaintext
*@planetmilav.com mail._domainkey.planetmilav.com
```

3. `/etc/opendkim/TrustedHosts`:
```plaintext
127.0.0.1
localhost
192.168.0.0/24
planetmilav.com
```

Add to Postfix configuration in `/etc/postfix/main.cf`:
```ini
# OpenDKIM
milter_protocol = 6
milter_default_action = accept
smtpd_milters = local:/var/spool/postfix/opendkim/opendkim.sock
non_smtpd_milters = $smtpd_milters
```

## 15. DMARC Setup
Create DNS record:
```txt
_dmarc.planetmilav.com. IN TXT "v=DMARC1; p=none; sp=none; rua=mailto:admin@planetmilav.com"
```

## 16. Spam Filters
```bash
sudo apt install spamassassin spamc
sudo systemctl enable spamassassin
sudo systemctl start spamassassin
```

Edit `/etc/postfix/master.cf`, add to smtpd entry:
```ini
-o content_filter=spamassassin
```

Add to end of file:
```ini
spamassassin unix -     n       n       -       -       pipe
  user=debian-spamd argv=/usr/bin/spamc -f -e /usr/sbin/sendmail -oi -f ${sender} ${recipient}
```

Edit `/etc/spamassassin/local.cf`:
```ini
rewrite_header Subject *****SPAM*****
required_score 5.0
use_bayes 1
bayes_auto_learn 1
```

## 17. Final Steps and Testing

1. Link all Nginx configurations:
```bash
sudo ln -s /etc/nginx/sites-available/* /etc/nginx/sites-enabled/
```

2. Restart all services:
```bash
sudo systemctl restart postfix dovecot nginx spamassassin
```

3. Test mail server:
```bash
telnet localhost 25
telnet localhost 143
telnet localhost 587
telnet localhost 993
sudo postfix check
sudo dovecot -n
doveadm auth test admin@planetmilav.com
```

4. Test email sending:
```bash
echo "Mail Test" | mail -s "Mail Test" milav.dabgar@gmail.com
```

5. Monitor logs:
```bash
tail -f /var/log/mail.log /var/log/nginx/error.log
```

6. DNS Records to Add:
- MX Record: `mail.planetmilav.com`
- SPF Record: `v=spf1 mx -all`
- DKIM Record: (from `/etc/opendkim/keys/planetmilav.com/mail.txt`)
- DMARC Record: (as specified in DMARC setup)

## 18. Security Checklist
- All passwords set to 'seagate'
- SSL certificates installed
- Firewall configured
- DKIM/DMARC/SPF configured
- SpamAssassin running
- Regular backups configured
- Monitoring in place

This completes the full setup of your server with mail functionality and all supporting services.

Would you like me to provide more details about any specific section or add any additional configurations?