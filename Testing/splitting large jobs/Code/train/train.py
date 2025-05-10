import torch
import torch.nn as nn
import torch.optim as optim
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--job_id', type=int, default=0)
args = parser.parse_args()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"[Job {args.job_id}] Using device: {device}")

# Split dummy data differently per job
total_samples = 50000
split_size = total_samples // 2
start_idx = args.job_id * split_size
end_idx = start_idx + split_size

# Full dataset (same seed across jobs ensures same data)
torch.manual_seed(42)
x_full = torch.randn(total_samples, 100)
y_full = torch.randn(total_samples, 1)

# Slice per job
x = x_full[start_idx:end_idx].to(device)
y = y_full[start_idx:end_idx].to(device)

# Model
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

# Save path
output_dir = '/mnt/nfs/training-results'
os.makedirs(output_dir, exist_ok=True)
model_path = os.path.join(output_dir, f'model_checkpoint_job_{args.job_id}.pth')

# Training loop
start = time.time()
for epoch in range(2000):  # Less per job
    optimizer.zero_grad()
    output = model(x)
    loss = loss_fn(output, y)
    loss.backward()
    optimizer.step()
    print(f"[Job {args.job_id}] Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Save model
torch.save(model.state_dict(), model_path)
print(f"[Job {args.job_id}] Model saved to {model_path}")
print(f"[Job {args.job_id}] Done in {time.time() - start:.2f}s")

