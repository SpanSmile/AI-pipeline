# KAI Scheduler
## Get KAI-Scheduler repository and update it
```sh
helm repo add nvidia-k8s https://helm.ngc.nvidia.com/nvidia/k8s
helm repo update
```
## Install KAI-Scheduler
```sh
helm upgrade -i kai-scheduler nvidia-k8s/kai-scheduler -n kai-scheduler --create-namespace --set "global.registry=nvcr.io/nvidia/k8s" --set "global.gpuSharing=true"
```

## Make the queues for KAI-Scheduler
You can find the `queues.yaml` in the folder
```sh
kubectl apply -f queues.yaml
```

## Verify the creation of queues
```sh
kubectl get queues
```