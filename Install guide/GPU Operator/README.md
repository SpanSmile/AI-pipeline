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

### Install GPU Operator
Ensure you have a `gpu-values.yaml` file available with your configuration.
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
Expected output should show the NVIDIA DCGM exporter and other components in a `Running` state.

---
