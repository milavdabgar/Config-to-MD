

Mail Server Setup Guide

```bash
sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y && sudo snap refresh
sudo hostnamectl set-hostname rpi
sudo timedatectl set-timezone Asia/Kolkata
sudo adduser milav
sudo usermod -aG sudo milav
sudo apt install openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh
sudo ufw allow ssh
sudo ufw allow "OpenSSH"
sudo ufw enable
sudo ufw status
```

Basic Setup of Ubuntu Server

```bash
sudo nano /etc/netplan/50-cloud-init.yaml
```

```yaml
network:
    ethernets:
        eth0:
            dhcp4: no
            optional: true
            addresses:
              - 192.168.0.50/24
            routes:
              - to: default
                via: 192.168.0.1
            nameservers:
              addresses: [192.168.0.1, 8.8.8.8]
    version: 2
    wifis:
      wlan0:
        dhcp4: true
        optional: true
        addresses:
          - 192.168.0.51/24
        nameservers:
          addresses: [192.168.0.1, 8.8.8.8]
        access-points:
          "Milav-Tenda":
            password: "seagate@123"
```

```bash
sudo netplan apply
ip a
```

```bash
ssh-keygen -t ed25519 -C "milav.dabgar@gmail.com"
cat ~/.ssh/id_ed25519.pub
mkdir code
cd code
git clone git@github.com:milavdabgar/ipEmail.git
git clone git@github.com:milavdabgar/gppLMSv1.git
sudo cp milavdabgar.github.io /var/www/portfolio.planetmilav.com -r
```

```bash
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo ufw allow "Nginx Full"
sudo apt install php-fpm php-mysql php-curl php-gd php-xml php-mbstring php-dom php-imagick php-zip php-intl -y
```

```bash
sudo nano /etc/nginx/sites-available/planetmilav.com 
sudo nano /etc/nginx/sites-available/texeg.planetmilav.com
sudo nano /etc/nginx/sites-available/portfolio.planetmilav.com
sudo nano /etc/nginx/sites-available/postfixadmin.planetmilav.com
sudo nano /etc/nginx/sites-available/roundcube 
sudo nano /etc/nginx/sites-available/nextcloud
```

