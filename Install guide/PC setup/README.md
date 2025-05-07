# PC & VM Setup Guide for Kubernetes Environment

This guide provides a setup procedure for all physical machines and virtual machines using Ubuntu 22.04 Server. It includes Kubernetes node configuration, and Docker setup for the Rancher host.

---

## 1. Base System Preparation

### OS Used
All machines (physical PCs and VMs) run **Ubuntu 22.04 Server**.

### Update & Upgrade
Ensure every system is up to date:
```sh
sudo apt update && sudo apt upgrade -y
```

## 2. Common Setup for All Kubernetes Nodes

### Disable Swap
Swap must be disabled for Kubernetes:
```sh
sudo swapoff -a
sudo nano /etc/fstab
```
- Comment out any line containing `swap`.

### Confirm Swap is Disabled
```sh
free -h
```
Look for this `Swap: 0B 0B 0B` in the output

### NFS Client Setup (for Worker Nodes Only)
This part is important to install that makes workers able to acces the NFS.
```sh
sudo apt install nfs-common
sudo systemctl restart rke2-agent
```

## 3. Rancher Host Setup

The PC or VM that will run Rancher needs Docker installed.

### Install Docker
```sh
sudo apt install docker.io -y
```
For the latest Docker Engine, see the [official Docker install guide](https://docs.docker.com/engine/install/ubuntu/).

### Verify Docker is Running
```sh
sudo systemctl status docker
```

### Optional: Enable Docker Without `sudo`
```sh
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
```
- You may need to **log out and back in** for group changes to take effect.


