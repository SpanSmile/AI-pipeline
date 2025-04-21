# Rancher

## Install Rancher with Docker
```sh
sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher
```
## Create Cluster
Create -> custom
![rke2](<Screenshot from 2025-04-21 12-18-34.png>)

### Management and etcd
```sh
curl --insecure -fL https://<RANCHER_SERVER_IP_OR_DOMAIN>/system-agent-install.sh | sudo sh -s - \
  --server https://<RANCHER_SERVER_IP_OR_DOMAIN> \
  --label 'cattle.io/os=linux' \
  --token <NODE_REGISTRATION_TOKEN> \
  --ca-checksum <CA_CHECKSUM> \
  --etcd \
  --controlplane
```

### Worker
```sh
curl --insecure -fL https://<RANCHER_SERVER_IP_OR_DOMAIN>/system-agent-install.sh | sudo sh -s - \
  --server https://<RANCHER_SERVER_IP_OR_DOMAIN> \
  --label 'cattle.io/os=linux' \
  --token <NODE_REGISTRATION_TOKEN> \
  --ca-checksum <CA_CHECKSUM> \
  --worker
```

## Make management access kubectl
```sh
find / -name kubectl 2>/dev/null
sudo ln -s /var/lib/rancher/rke2/data/v1.30.10-rke2r1-358c11a13b19/bin/kubectl /usr/local/bin/kubectl
kubectl version --client

export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
echo 'export KUBECONFIG=/etc/rancher/rke2/rke2.yaml' >> ~/.bashrc source ~/.bashrc
sudo chmod 644 /etc/rancher/rke2/rke2.yaml
sudo chown $(whoami) /etc/rancher/rke2/rke2.yaml
```

```sh
NAME         STATUS   ROLES                       AGE     VERSION
management   Ready    control-plane,etcd,master   11d     v1.30.11+rke2r1
worker1      Ready    worker                      11d     v1.30.11+rke2r1
worker2      Ready    worker                      2d22h   v1.30.11+rke2r1
```