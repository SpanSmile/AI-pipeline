# Storage
We installed a NFS share on a desktop that runs a Ubuntu Desktop OS
## NFS
### Install NFS-kernel-server
```sh
sudo apt install nfs-kernel-server
```
### Make a directory for the NFS share
```sh
sudo mkdir -p /srv/nfs
```

### Permissions for the NFS folder
```sh
sudo chown nobody:nogroup /srv/nfs
sudo chmod 777 /srv/nfs
```

## Change NFS exports Config
``` sh
sudo nano exports   # Add row bellow
/srv/nfs 192.168.X.X/24(rw,sync,no_subtree_check,no_root_squash,insecure)

sudo exportfs -ra  # Apply changes
sudo exportfs -v   # Verify changes
```
Change to match your NFS PCs IP adrress
### Firewall rules
You might need to change your firewall rules to make it work
``` sh
sudo ufw allow from 192.168.X.X/24 to any port nfs
```
Change to match your NFS PCs IP adrress

## Test on windows
- Enable NFS windows service. Controlpanel -> Program -> Activate inactivate windows functions
- Test and se if you can access it in file explorer \\\\192.168.X.X\srv\nfs (\\\\IP\location) 