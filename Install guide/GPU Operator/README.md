# GPU Operator
## Install helm if you don't have it
```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```
## Get GPU Operator repositry and update it
```sh
helm repo add nvidia https://nvidia.github.io/gpu-operator
helm repo update
```
## Install GPU Operator
You can find the `values.yaml` in the folder
``` sh
helm install gpu-operator nvidia/gpu-operator --namespace gpu-operator --create-namespace --wait -f gpu-values.yaml
```

## Verify the installation
```sh
kubectl get pods -n gpu-operator-resources
```