sudo nano /etc/hosts
ssh-keygen -t ed25519
touch .ssh/authorized_keys
cat .ssh/id_ed25519.pub > .ssh/authorized_keys
ssh milav@rpi
sudo nano /etc/ssh/sshd_config


   40  sudo apt install gh
   41  gh ssh-key add .ssh/id_ed25519.pub --title "RPi Key"
   42  gh auth login
   43  mkdir code
   44  cd code
   45  git clone git@github:milavdabgar/ipEmail.git
   46  git clone git@github.com:milavdabgar/ipEmail.git
   47  git clone git@github.com:milavdabgar/milavdabgar.github.io
   48  git clone git@github.com:milavdabgar/gppLMSv1.git
   49  git clone git@github.com:milavdabgar/config-to-md.git


sudo apt install samba
sudo ufw allow Samba
sudo apt install cifs-utils
sudo mkdir -p /mnt/backup-drive
sudo nano /root/.smbcredentials
sudo chmod 600 /root/.smbcredentials

sudo nano /etc/fstab
//192.168.0.1/G /mnt/backup-drive cifs vers=2.0,credentials=/root/.smbcredentials,iocharset=utf8,file_mode=0777,dir_mode=0777 0 0
sudo systemctl daemon-reload
sudo mounmt -a
df -h
sudo mkdir -p /mnt/backup-drive/Backups/rpi
sudo chmod -R 777 /mnt/backup-drive/Backups/rpi