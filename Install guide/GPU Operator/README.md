# GPU Operator Setup Guide

This guide walks you through setting up the NVIDIA GPU Operator on Kubernetes.

---

## 1. GPU Operator Setup

### GitHub Repository
You can find the official GPU Operator repository here: [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator)

### Install Helm (if not already installed)
```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Add and Update NVIDIA GPU Operator Repository
```sh
helm repo add nvidia https://nvidia.github.io/gpu-operator
helm repo update
```

### Verify Repository
```sh
helm repo list
```
Look for an output like this::
```sh
NAME                    URL
nvidia                  https://nvidia.github.io/gpu-operator
```

### Install GPU Operator
Ensure you have a `gpu-values.yaml` file available with your configuration. Provided manifest:
- [values.yaml](values.yaml)
```sh
helm install gpu-operator nvidia/gpu-operator \
  --namespace gpu-operator \
  --create-namespace \
  --wait \
  -f gpu-values.yaml
```

### Verify the Installation
Check for running pods in the GPU Operator namespace:
```sh
kubectl get pods -n gpu-operator
```
Look for an output like this::
```sh
NAME                                                          READY   STATUS    RESTARTS        AGE
gpu-feature-discovery-5thll                                   1/1     Running   0               11d
gpu-feature-discovery-7mcnm                                   1/1     Running   0               2d21h
gpu-operator-64b6d46dbc-66qng                                 1/1     Running   16 (23h ago)    2d20h
gpu-operator-node-feature-discovery-gc-588bf46b7d-9rn46       1/1     Running   0               2d20h
gpu-operator-node-feature-discovery-master-8495ccc578-27fhf   1/1     Running   0               2d20h
gpu-operator-node-feature-discovery-worker-hcv7h              1/1     Running   14 (2d4h ago)   2d21h
gpu-operator-node-feature-discovery-worker-jbdkt              1/1     Running   471 (23h ago)   11d
nvidia-container-toolkit-daemonset-gqxp9                      1/1     Running   0               11d
nvidia-container-toolkit-daemonset-zsld7                      1/1     Running   0               2d21h
nvidia-dcgm-exporter-9928p                                    1/1     Running   0               2d21h
nvidia-dcgm-exporter-s872m                                    1/1     Running   0               11d
nvidia-device-plugin-daemonset-5lw5t                          1/1     Running   0               11d
nvidia-device-plugin-daemonset-zjw7g                          1/1     Running   0               2d21h
nvidia-driver-daemonset-r8kjp                                 1/1     Running   0               2d21h
nvidia-driver-daemonset-wtt7b                                 1/1     Running   0               11d
nvidia-operator-validator-hxt7z                               1/1     Running   0               11d
nvidia-operator-validator-xn55k                               1/1     Running   0               2d21h

```
In this output we have two workers which makes duplicates

## 2. Make a test pod
To verify that the GPU Operator works correctly using GPU, you can use the provided test pod manifest:
- [testJob-seeGPU.yaml](TEST/testJob-seeGPU.yaml)

### Deploy the Test Pod
```sh
kubectl apply -f testJob-seeGPU.yaml
```

### Check Pod Logs
```sh
kubectl logs <pod-name>
```
Look for an output like this: `[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]`