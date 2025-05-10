# Thesis Work

INFROMATION.......

Technologies used:
- Ubuntu 22.04 Server (on all nodes)
- Kubernetes via RKE2
- NVIDIA KAI Scheduler
- NFS for shared storage
- Docker for Rancher management

---

## Project Goals
Develop a Kubernetes-based GPU-cluster as a proof of concept for University West, with the following functionalities:
- Jobs that exceed the VRAM pool size of a single GPU can be split to run in parallel instead of in sequence, to reduce training time.  
- Several jobs can run simultaneously on the same worker node to optimize utilization and reduce wasted resources.
- Preferrably, the cluster should be usable through a previously created webserver environment, simplifying the process of starting a job.
---

## Installation
Follow the [Install Guide](Install%20guide/README.md) to replicate the full cluster setup.

## Testing

[Testing Checkpoints](Testing/checkpoints/README.md)

[Testing splitting large jobs](Testing/splitting%20large%20jobs/README.md)

## Result
[Result Runs](Jobs%20in%20result/README.md)



---

