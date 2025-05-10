import torch
import torch.nn as nn
import os
import time

output_dir = '/mnt/nfs/training-results'
combined_model_path = os.path.join(output_dir, 'combined_model.pth')

def build_model():
    return nn.Sequential(
        nn.Linear(100, 512),
        nn.ReLU(),
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Linear(512, 1)
    )

# Wait for both jobs
job_paths = [os.path.join(output_dir, f'model_checkpoint_job_{i}.pth') for i in range(1,3)]
print("Waiting for both checkpoints...")
print("Looking for these files:")
for p in job_paths:
    print("-", p)

while not all(os.path.exists(p) for p in job_paths):
    print("Still waiting... Current files:", os.listdir(output_dir))
    time.sleep(5)

print("✅ All files found, continuing...")

# Load and average
state_dicts = [torch.load(p, map_location='cpu') for p in job_paths]
combined = {}
for key in state_dicts[0].keys():
    combined[key] = (state_dicts[0][key] + state_dicts[1][key]) / 2.0

# Save
model = build_model()
model.load_state_dict(combined)
torch.save(model.state_dict(), combined_model_path)
print(f"✅ Combined model saved to {combined_model_path}")

