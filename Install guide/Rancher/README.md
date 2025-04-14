# Rancher
```sh
find / -name kubectl 2>/dev/null
sudo ln -s /var/lib/rancher/rke2/data/v1.30.10-rke2r1-358c11a13b19/bin/kubectl /usr/local/bin/kubectl
kubectl version --client

export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
echo 'export KUBECONFIG=/etc/rancher/rke2/rke2.yaml' >> ~/.bashrc source ~/.bashrc
sudo chmod 644 /etc/rancher/rke2/rke2.yaml
sudo chown $(whoami) /etc/rancher/rke2/rke2.yaml
```