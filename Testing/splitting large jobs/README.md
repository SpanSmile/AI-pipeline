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
- [ai-trainer-checkpoints.yaml](ai-trainer-checkpoints.yaml)

To make this test you need run `combine.yaml` when both `job1.yaml` and `job2.yaml` are finished.

### Code
You can also look at the source code:

- For training [HERE](Code/train/train.py). 
- For combing [HERE](Code/combine/train.py).
