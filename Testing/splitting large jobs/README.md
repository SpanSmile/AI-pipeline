# Splitting large jobs
To run bigger jobs than physicaly avaiable on one node, we have to make the training jobs in smaller parts. This demonstration is just showing an example of how two trainings can be combined in the end.

## Example
You can use the provided manifest files:

### Train
These two jobs will later be combined.
- [job1.yaml](ai-trainer-checkpoints.yaml)
- [job1.yaml](ai-trainer-checkpoints.yaml)

### Combine
This will combine `job1.yaml` and ``job2.yaml`.
- [ai-trainer-checkpoints.yaml](ai-trainer-checkpoints.yaml)

To make this test you need run `combine.yaml` when both `job1.yaml` and `job2.yaml` are finished.

### Code
You can also look at the source code:

- For training [HERE](Code/train/train.py). 
- For combing [HERE](Code/combine/train.py).