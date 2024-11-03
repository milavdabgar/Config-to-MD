# Server Configuration Files

## Web Server (Nginx)
- /etc/nginx/sites-available/default
- /etc/nginx/sites-available/planetmilav.com
- /etc/nginx/sites-available/portfolio.planetmilav.com
- /etc/nginx/sites-available/texeg.planetmilav.com
- /etc/nginx/sites-available/postfixadmin.planetmilav.com
- /etc/nginx/sites-available/roundcube
- /etc/nginx/sites-available/nextcloud
- /etc/nginx/sites-available/gpplmsv1.planetmilav.com

## Mail Server
### Postfix
- /etc/postfix/main.cf
- /etc/postfix/master.cf
- /etc/postfix/mysql-virtual-mailbox-domains.cf
- /etc/postfix/mysql-virtual-mailbox-maps.cf
- /etc/postfix/mysql-virtual-alias-maps.cf

### Dovecot
- /etc/dovecot/dovecot.conf
- /etc/dovecot/conf.d/10-auth.conf
- /etc/dovecot/conf.d/10-mail.conf
- /etc/dovecot/conf.d/10-master.conf
- /etc/dovecot/conf.d/10-ssl.conf
- /etc/dovecot/conf.d/auth-sql.conf.ext
- /etc/dovecot/conf.d/auth-master.conf.ext
- /etc/dovecot/conf.d/auth-system.conf.ext
- /etc/dovecot/dovecot-sql.conf.ext

## Mail Web Interfaces
### Roundcube
- /etc/roundcube/config.inc.php
- /etc/roundcube/debian-db-roundcube.php
- /etc/roundcube/debian-db.php
- /etc/roundcube/apache.conf

### PostfixAdmin
- /etc/postfixadmin/config.inc.php
- /etc/postfixadmin/dbconfig.inc.php
- /etc/postfixadmin/config.local.php

## DKIM Configuration
- /etc/opendkim.conf
- /etc/opendkim/KeyTable
- /etc/opendkim/SigningTable
- /etc/opendkim/TrustedHosts
- /etc/systemd/system/opendkim.service.d/override.conf

## PHP Configuration
- /etc/php/8.3/fpm/pool.d/www.conf

## Network Configuration
- /etc/netplan/50-cloud-init.yaml
- /etc/hosts

## System Configuration
- /etc/systemd/system/opendkim.service.d/override.conf

## Log Files
- /var/log/mail.log
