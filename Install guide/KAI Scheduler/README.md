# KAI Scheduler Setup Guide

This guide walks you through setting up the NVIDIA KAI Scheduler on Kubernetes.

---

## 1. KAI Scheduler Setup

### GitHub Repository
You can find the official KAI Scheduler repository here: [KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler)

### Install Helm (if not already installed)
```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Add and Update KAI Scheduler Helm Repository
```sh
helm repo add nvidia-k8s https://helm.ngc.nvidia.com/nvidia/k8s
helm repo update
```

### Verify Repository
```sh
helm repo list
```

### Install KAI Scheduler
```sh
helm upgrade -i kai-scheduler nvidia-k8s/kai-scheduler \
  -n kai-scheduler \
  --create-namespace \
  --set "global.registry=nvcr.io/nvidia/k8s" \
  --set "global.gpuSharing=true"
```

---

## 2. Queue Configuration

### Apply Queue Definitions
Ensure you have a `queues.yaml` file with your desired configuration.
```sh
kubectl apply -f queues.yaml
```

### Verify Queue Creation
```sh
kubectl get queues
```
Expected output should list your configured queues.

---

## 3. Verification with Test Pod

To verify that the scheduler works correctly with GPU workloads, you can use the provided test pod manifest from the KAI Scheduler repository:

- [gpu-pod.yaml](https://github.com/NVIDIA/KAI-Scheduler/blob/main/docs/quickstart/pods/gpu-pod.yaml)

### Deploy the Test Pod
```sh
kubectl apply -f gpu-pod.yaml
```

### Check Pod Logs
```sh
kubectl logs <pod-name>
```

### Example Output
The output should show `nvidia-smi` results similar to the following:
```sh
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 535.54.03    Driver Version: 535.54.03    CUDA Version: 12.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            Off  | 00000000:00:1E.0 Off |                    0 |
| N/A   55C    P8     9W /  70W |      0MiB / 15109MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```

---

