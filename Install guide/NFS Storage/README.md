# NFS Storage Setup Guide
This guide walks you through setting up a simple NFS (Network File System) share on a Linux Ubuntu machine

---

## 1. NFS Server Setup on Ubuntu

### Install NFS Kernel Server
```sh
sudo apt update
sudo apt install nfs-kernel-server
```

### Create the NFS Shared Directory
```sh
sudo mkdir -p /srv/nfs
```

### Set Permissions
```sh
sudo chown nobody:nogroup /srv/nfs
sudo chmod 777 /srv/nfs
```
> ⚠️ These permissions make the directory fully open. Adjust for stricter access in production environments.


## 2. Configure NFS Exports

### Edit the Exports File
```sh
sudo nano /etc/exports
```
Add the following line:
```
/srv/nfs 192.168.X.X/24(rw,sync,no_subtree_check,no_root_squash,insecure)
```
- Replace `192.168.X.X` with your actual subnet (e.g. `192.168.1.0/24`).
- `no_root_squash` is useful for development, but not secure for production.

### Apply and Verify Export Configuration
```sh
sudo exportfs -ra    # Apply changes
sudo exportfs -v     # View active exports
```


## 3. Firewall Configuration (UFW)
Allow NFS traffic through the firewall:
```sh
sudo ufw allow from 192.168.X.X/24 to any port nfs
```
- Adjust IP/subnet to match your network.

## 4. Test NFS Access from Windows

### Enable NFS Client Feature
1. Open **Control Panel** → **Programs** → **Turn Windows features on or off**
2. Enable **Services for NFS**

### Access the NFS Share
1. Open **File Explorer**
2. Enter the path: `\\192.168.X.X\srv\nfs`
   - Replace `192.168.X.X` with your NFS server’s IP address.

If successful, you should see the contents of your `/srv/nfs` directory.

## 5. Persistant Volume & Persistant Volume Claim

### Adding PV and PVC
After verifying the NFS, we need to make Persistant Volume & Persistant Volume Claim in our kubernetes cluster. Provided following manifests:

- [pv.yaml](pv.yaml)
- [pvc.yaml](pvc.yaml)

```sh
kubectl apply -f pv.yaml -f pvc.yaml
```
### Verify
```sh
ADD HERE
```

## Test with a pod
Verify access to NFS from a pod. Provided following manifest:

- [testNFS.yaml](TESTS/testpod/testNFS.yaml)

### Open container
```sh
kubectl exec -it nfs-test-pod -- /bin/sh
```

### Add a file with `Hello from NFS!`
```sh
touch /mnt/nfs/test-file.txt
echo "Hello from NFS!" > /mnt/nfs/test-file.txt
```
Know you should find a .txt file with the text `Hello from NFS!` in your NFS share.


