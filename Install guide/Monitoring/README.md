# GPU Monitoring Setup with Prometheus and Grafana

This guide walks you through setting up GPU monitoring on Kubernetes using Prometheus, Grafana, and the NVIDIA DCGM exporter.

---

## 1. Prometheus Setup

### Add and Update Helm Repository

```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### Verify Repository

```sh
helm repo list
```

### Install Kube-Prometheus-Stack

```sh
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace

# Verify installation
kubectl get pods -n monitoring
```

---

## 2. Configure Prometheus to Scrape GPU Metrics

### Check DCGM Exporter Logs and Namespace

```sh
MAYBE ADD HOW TO FIND IT?
kubectl logs -n gpu-operator nvidia-dcgm-exporter-<pod-name>
kubectl describe pod nvidia-dcgm-exporter-<pod-name> -n gpu-operator
```

### Identify Prometheus Instance

```sh
helm list -A
# Get the name of prometheus
kubectl get prometheus -n monitoring
```

### Edit Prometheus Custom Resource

```sh
kubectl get prometheus prometheus-kube-prometheus-prometheus -n monitoring -o yaml
```

- Set `serviceMonitorNamespaceSelector: {}` to allow all namespaces.
- Ensure `serviceMonitorSelector` has `matchLabels` with `release: prometheus`.

---

## 3. Create a ServiceMonitor for DCGM Exporter

### Check Existing ServiceMonitors

```sh
kubectl get servicemonitors -A
```

If none for DCGM exists, create one manually:

### Create `dcgm-servicemonitor.yaml`

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: dcgm-exporter-monitor
  namespace: gpu-operator       # 1. This is where you deploy it, use same namespace as DCGM Service
  labels:
    release: prometheus         # 2. Must match your Prometheus Helm release name
spec:
  selector:
    matchLabels:
      app: nvidia-dcgm-exporter # 3. Must match the labels on your DCGM Service
  endpoints:
    - port: gpu-metrics         # 4. Name of the port exposed by the Service
      interval: 30s
  namespaceSelector:
    matchNames:
      - gpu-operator
```
1. namespace: `get pods -A` (Check what namespace dcgm-exporter is running)
2. release: `kubectl get prometheus -n monitoring --show-labels` (check "release" under the labels header)
3. app: `kubectl get svc -n gpu-operator --show-labels` (check "app" under "label"-header)
4. port: `kubectl get svc nvidia-dcgm-exporter -n gpu-operator -o yaml` (check spec->ports->name)

### Apply the File

```sh
kubectl apply -f dcgm-servicemonitor.yaml
```

---

## 4. Access Prometheus Web UI

### Get the Service and Expose It

```sh
kubectl get svc -n monitoring
kubectl expose svc prometheus-operated --type=NodePort --name=prometheus-ui -n monitoring
```

### Access the Web Interface

In your browser, go to:

```
<your-node-ip>:<node-port>/targets
```

---

## 5. Grafana Setup

### Add and Update Helm Repository

```sh
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm repo list
```

### Install Grafana

```sh
helm install grafana grafana/grafana --namespace monitoring --create-namespace
kubectl get pods -n monitoring
```

### Expose Grafana Locally

```sh
kubectl get svc grafana -n monitoring
kubectl edit svc grafana -n monitoring
```

- Change `type: ClusterIP` to `type: NodePort`

### Access Grafana Web Interface

```sh
kubectl get svc grafana -n monitoring
```
Look for XXX

Then visit:

```
<your-node-ip>:<node-port>
```
---
