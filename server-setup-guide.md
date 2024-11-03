# Server Configuration Guide
Generated on: 2024-11-03 01:07:17

## Table of Contents

- [Rsyncd](#rsyncd)
- [Config.Inc](#config.inc)

---

## Rsyncd
Source: `/etc/rsyncd.conf`

```conf
# /etc/rsyncd: configuration file for rsync daemon mode

# See rsyncd.conf man page for more options.

# configuration example:

# uid = nobody
# gid = nobody
# use chroot = yes
# max connections = 4
# pid file = /var/run/rsyncd.pid
# exclude = lost+found/
# transfer logging = yes
# timeout = 900
# ignore nonreadable = yes
# dont compress   = *.gz *.tgz *.zip *.z *.Z *.rpm *.deb *.bz2

# [ftp]
#        path = /home/ftp
#        comment = ftp export area

```

## Config.Inc
Source: `/home/milav/Downloads/config.inc.php`

```php
<?php

/* Local configuration for Roundcube Webmail */

// ----------------------------------
// SQL DATABASE
// ----------------------------------
// Database connection string (DSN) for read+write operations
// Format (compatible with PEAR MDB2): db_provider://user:password@host/database
// Currently supported db_providers: mysql, pgsql, sqlite, mssql, sqlsrv, oracle
// For examples see http://pear.php.net/manual/en/package.database.mdb2.intro-dsn.php
// Note: for SQLite use absolute path (Linux): 'sqlite:////full/path/to/sqlite.db?mode=0646'
//       or (Windows): 'sqlite:///C:/full/path/to/sqlite.db'
// Note: Various drivers support various additional arguments for connection,
//       for Mysql: key, cipher, cert, capath, ca, verify_server_cert,
//       for Postgres: application_name, sslmode, sslcert, sslkey, sslrootcert, sslcrl, sslcompression, service.
//       e.g. 'mysql://roundcube:@localhost/roundcubemail?verify_server_cert=false'
$config['db_dsnw'] = 'mysql://roundcube:seagate@localhost:3306/roundcube';

// Log sent messages to <log_dir>/sendmail.log or to syslog
$config['smtp_log'] = false;

// Do not set db_dsnw here, use dpkg-reconfigure roundcube-core to configure database!
// IMAP host chosen to perform the log-in.
// See defaults.inc.php for the option description.
$config['imap_host'] = 'localhost:143';

// provide an URL where a user can get support for this Roundcube installation
// PLEASE DO NOT LINK TO THE ROUNDCUBE.NET WEBSITE HERE!
$config['support_url'] = '';

// Automatically register user in Roundcube database on successful (IMAP) logon.
// Set to false if only registered users should be allowed to the webmail.
// Note: If disabled you have to create records in Roundcube users table by yourself.
// Note: Roundcube does not manage/create users on a mail server.
$config['auto_create_user'] = false;

// This key is used to encrypt the users imap password which is stored
// in the session record. For the default cipher method it must be
// exactly 24 characters long.
// YOUR KEY MUST BE DIFFERENT THAN THE SAMPLE VALUE FOR SECURITY REASONS
$config['des_key'] = 'KDWN44HZaN+YYlyGY+E/ExLQ';

// List of active plugins (in plugins/ directory)
// Debian: install roundcube-plugins first to have any
$config['plugins'] = [];

// prefer displaying HTML messages
$config['prefer_html'] = false;


```
