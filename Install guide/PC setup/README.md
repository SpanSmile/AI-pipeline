# PC Setup

We used Ununtu 22.04 server for all PCs and VMs
## Commands
### Make sure to update and upgrade all PC
```sh
sudo apt update && sudo apt upgrade -y
```
## Commands for all Kubernetes PCs

### Remove Swap
```sh
sudo swapoff -a
sudo nano /etc/fstab   # Commenting out the swap entry
```

### Confrim it's no longer active
```sh
free -h
```
Look for `Swap: 0B 0B 0B`

### If using a NFS share install NFS-tools to `WORKER` nodes
```sh
sudo apt install nfs-common
sudo systemctl restart rke2-agent
```

## Commands Rancher PC
### Install Docker
```sh
sudo apt install docker.io -y
```
You can also download the newer Engine [HERE](https://docs.docker.com/engine/install/ubuntu/)
### Make sure Docker is running
```sh
sudo systemctl status docker
```

### Add user to be able to acces Docker without sudo
```sh
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
```
