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
Look for an output like this::
```sh
NAME                    URL
prometheus-community    https://prometheus-community.github.io/helm-charts
```

### Install Kube-Prometheus-Stack

```sh
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace

# Verify installation
kubectl get pods -n monitoring
```


## 2. Configure Prometheus to Scrape GPU Metrics

### Check DCGM Exporter Logs and Namespace

```sh
# Get the name of a DCGM-exporter
kubectl get pods -n gpu-operator

# See if metrics collection enabled
kubectl logs -n gpu-operator nvidia-dcgm-exporter-<pod-name>
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


## 3. Create a ServiceMonitor for DCGM Exporter

### Check Existing ServiceMonitors

```sh
kubectl get servicemonitors -A
```

If none for DCGM exists, create one manually:

### Create a DCGM ServiceMonitor

Provided manifest:

- [dcgm-serviceminitor.yaml](dcgm-servicemonitor.yaml)

Remember to change the commented lines. See bellow to find the right names.
```sh
#1. namespace (Check what namespace dcgm-exporter is running in)
get pods -A

#2. release (Check "release=XXX" under the labels header)
kubectl get prometheus -n monitoring --show-labels

#3. app (check "app=XXX" under "label"-header for DCGM-exporter)
kubectl get svc -n gpu-operator --show-labels

#4. port (Check spec->ports->name)
kubectl get svc nvidia-dcgm-exporter -n gpu-operator -o yaml
```

### Apply the File

```sh
kubectl apply -f dcgm-servicemonitor.yaml
```


## 4. Access Prometheus Web UI

### Get the Service and Expose It

```sh
kubectl get svc -n monitoring
kubectl expose svc prometheus-operated --type=NodePort --name=prometheus-ui -n monitoring
```
### Access Prometheus Web Interface
```sh
kubectl get svc prometheus-ui -n monitoring
```
Look for ports, similar like this: `9090:32508/TCP`
### Access the Web Interface

In your browser, go to:

```
<your-node-ip>:32508/targets
```
Look for a line containing `DCGM`. Important that is says state: `UP`


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
Look for ports, similar like this: 80:30948/TCP

Then visit:

```
<your-node-ip>:30948
```
---

### Monitoring test
Run some load example manifest:

- [training-job-1.yaml](../KAI%20Scheduler/TESTS/testJob-KAI/training-job-1.yaml)
- [training-job-2.yaml](../KAI%20Scheduler/TESTS/testJob-KAI/training-job-1.yaml)

As it runs check the monitoring dashboard.
