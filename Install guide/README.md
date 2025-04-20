# Installation guide
## Step 1 PC Setup
Before doing anything make sure your devices have the right [PC setup](PC%20setup/README.md).

## Step 2 Rancher
When PCs are ready next step would be to install and create the Kubernetes cluster using [Rancher](Rancher/README.md).

## Step 3 GPU Operator
Install [GPU Operator](GPU%20Operator/README.md) to automate the management of NVIDIA devices.

## Step 4 Prometheus/Grafana
For monitoring install [Prometheus and Grafana](Monitoring/README.md). Prometheus collects metrics from the cluster and Grafana visualize the metrics collected.

## Step 5 KAI Scheduler
To optimize GPU GPU resourse allocation for AI and machine learning we need a more robust Kubernetes Scheduler. Install [KAI Scheduler](KAI%20Scheduler/README.md).