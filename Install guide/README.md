# Installation guide
## Part 1: PC Setup
Before doing anything make sure your devices have the right [PC setup](PC%20setup/README.md).

## Part 2: Rancher
When PCs are ready next step would be to install and create the Kubernetes cluster using [Rancher](Rancher/README.md).

## Part 3: GPU Operator
Install [GPU Operator](GPU%20Operator/README.md) to automate the management of NVIDIA devices.

## Part 4: KAI Scheduler
To optimize GPU GPU resourse allocation for AI and machine learning we need a more robust Kubernetes Scheduler. Install [KAI Scheduler](KAI%20Scheduler/README.md).

## Part 5: NFS Share
To save files from training we used a [NFS Share](NFS%20Storage/README.md). NFS is a network storage system that any device on the local network can access.

## Part 6: Prometheus/Grafana
For monitoring install [Prometheus and Grafana](Monitoring/README.md). Prometheus collects metrics from the cluster and Grafana visualize the metrics collected.
