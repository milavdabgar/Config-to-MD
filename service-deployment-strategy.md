# Service Deployment Strategy Guide

## 1. Run Natively (On Host System)

### 1.1 Core System Services
1. SSH Server
   - Reason: Core system access, security critical
   - Installation: `sudo apt install openssh-server`

2. UFW (Firewall)
   - Reason: Host-level security, container network management
   - Installation: `sudo apt install ufw`

3. Timeshift
   - Reason: System-level backups, requires direct system access
   - Installation: `sudo apt install timeshift`

### 1.2 File Sharing Services
1. Samba
   - Reason: Direct hardware access, better performance
   - Uses: Local file sharing, backup storage
   - Installation: `sudo apt install samba`

2. NFS Server
   - Reason: Low-level system integration, performance
   - Uses: Network file system for Linux clients
   - Installation: `sudo apt install nfs-kernel-server`

### 1.3 Monitoring & Management
1. System Monitoring Tools
   - Reason: Need direct system access
   - Tools: htop, iotop, nethogs
   - Installation: `sudo apt install htop iotop nethogs`

2. Log Management
   - Reason: System-wide log collection
   - Tool: rsyslog
   - Installation: Built-in

### 1.4 Basic Network Services
1. Network Manager
   - Reason: Core network functionality
   - Installation: Built-in

2. avahi-daemon (for .local domains)
   - Reason: Local network discovery
   - Installation: `sudo apt install avahi-daemon`

## 2. Run in Docker

### 2.1 Web Services
1. WordPress Sites
   ```yaml
   services:
     wordpress:
       image: wordpress
     db:
       image: mariadb
   ```

2. Nginx Reverse Proxy
   ```yaml
   services:
     nginx:
       image: nginx
   ```

3. Personal Portfolio
   ```yaml
   services:
     portfolio:
       image: nginx
   ```

### 2.2 Development & Learning Projects
1. Flask/Vue Applications
   ```yaml
   services:
     frontend:
       image: node
     backend:
       image: python
   ```

2. Learning Environments
   - Development databases
   - Test servers
   - Staging environments

### 2.3 Cloud Storage
1. Nextcloud
   ```yaml
   services:
     nextcloud:
       image: nextcloud
     db:
       image: mariadb
   ```

### 2.4 Mail Services
1. Complete Mail Stack
   ```yaml
   services:
     postfix:
       image: postfix
     dovecot:
       image: dovecot
     roundcube:
       image: roundcube
   ```

### 2.5 Database Servers
1. MariaDB/MySQL
   ```yaml
   services:
     db:
       image: mariadb
   ```

2. PostgreSQL
   ```yaml
   services:
     db:
       image: postgres
   ```

### 2.6 Development Tools
1. GitLab/Gitea
   ```yaml
   services:
     gitea:
       image: gitea/gitea
   ```

2. CI/CD Tools
   ```yaml
   services:
     jenkins:
       image: jenkins/jenkins
   ```

## 3. Implementation Strategy

### 3.1 Docker Network Setup
```bash
# Create main network
docker network create web-network

# Create mail network
docker network create mail-network
```

### 3.2 Volume Management
```bash
# Create named volumes
docker volume create wordpress_data
docker volume create nextcloud_data
docker volume create mail_data
```

### 3.3 Directory Structure
```plaintext
/home/milav/
├── docker/
│   ├── wordpress/
│   ├── nextcloud/
│   ├── mail/
│   └── nginx-proxy/
└── native/
    ├── samba/
    └── nfs/
```

## 4. Decision Making Guide

### 4.1 Run Natively If:
1. Service requires direct hardware access
2. Service is security-critical
3. Service needs maximum performance
4. Service is part of core system functionality
5. Service manages other services

### 4.2 Run in Docker If:
1. Service is self-contained
2. Service needs isolation
3. Service is being developed/tested
4. Service needs easy version management
5. Service might need to be moved to another server
6. Service is part of a development stack

## 5. Migration Path

### 5.1 From Native to Docker
1. Document current configuration
2. Create Docker composition
3. Test in parallel
4. Migrate data
5. Switch DNS/reverse proxy

### 5.2 From Docker to Native
1. Export data from container
2. Install native service
3. Import data
4. Test functionality
5. Update DNS/proxy

## 6. Maintenance Considerations

### 6.1 Native Services
- Regular system updates
- Configuration backups
- Log rotation
- Performance monitoring

### 6.2 Docker Services
- Image updates
- Volume backups
- Container health checks
- Resource limits

## 7. Scaling Considerations

### 7.1 Native Services
- Hardware upgrades
- Load balancing
- Service optimization

### 7.2 Docker Services
- Container replication
- Resource allocation
- Network optimization
