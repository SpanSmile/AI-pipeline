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
Look for an output like this::
```sh
NAME                    URL
nvidia-k8s              https://helm.ngc.nvidia.com/nvidia/k8s
```

### Install KAI Scheduler
```sh
helm upgrade -i kai-scheduler nvidia-k8s/kai-scheduler \
  -n kai-scheduler \
  --create-namespace \
  --set "global.registry=nvcr.io/nvidia/k8s" \
  --set "global.gpuSharing=true"
```


## 2. Queue Configuration

### Apply Queue Definitions
Ensure you have a `queues.yaml` file with your desired configuration. Provided manifest:
- [gueues.yaml](queues.yaml)
```sh
kubectl apply -f queues.yaml
```

### Verify Queue Creation
```sh
kubectl get queues
```
Expected output should list:
```sh
NAME      PRIORITY   PARENT    CHILDREN   DISPLAYNAME
default
test                 default
```

## 3. Verification with Test Pod

To verify that the scheduler works correctly with GPU workloads, you can use the provided test pod manifest:

- [gpu-pod.yaml](TESTS/GPU-test-pod/gpu-test-pod.yaml)

### Deploy the Test Pod
```sh
kubectl apply -f gpu-test-pod.yaml
```

### Check Pod Logs
```sh
kubectl logs <pod-name>
```

### Example Output
The output should show `nvidia-smi` results similar to the following:
```sh
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.15              Driver Version: 550.54.15      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A5000               On  |   00000000:01:00.0 Off |                  Off |
| 30%   34C    P8             24W /  230W |       1MiB /  24564MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```
## 4. Verification with Job pods
To verify a single job and multiple jobs running on the same node and sharing a single gpu.

### One job

Provided manifest:

- [training-job-1.yaml](TESTS/testJob-KAI/training-job-1.yaml)

In Rancher gui inside your cluster. In Workloads -> Pods, find you pod and make sure pod state in state `Completed`

### Multiple jobs

Provided manifests:

- [training-job-1.yaml](TESTS/testJob-KAI/training-job-1.yaml)
- [training-job-2.yaml](TESTS/testJob-KAI/training-job-2.yaml)

In Rancher gui inside your cluster. In Workloads -> Pods, find you pods and make sure both is running at the same time and same worker.

MAYBE ADD PICTURE???