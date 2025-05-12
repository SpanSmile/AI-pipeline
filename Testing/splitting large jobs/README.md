# Splitting large jobs
To run jobs larger than the available VRAM on a GPU, the job has to be split into smaller segments. This demonstration shows an example of how two jobs can be split to run separately and then be combined using a third job to form a final result.

## Example
You can use the provided manifest files:

### Train
The following two jobs will later be combined into one result.
- [job1.yaml](job1.yaml)
- [job2.yaml](job2.yaml)

### Combine
This will combine `job1.yaml` and `job2.yaml`.
- [combine.yaml](combine.yaml)

To make this test you need run `combine.yaml` when both `job1.yaml` and `job2.yaml` are finished.


### Output
In the logs you should find rows like the following to verify that the jobs have successfully been combined:

```sh
# Job 1
[Job 1] Model saved to /mnt/nfs/training-results/model_checkpoint_job_1.pth
[Job 1] Done in 16.33s
# Job 2
[Job 2] Model saved to /mnt/nfs/training-results/model_checkpoint_job_2.pth
[Job 2] Done in 4.71s
# Combined
Combined model saved to /mnt/nfs/training-results/combined_model.pth
````
### Code
You can also look at the source code:

- For training [HERE](Code/train/train.py). 
- For combing [HERE](Code/combine/train.py).
