import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import os

# === Step 1: Load data ===
file_path = "tomo_R_SSw_SS_nc/block00000001.nc"
ds = xr.open_dataset(file_path)

# Extract the 3D volume
volume = ds["tomo"].values  # shape: (400, 800, 800)

# === Step 2: Normalize to 0–255 ===
volume = volume.astype(np.float32)
volume -= volume.min()
volume /= volume.max()
volume *= 255.0
volume = volume.astype(np.uint8)

# === Step 3: Save selected slices ===
output_dir = "slices1"
os.makedirs(output_dir, exist_ok=True)

print(f"Saving slices to: {output_dir}")
for i in range(0, volume.shape[0], 50):  # every 50th slice
    plt.imsave(f"{output_dir}/slice_{i:03d}.png", volume[i], cmap="gray")

print("✅ Done.")
