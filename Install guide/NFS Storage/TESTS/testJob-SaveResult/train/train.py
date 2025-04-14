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

# Ensure the output directory exists
output_dir = '/mnt/nfs/training-results'  # The NFS mount point
os.makedirs(output_dir, exist_ok=True)

# Save model path
model_save_path = os.path.join(output_dir, f'model_checkpoint_job_{args.job_id}.pth')

# More epochs
start = time.time()
for epoch in range(4000):  # Adjust as needed for your hardware
    optimizer.zero_grad()
    output = model(x)
    loss = loss_fn(output, y)
    loss.backward()
    optimizer.step()
    print(f"[Job {args.job_id}] Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Save the trained model after training
torch.save(model.state_dict(), model_save_path)
print(f"[Job {args.job_id}] Model saved at {model_save_path}")

end = time.time()
print(f"[Job {args.job_id}] Training finished in {end - start:.2f} seconds.")