```nginx
# /etc/nginx/sites-available/planetmilav.com
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

```nginx
# /etc/nginx/sites-available/texeg.planetmilav.com
server {
    server_name texeg.planetmilav.com;
    root /var/www/texeg.planetmilav.com;
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

    gzip on;
    gzip_types text/plain text/xml text/css application/javascript;
}
```

```nginx
# /etc/nginx/sites-available/portfolio.planetmilav.com
server {
    server_name portfolio.planetmilav.com;
    root /var/www/portfolio.planetmilav.com;
    index index.html index.htm index.php;
    location / {
        try_files $uri $uri/ =404;
    }
}
```

```nginx
# /etc/nginx/sites-available/postfixadmin.planetmilav.com
server {
    server_name postfixadmin.planetmilav.com;
    root /usr/share/postfixadmin/public/;
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

```nginx
# /etc/nginx/sites-available/roundcube
server {
    server_name roundcube.planetmilav.com;
    root /usr/share/roundcube;
    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_intercept_errors on;
        fastcgi_pass php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    location ~* ^.+\.(jpeg|jpg|png|gif|bmp|ico|svg|css|js)$ {
        expires max;
    }

    location ~ /\.ht {
        deny all;
    }
}

```

```nginx
# /etc/nginx/sites-available/nextcloud
server {
    server_name nextcloud.planetmilav.com;
    root /usr/share/nextcloud;
    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_intercept_errors on;
        fastcgi_pass php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    location ~* ^.+\.(jpeg|jpg|png|gif|bmp|ico|svg|css|js)$ {
        expires max;
    }

    location ~ /\.ht {
        deny all;
    }
}

```

```bash
sudo ln -s /etc/nginx/sites-available/gpplmsv1.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/texeg.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/portfolio.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/postfixadmin.planetmilav.com /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/roundcube /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/
```

```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d planetmilav.com -d www.planetmilav.com -d gpplmsv1.planetmilav.com -d mail.planetmilav.com -d portfolio.planetmilav.com -d postfixadmin.planetmilav.com -d texeg.planetmilav.com -d roundcube.planetmilav.com -d nextcloud.planetmilav.com
```

```bash
sudo crontab -e
# 0 */12 * * * certbot renew --nginx --quiet
crontab -e
# */1 * * * * /usr/bin/python /home/milav/code/ipEmail/cloudflare-dns-update-api.py >/dev/null 2>&1
```

```bash
sudo apt install mariadb-server mariadb-client -y
sudo mysql_secure_installation
sudo mysql -u root -p
sudo mysql -e "CREATE DATABASE planetmilav_com;"
sudo mysql -e "CREATE DATABASE texeg_planetmilav_com;"
sudo mysql -e "CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'seagate';"
sudo mysql -e "GRANT ALL PRIVILEGES ON planetmilav_com.* TO 'wordpress'@'localhost';"
sudo mysql -e "GRANT ALL PRIVILEGES ON texeg_planetmilav_com.* TO 'wordpress'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"
```

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

```bash
sudo apt install mailutils
sudo apt install maildirmake
sudo apt install maildrop
sudo maildirmake /home/milav/Maildir
sudo chown -R $USER:$USER /home/$USER/Maildir
sudo nano /etc/postfix/main.cf
sudo nano /etc/dovecot/dovecot.conf
sudo nano /etc/dovecot/conf.d/10-ssl.conf
sudo systemctl restart postfix
sudo systemctl restart dovecot
sudo nano /etc/dovecot/conf.d/10-auth.conf
sudo certbot certonly --standalone -d mail.planetmilav.com
sudo cat /var/log/mail.log
sudo apt install dovecot-core dovecot-imapd dovecot-pop3d
sudo apt remove --purge postfixadmin postfix postfix-mysql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql spamassassin spamc fail2ban
docker run -d -p 8000:8000 gpp-lms-v1
sudo nano /etc/php/8.3/fpm/pool.d/www.conf
```

```bash
sudo ufw app list
sudo ufw allow "Dovecot IMAP"
sudo ufw allow "Dovecot POP3"
sudo ufw allow "Dovecot Secure IMAP"
sudo ufw allow "Dovecot Secure POP3"
sudo ufw allow "Nginx HTTP"
sudo ufw allow "Nginx HTTPS"
sudo ufw allow "Postfix"
sudo ufw allow "Postfix SMTPS"
sudo ufw allow "Postfix Submission"
```

```bash
# sudo nano /etc/postfix/main.cf

# See /usr/share/postfix/main.cf.dist for a commented, more complete version
smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
biff = no
append_dot_mydomain = no
readme_directory = no
compatibility_level = 3.6

myhostname = mail.planetmilav.com
mydomain = planetmilav.com
myorigin = $mydomain
home_mailbox = Maildir/

# TLS parameters
smtpd_tls_cert_file=/etc/letsencrypt/live/mail.planetmilav.com/fullchain.pem
smtpd_tls_key_file=/etc/letsencrypt/live/mail.planetmilav.com/privkey.pem
smtpd_tls_security_level=may
#smtpd_tls_security_level = encrypt

smtp_tls_CApath=/etc/ssl/certs
smtp_tls_security_level=may
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
#mydestination = $myhostname, planetmilav.com, localhost.localdomain, localhost
mydestination = $myhostname, localhost.localdomain, localhost
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all
inet_protocols = all

# SMTP server
# Uncomment and configure if using an external SMTP server
#relayhost = [smtp.yourprovider.com]:587

# Configure for authentication if using an external SMTP server
#smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
#smtpd_sasl_security_options = noanonymous
#smtpd_sasl_local_domain = $myhostname

smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth
smtpd_sasl_auth_enable = yes
smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination

milter_protocol = 6
milter_default_action = accept
smtpd_milters = unix:/var/spool/postfix/opendkim/opendkim.sock
non_smtpd_milters = $smtpd_milters

virtual_mailbox_domains = mysql:/etc/postfix/mysql-virtual-mailbox-domains.cf
virtual_mailbox_maps = mysql:/etc/postfix/mysql-virtual-mailbox-maps.cf
virtual_alias_maps = mysql:/etc/postfix/mysql-virtual-alias-maps.cf
virtual_transport = lmtp:unix:private/dovecot-lmtp
cyrus_sasl_config_path = /etc/postfix/sasl
```

```bash
# sudo nano /etc/dovecot/dovecot.conf

# Enable installed protocols
!include_try /usr/share/dovecot/protocols.d/*.protocol

# Dictionary can be used to store key=value lists. This is used by several
# plugins. The dictionary can be accessed either directly or though a
# dictionary server. The following dict block maps dictionary names to URIs
# when the server is used. These can then be referenced using URIs in format
# "proxy::<name>".

dict {
  #quota = mysql:/etc/dovecot/dovecot-dict-sql.conf.ext
}

# Most of the actual configuration gets included below. The filenames are
# first sorted by their ASCII value and parsed in that order. The 00-prefixes
# in filenames are intended to make it easier to understand the ordering.
!include conf.d/*.conf

# A config file can also tried to be included without giving an error if
# it's not found:
!include_try local.conf

```

```bash
# sudo nano /etc/dovecot/conf.d/10-ssl.conf

# SSL/TLS support: yes, no, required. <doc/wiki/SSL.txt>
ssl = yes

# Directory and/or file for trusted SSL CA certificates. These are used only
# when Dovecot needs to act as an SSL client (e.g. imapc backend or
# submission service). The directory is usually /etc/ssl/certs in
# Debian-based systems and the file is /etc/pki/tls/cert.pem in
# RedHat-based systems. Note that ssl_client_ca_file isn't recommended with
# large CA bundles, because it leads to excessive memory usage.
#ssl_client_ca_dir =
ssl_client_ca_dir = /etc/ssl/certs
#ssl_client_ca_file =

# SSL DH parameters
# Generate new params with `openssl dhparam -out /etc/dovecot/dh.pem 4096`
# Or migrate from old ssl-parameters.dat file with the command dovecot
# gives on startup when ssl_dh is unset.
ssl_dh = </usr/share/dovecot/dh.pem

```

```bash
# /etc/dovecot/conf.d/10-master.conf

service imap-login {
  inet_listener imap {
    port = 0
  }
  inet_listener imaps {
    port = 993
    ssl = yes
  }
}

service pop3-login {
  inet_listener pop3 {
    #port = 0 # disable plain POP3 by setting the port to 0
  }
  inet_listener pop3s {
    port = 995
    ssl = yes
  }
}


service submission-login {
  inet_listener submission {
    #port = 587
  }
}

service lmtp {
    unix_listener /var/spool/postfix/private/dovecot-lmtp {
        mode = 0600
        user = postfix
        group = postfix
    }
    # If you want to enable LMTP over the network, uncomment the following:
    # inet_listener lmtp {
    #     address = 127.0.0.1
    #     port = 24
    # }
}

service imap {
  # Most of the memory goes to mmap()ing files. You may need to increase this
  # limit if you have huge mailboxes.
  #vsz_limit = $default_vsz_limit

  # Max. number of IMAP processes (connections)
  #process_limit = 1024
}

service pop3 {
  # Max. number of POP3 processes (connections)
  #process_limit = 1024
}

service submission {
  # Max. number of SMTP Submission processes (connections)
  #process_limit = 1024
}

service auth {
  unix_listener /var/spool/postfix/private/auth {
    mode = 0660
    user = postfix
    group = postfix
  }
}

service auth-worker {
  # Auth worker process is run as root by default, so that it can access
  # /etc/shadow. If this isn't necessary, the user should be changed to
  # $default_internal_user.
  #user = root
}

service dict {
  # If dict proxy is used, mail processes should have access to its socket.
  # For example: mode=0660, group=vmail and global mail_access_groups=vmail
  unix_listener dict {
    #mode = 0600
    #user = 
    #group = 
  }
}
```

```php
# /etc/postfixadmin/dbconfig.inc.php

<?php
##
## database access settings in php format
## automatically generated from /etc/dbconfig-common/postfixadmin.conf
## by /usr/sbin/dbconfig-generate-include
##
## by default this file is managed via ucf, so you shouldn't have to
## worry about manual changes being silently discarded.  *however*,
## you'll probably also want to edit the configuration file mentioned
## above too.
##
$dbuser='postfixadmin';
$dbpass='seagate';
$basepath='';
$dbname='postfixadmin';
$dbserver='localhost';
$dbport='3306';
$dbtype='mysql';
```

```php
# sudo nano /etc/postfixadmin/config.inc.php

$CONF['setup_password'] = '$2y$10$ElGy2wIPcwTul3Ct2ejwzuPi/OGxzBJE2dDzwH8s5xhe5ETx.Oy7u';

// Database Config
// mysql = MySQL 3.23 and 4.0, 4.1 or 5
// mysqli = MySQL 4.1+ or MariaDB
// pgsql = PostgreSQL
// sqlite = SQLite 3
$CONF['database_type'] = $dbtype;
$CONF['database_host'] = $dbserver;
$CONF['database_user'] = $dbuser;
$CONF['database_password'] = $dbpass;
$CONF['database_name'] = $dbname;

// Database SSL Config (PDO/MySQLi only)
$CONF['database_use_ssl'] = false;
$CONF['database_ssl_key'] = NULL;
$CONF['database_ssl_cert'] = NULL;
$CONF['database_ssl_ca'] = NULL;
$CONF['database_ssl_ca_path'] = NULL;
$CONF['database_ssl_cipher'] = NULL;
$CONF['database_ssl_verify_server_cert'] = true;

// Site Admin
// Define the Site Admin's email address below.
// This will be used to send emails from to create mailboxes and
// from Send Email / Broadcast message pages.
// Leave blank to send email from the logged-in Admin's Email address.
$CONF['admin_email'] = '';

// Define the smtp password for admin_email.
// This will be used to send emails from to create mailboxes and
// from Send Email / Broadcast message pages.
// Leave blank to send emails without authentification
$CONF['admin_smtp_password'] = '';

// Site admin name
// This will be used as signature in notification messages
$CONF['admin_name'] = 'Postmaster';

// Mail Server
// Hostname (FQDN) of your mail server.
// This is used to send email to Postfix in order to create mailboxes.
$CONF['smtp_server'] = 'localhost';
$CONF['smtp_port'] = '25';

// SMTP Client
// Hostname (FQDN) of the server hosting Postfix Admin
// Used in the HELO when sending emails from Postfix Admin
$CONF['smtp_client'] = '';

// Set 'YES' to use TLS when sending emails.
$CONF['smtp_sendmail_tls'] = 'NO';

```

```bash
# sudo nano /etc/postfix/mysql-virtual-mailbox-domains.cf
user = postfixadmin
password = seagate
hosts = 127.0.0.1
dbname = postfixadmin
query = SELECT domain FROM domain WHERE domain='%s' AND active = '1'
```

```bash
# sudo nano /etc/postfix/mysql-virtual-mailbox-maps.cf
user = postfixadmin
password = seagate
hosts = 127.0.0.1
dbname = postfixadmin
query = SELECT maildir FROM mailbox WHERE username='%s' AND active = '1'
```

```bash
# sudo nano /etc/postfix/mysql-virtual-alias-maps.cf
user = postfixadmin
password = seagate
hosts = 127.0.0.1
dbname = postfixadmin
query = SELECT goto FROM alias WHERE address='%s' AND active = '1'
```

```bash
# /etc/dovecot/conf.d/auth-sql.conf.ext

passdb {
  driver = sql

  # Path for SQL configuration file, see example-config/dovecot-sql.conf.ext
  args = /etc/dovecot/dovecot-sql.conf.ext
}

userdb {
  driver = sql
  args = /etc/dovecot/dovecot-sql.conf.ext
}
```

```bash
# sudo nano /etc/dovecot/dovecot-sql.conf.ext
driver = mysql
connect = host=127.0.0.1 dbname=postfixadmin user=postfixadmin password=seagate
default_pass_scheme = SHA256-CRYPT
password_query = SELECT username as user, password FROM mailbox WHERE username='%u' AND active = '1';
user_query = SELECT concat('/var/mail/vhosts/', domain, '/', local_part, '/') as home, 5000 as uid, 5000 as gid FROM mailbox WHERE username = '%u' AND active='1';
```

```bash
# sudo nano /etc/dovecot/conf.d/10-mail.conf

mail_location = maildir:/var/mail/vhosts/%d/%n
mail_uid = 5000
mail_gid = 5000
```

```bash
# sudo nano /etc/dovecot/conf.d/10-auth.conf

# Disable LOGIN command and all other plaintext authentications unless
# SSL/TLS is used (LOGINDISABLED capability). Note that if the remote IP
# matches the local IP (ie. you're connecting from the same computer), the
# connection is considered secure and plaintext authentication is allowed.
# See also ssl=required setting.
#disable_plaintext_auth = yes
disable_plaintext_auth = no


# Space separated list of wanted authentication mechanisms:
#   plain login digest-md5 cram-md5 ntlm rpa apop anonymous gssapi otp
#   gss-spnego
# NOTE: See also disable_plaintext_auth setting.
#auth_mechanisms = plain
auth_mechanisms = plain login


##
## Password and user databases
##

#
# Password database is used to verify user's password (and nothing more).
# You can have multiple passdbs and userdbs. This is useful if you want to
# allow both system users (/etc/passwd) and virtual users to login without
# duplicating the system users into virtual database.
#
# <doc/wiki/PasswordDatabase.txt>
#
# User database specifies where mails are located and what user/group IDs
# own them. For single-UID configuration use "static" userdb.
#
# <doc/wiki/UserDatabase.txt>

#!include auth-deny.conf.ext
#!include auth-master.conf.ext

#!include auth-system.conf.ext
!include auth-sql.conf.ext
#!include auth-ldap.conf.ext
#!include auth-passwdfile.conf.ext
#!include auth-checkpassword.conf.ext
#!include auth-static.conf.ext
```

```bash
# sudo nano /etc/dovecot/conf.d/auth-master.conf.ext

# Example master user passdb using passwd-file. You can use any passdb though.
passdb {
  driver = passwd-file
  master = yes
  args = /etc/dovecot/master-users

  # Unless you're using PAM, you probably still want the destination user to
  # be looked up from passdb that it really exists. pass=yes does that.
  pass = yes
}
```

```bash
# sudo nano /etc/dovecot/conf.d/auth-system.conf.ext

passdb {
  driver = pam
  # [session=yes] [setcred=yes] [failure_show_msg=yes] [max_requests=<n>]
  # [cache_key=<key>] [<service name>]
  #args = dovecot
}

# System users (NSS, /etc/passwd, or similar). In many systems nowadays this
# uses Name Service Switch, which is configured in /etc/nsswitch.conf.
userdb {
  # <doc/wiki/AuthDatabase.Passwd.txt>
  driver = passwd
  # [blocking=no]
  #args = 

  # Override fields from passwd
  #override_fields = home=/home/virtual/%u
}
```



```bash
  935  sudo apt install postfix postfix-mysql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql mariadb-server php-fpm php-mysql
  936  mysql -u root -p
  937  sudo apt install postfixadmin 
  938  sudo nano /etc/postfixadmin/dbconfig.inc.php
  939  sudo nano /etc/postfixadmin/config.inc.php 
  941  mysql -u root -p
  943  sudo nano /etc/nginx/sites-available/postfixadmin.planetmilav.com
  949  sudo systemctl restart opendkim postfix nginx
  951  sudo nano /etc/postfix/main.cf
  952  sudo nano /etc/postfix/mysql-virtual-mailbox-domains.cf
  953  sudo nano /etc/postfix/mysql-virtual-mailbox-maps.cf
  954  sudo nano /etc/postfix/mysql-virtual-alias-maps.cf
  955  sudo nano /etc/dovecot/conf.d/auth-sql.conf.ext
  956  sudo nano /etc/dovecot/dovecot-sql.conf.ext
  957  sudo nano /etc/dovecot/conf.d/10-mail.conf
  958  sudo mkdir -p /var/mail/vhosts/planetmilav.com
  959  sudo chown -R vmail:vmail /var/mail/vhosts
  960  sudo groupadd -g 5000 vmail
  961  sudo useradd -m -d /var/mail/vhosts -s /usr/sbin/nologin -u 5000 -g vmail vmail
  962  sudo chown -R vmail:vmail /var/mail/vhosts
  963  sudo nano /etc/dovecot/conf.d/10-mail.conf
  964  sudo nano /etc/dovecot/conf.d/10-auth.conf 
  966  sudo nano /etc/dovecot/dovecot-sql.conf.ext
  967  sudo nano /etc/dovecot/conf.d/auth-sql.conf.ext
  969  sudo groupadd -g 5000 vmail
  970  sudo useradd -m -d /var/mail/vhosts -s /usr/sbin/nologin -u 5000 -g vmail vmail
  971  sudo systemctl restart opendkim postfix nginx postfixadmin dovecot
  974  sudo nano /etc/opendkim/KeyTable 
  975  sudo cat /etc/opendkim/KeyTable 
  976  sudo cat /etc/opendkim/SigningTable 
  977  sudo cat /etc/opendkim/TrustedHosts 
  978  sudo opendkim-testkey -d planetmilav.com -s mail -vvv
  988  id vmail
  989  sudo chown -R vmail:vmail /var/mail/vhosts
  990  sudo chmod -R 770 /var/mail/vhosts
  995  sudo chown -R vmail:vmail /var/mail/vhosts
  996  sudo find /var/mail/vhosts -type d -exec chmod 770 {} \;
 1009  sudo doveconf | grep userdb
```

```bash
 1021  sudo groupadd vmail 
 1022  sudo useradd -g vmail vmail
 1023  sudo usermod -d /var/mail vmail
 1024  sudo chown vmail:vmail /var/mail
 1025  sudo systemctl restart postfix dovecot
 1026  sudo journalctl -u dovecot | tail
 1027  sudo systemctl status postfix dovecot
 1028  sudo doveconf | grep userdb
 1029  sudo journalctl -u dovecot
 1030  sudo chown -R vmail:vmail /var/mail/vhosts
 1031  sudo chmod -R 775 /var/mail/vhosts
 1032  sudo nano /etc/dovecot/conf.d/10-mail.conf
 1033  sudo nano /etc/dovecot/dovecot-sql.conf.ext
 1034  sudo nano /etc/dovecot/conf.d/10-auth.conf
 1035  sudo nano /etc/dovecot/conf.d/auth-master.conf.ext 
 1037  sudo doveconf | grep mail_
 1038  sudo doveconf | grep userdb
 1039  sudo journalctl -u dovecot
 1040  sudo nano /etc/dovecot/conf.d/10-mail.conf
 1041  sudo journalctl -u dovecot
 1044  sudo ls -al /var/mail/vhosts/planetmilav.com/
 1046  echo "This is a test message" | mail -s "Test Subject" user1@planetmilav.com
 1048  sudo apt-get install roundcube
 1049  sudo apt install roundcube roundcube-mysql roundcube-plugins
 1052  sudo nano /etc/nginx/sites-available/roundcube
 1070  sudo nano /etc/postfix/main.cf
 1071  sudo nano /etc/postfix/mysql-virtual-mailbox-domains.cf
 1072  sudo nano /etc/postfix/main.cf
 1074  sudo nano /etc/postfix/main.cf
 1076  doveadm auth test user1@planetmilav.com
 1085  sudo nano /etc/dovecot/conf.d/10-mail.conf
 1086  sudo nano /etc/dovecot/conf.d/10-auth.conf 
 1087  sudo nano /etc/dovecot/conf.d/auth-sql.conf.ext
 1088  sudo nano /etc/dovecot/dovecot-sql.conf.ext
 1089  telnet mail.planetmilav.com 993
 1090  openssl s_client -connect mail.planetmilav.com:993
 1092  sudo nano /etc/roundcube/config.inc.php 
 1094  sudo nano /etc/dovecot/conf.d/10-master.conf 
 1095  sudo nano /etc/postfix/main.cf
 1096  sudo ls -l /var/spool/postfix/private/dovecot-lmtp
 1097  sudo doveadm service list
 1099  sudo apt install dovecot-lmtp
 1103  sudo nano /etc/dovecot/conf.d/10-master.conf
 1106  sudo nano /etc/dovecot/conf.d/10-auth.conf 
 1107  sudo nano /etc/dovecot/conf.d/auth-system.conf.ext 
 1111  sudo doveadm service list
 1112  sudo doveadm service status
 1113  sudo doveadm auth test admin@planetmilav.com
 1115  sudo cat /var/log/mail.log
 1116  sudo nano /etc/roundcube/config.inc.php 
```

