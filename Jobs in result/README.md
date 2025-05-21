# Result Run
This summarizes the results for our **thesis proof of concept**, where we executed **five jobs simultaneously** to observe **GPU Memory Utilization** and **GPU Utilization** metrics. The data was exported from **Grafana** as CSV files.
## Jobs
List of jobs executed for the result:
- [3000b2](3000b2.yaml)
- [3000b4](3000b4.yaml)
- [3000b6](3000b6.yaml)
- [3000b8](3000b8.yaml)
- [3000b12](3000b12.yaml)

> `3000` refers to the number of images processed.  
> `b` stands for batch size (ranging from 2 to 12).

## Result

### List for Worker1 and Worker2 GPU Memory Utilization
- [Worker1](Data/GPU%20Memory%20Utilization-Worker1.csv)
- [Worker2](Data/GPU%20Memory%20Utilization-Worker2.csv)
### List for Worker1 and Worker2 GPU Utilization
- [Worker1](Data/GPU%20Utilization-Worker1.csv)
- [Worker2](Data/GPU%20Utilization-Worker2.csv)