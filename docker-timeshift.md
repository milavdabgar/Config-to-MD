sudo apt install cifs-utils
sudo mkdir -p /mnt/backup-drive
sudo nano /root/.smbcredentials
sudo chmod 600 /root/.smbcredentials




sudo apt install samba
sudo ufw allow Samba
sudo nano /etc/fstab
//192.168.0.1/G /mnt/backup-drive cifs vers=2.0,credentials=/root/.smbcredentials,iocharset=utf8,file_mode=0777,dir_mode=0777 0 0
sudo systemctl daemon-reload
sudo mounmt -a
df -h
sudo mkdir -p /mnt/backup-drive/Backups/rpi
sudo chmod -R 777 /mnt/backup-drive/Backups/rpi