# Checkpoints
The university in the bigger picture wants to have computers running night time only but if jobs arent done the progress shouldnt be lost.

The only solution for a container to switch worker are if the container exits and get rescheduled but then all the progress would get lost.

Our solution are that the programmer have to use chechpoints in for example PyTorch. This makes it only lose the progress to the last checkpoint made. This means that before starting training it looks for a checkpoint and loads it if it exists.

## Example
You can use the provided manifest file:

- [ai-trainer-checkpoints.yaml](ai-trainer-checkpoints.yaml)

To make this test you need to delete/kill the job under training. Sense this is a `kind: job` it will automaticly make a new pod.

### Code
You can also look at the source code [HERE](Code/train.py).

### Output
In the logs you should find rows like this:

```sh
[2025-04-18 10:49:44] [Job 1 - 2] Checkpoint saved at epoch 500 
[2025-04-18 10:49:51] [Job 1 - 2] Checkpoint saved at epoch 1000 
[2025-04-18 10:49:59] [Job 1 - 2] Checkpoint saved at epoch 1500 
[2025-04-18 10:49:59] [Job 1 - 6] Resuming from epoch 1500 
````
Where `[Job 1 - 2 ]` was the first run and `[Job 1 - 6]` was the contiued run after `[Job 1 - 2 ]` got exited.