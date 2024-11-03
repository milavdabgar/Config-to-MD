# Server Configuration Files

## Web Server (Nginx)
- /etc/nginx/sites-available/default
- /etc/nginx/sites-available/planetmilav.com
- /etc/nginx/sites-available/portfolio.planetmilav.com
- /etc/nginx/sites-available/gppec
- /etc/nginx/sites-available/gpplmsv1.planetmilav.com
- /etc/nginx/sites-available/texeg.planetmilav.com
- /etc/nginx/sites-available/roundcube
- /etc/nginx/sites-available/nextcloud
- /etc/nginx/sites-available/postfixadmin.planetmilav.com

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
- /etc/dovecot/conf.d/20-imap.conf
- /etc/dovecot/conf.d/20-lmtp.conf
- /etc/dovecot/conf.d/15-mailboxes.conf
- /etc/dovecot/conf.d/10-director.conf
- /etc/dovecot/dovecot-sql.conf.ext

## PHP Configuration
- /etc/php/8.3/fpm/pool.d/www.conf
- /var/www/html/info.php

## Mail Web Interfaces
### Roundcube
- /etc/roundcube/config.inc.php

### PostfixAdmin
- /etc/postfixadmin/config.inc.php
- /etc/postfixadmin/dbconfig.inc.php

## DKIM Configuration
- /etc/opendkim.conf
- /etc/opendkim/SigningTable
- /etc/opendkim/KeyTable
- /etc/opendkim/TrustedHosts

## File Sharing (Samba)
- /etc/samba/smb.conf

## Network Configuration
- /etc/netplan/00-installer-config.yaml
- /etc/netplan/50-cloud-init.yaml

## System Configuration
- /boot/firmware/config.txt
- /etc/update-manager/release-upgrades
