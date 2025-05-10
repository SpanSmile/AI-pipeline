import torch
import torch.nn as nn
import torch.optim as optim
import time
import argparse
import os
import logging
import random

num = random.randint(1,10)

parser = argparse.ArgumentParser()
parser.add_argument('--job_id', type=int, default=0)
args = parser.parse_args()

# Output directory
output_dir = '/mnt/nfs/training-results'
os.makedirs(output_dir, exist_ok=True)

# Setup logging
log_file = os.path.join(output_dir, f'job_{args.job_id}_log.txt')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
logging.info(f"[Job {args.job_id} - {num}] Using device: {device}")
msg = f"[Job {args.job_id}] Using device: {device}"
print(msg)

# Larger dummy data
x = torch.randn(50000, 100).to(device)
y = torch.randn(50000, 1).to(device)

# Bigger model
model = nn.Sequential(
    nn.Linear(100, 512),
    nn.ReLU(),
    nn.Linear(512, 512),
    nn.ReLU(),
    nn.Linear(512, 512),
    nn.ReLU(),
    nn.Linear(512, 1)
).to(device)

loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Checkpoint path
checkpoint_path = os.path.join(output_dir, f'model_checkpoint_job_{args.job_id}.pth')

# Load checkpoint if exists
start_epoch = 0
if os.path.exists(checkpoint_path):
    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    start_epoch = checkpoint['epoch'] + 1
    logging.info(f"[Job {args.job_id} - {num}] Resuming from epoch {start_epoch}")
    msg = f"[Job {args.job_id}] Resuming from epoch {start_epoch}"
    print(msg)

# Training loop
total_epochs = 4000
checkpoint_interval = 500  # Save every 500 epochs

start_time = time.time()
for epoch in range(start_epoch, total_epochs):
    model.train()
    optimizer.zero_grad()
    output = model(x)
    loss = loss_fn(output, y)
    loss.backward()
    optimizer.step()

    logging.info(f"[Job {args.job_id} - {num}] Epoch {epoch + 1}, Loss: {loss.item():.4f}")
    msg = f"[Job {args.job_id}] Epoch {epoch + 1}, Loss: {loss.item():.4f}"
    print(msg)

    # Save checkpoint
    if (epoch + 1) % checkpoint_interval == 0 or (epoch + 1) == total_epochs:
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict()
        }, checkpoint_path)
        logging.info(f"[Job {args.job_id} - {num}] Checkpoint saved at epoch {epoch + 1}")
        msg = f"[Job {args.job_id}] Checkpoint saved at epoch {epoch + 1}"
        print(msg)

end_time = time.time()
logging.info(f"[Job {args.job_id} - {num}] Training finished in {end_time - start_time:.2f} seconds.")
msg = f"[Job {args.job_id}] Training finished in {end_time - start_time:.2f} seconds."
print(msg)

