

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

```bash
  233  sudo timedatectl set-timezone Asia/Kolkata
    1  sudo nano /etc/netplan/50-cloud-init.yaml 
    2  sudo netplan apply 
    3  ip a
   89  sudo apt install openssh-server
   70  ssh-keygen
   71  sudo ufw allow OpenSSH
   72  sudo ufw status
  105  sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
  112  sudo hostnamectl set-hostname rpi
  116  sudo nano /etc/hosts
  117  sudo apt install nginx -y
  118  sudo systemctl start nginx
  119  sudo systemctl enable nginx
  120  sudo apt install mariadb-server mariadb-client -y
  121  sudo mysql_secure_installation
  122  sudo mysql -u root -p
  123  sudo apt install php-fpm php-mysql php-curl php-gd php-xml php-mbstring php-dom php-imagick php-zip php-intl -y
  124  sudo mysql -e "CREATE DATABASE planetmilav_com;"
  125  sudo mysql -u root -p
  126  sudo mysql -e "CREATE DATABASE texeg_planetmilav_com;"
  127  sudo mysql -e "CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'seagate';"
  128  sudo mysql -e "GRANT ALL PRIVILEGES ON planetmilav_com.* TO 'wordpress'@'localhost';"
  129  sudo mysql -e "GRANT ALL PRIVILEGES ON texeg_planetmilav_com.* TO 'wordpress'@'localhost';"
  130  sudo mysql -e "FLUSH PRIVILEGES;"
  147  sudo nano /etc/nginx/sites-available/default  
  131  sudo nano /etc/nginx/sites-available/planetmilav
  132  sudo nano /etc/nginx/sites-available/portfolio.planetmilav.com
  133  sudo nano /etc/nginx/sites-available/texeg.planetmilav.com
  134  sudo nano /etc/nginx/sites-available/postfixadmin.planetmilav.com
  135  sudo nano /etc/nginx/sites-available/roundcube
  136  sudo nano /etc/nginx/sites-available/nextcloud
  137  sudo nano /etc/nginx/sites-available/gpplmsv1.planetmilav.com
  138  sudo cp /etc/nginx/sites-available/planetmilav /etc/nginx/sites-available/planetmilav.com
  139  sudo rm /etc/nginx/sites-available/planetmilav
  140  sudo ln -s /etc/nginx/sites-available/gpplmsv1.planetmilav.com /etc/nginx/sites-enabled/
  141  sudo ln -s /etc/nginx/sites-available/planetmilav.com /etc/nginx/sites-enabled/
  142  sudo ln -s /etc/nginx/sites-available/texeg.planetmilav.com /etc/nginx/sites-enabled/
  143  sudo ln -s /etc/nginx/sites-available/portfolio.planetmilav.com /etc/nginx/sites-enabled/
  144  sudo ln -s /etc/nginx/sites-available/postfixadmin.planetmilav.com /etc/nginx/sites-enabled/
  145  sudo ln -s /etc/nginx/sites-available/roundcube /etc/nginx/sites-enabled/
  146  sudo ln -s /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/
  148  sudo nginx -t
  154  sudo apt install python3-certbot-nginx
  156  sudo certbot --nginx -d planetmilav.com -d www.planetmilav.com -d gpplmsv1.planetmilav.com -d mail.planetmilav.com -d portfolio.planetmilav.com -d postfixadmin.planetmilav.com -d texeg.planetmilav.com -d roundcube.planetmilav.com -d nextcloud.planetmilav.com
  168  sudo systemctl restart nginx
  174  sudo ufw allow "Nginx Full"
  181  sudo crontab -e
  182  crontab -e
  184  sudo wget https://wordpress.org/latest.tar.gz
  185  sudo tar -xzvf latest.tar.gz
  187  sudo cp wordpress /var/www/texeg.planetmilav.com -r
  190  sudo cp wordpress /var/www/planetmilav.com -r
  192  sudo rm -rf wordpress/
  193  sudo rm latest.tar.gz
  196  sudo chown -R www-data:www-data /var/www/planetmilav.com/
  197  sudo chown -R www-data:www-data /var/www/texeg.planetmilav.com/
  198  sudo chmod -R 755 /var/www/planetmilav.com/
  199  sudo chmod -R 755 /var/www/texeg.planetmilav.com/
  203  mkdir code
  205  cd code
  212  git config --global user.name "Milav Dabgar"
  213  git config --global user.email "milav.dabgar@gmail.com"
  215  ssh-keygen -t ed25519 -C "milav.dabgar@gmail.com"
  216  cat ~/.ssh/id_ed25519.pub  
  217  git clone git@github.com:milavdabgar/ipEmail.git
  218  git clone https://github.com/milavdabgar/milavdabgar.github.io.git
  221  git clone git@github.com:milavdabgar/gppLMSv1.git
  251  sudo apt install postfix postfix-mysql dovecot-core dovecot-imapd dovecot-lmtpd dovecot-mysql mariadb-server nginx php-fpm php-mysql postfixadmin roundcube roundcube-mysql roundcube-plugins opendkim opendkim-tools
  252  sudo ufw app list
  253  sudo ufw allow "Dovecot IMAP"
  254  sudo ufw allow "Dovecot Secure IMAP"
  255  sudo ufw allow "Postfix"
  256  sudo ufw allow "Postfix SMTPS"
  257  sudo ufw allow "Postfix Submission"  
  285  sudo postfix check
  286  sudo dovecot -n
  306  doveadm auth test admin@planetmilav.com
  307  sudo groupadd -g 5000 vmail
  308  sudo useradd -g vmail -u 5000 vmail -d /var/mail
  309  sudo mkdir -p /var/mail/vhosts
  310  sudo chown -R vmail:vmail /var/mail/vhosts
  311  sudo chmod -R 770 /var/mail/vhosts
  314  telnet localhost 25
  319  telnet localhost 143
  433  telnet localhost 587
  434  telnet localhost 993
  347  sudo mkdir -p /etc/opendkim/keys/planetmilav.com
  348  cd /etc/opendkim/keys/planetmilav.com
  349  sudo opendkim-genkey -b 2048 -d planetmilav.com -D /etc/opendkim/keys/planetmilav.com -s mail -v
  350  sudo chown -R opendkim:opendkim /etc/opendkim/keys
  351  sudo chmod 600 /etc/opendkim/keys/planetmilav.com/mail.private
  352  sudo nano /etc/opendkim.conf
  353  sudo nano /etc/opendkim/KeyTable
  354  sudo nano /etc/opendkim/SigningTable
  355  sudo nano /etc/opendkim/TrustedHosts
  356  sudo cat /etc/opendkim/keys/planetmilav.com/mail.txt
  357  sudo nano /etc/opendkim/keys/planetmilav.com/mail.txt
  358  sudo mkdir -p /var/spool/postfix/opendkim
  359  sudo chown opendkim:postfix /var/spool/postfix/opendkim
  360  sudo systemctl restart opendkim postfix
  361  sudo opendkim-testkey -d planetmilav.com -s mail -vvv
  362  sudo nano /etc/postfix/main.cf  
  365  sudo apt install mailutils
  366  echo "DKIM Test" | mail -s "DKIM Test" milav.dabgar@gmail.com  
```

