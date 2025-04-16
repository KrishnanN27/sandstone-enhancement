from skimage.metrics import peak_signal_noise_ratio, structural_similarity
from PIL import Image
import numpy as np
import os

input_dir = "slices_small"
output_dir = "results"

psnr_scores = []
ssim_scores = []

for fname in os.listdir(input_dir):
    if fname.endswith(".png") and os.path.exists(os.path.join(output_dir, fname)):
        lr = Image.open(os.path.join(input_dir, fname)).convert("L")
        sr = Image.open(os.path.join(output_dir, fname)).convert("L")

        # Resize SR to match LR (since SR is 4x)
        sr = sr.resize(lr.size)

        lr_np = np.array(lr)
        sr_np = np.array(sr)

        psnr = peak_signal_noise_ratio(lr_np, sr_np)
        ssim = structural_similarity(lr_np, sr_np)

        psnr_scores.append(psnr)
        ssim_scores.append(ssim)

        print(f"{fname}: PSNR={psnr:.2f} dB, SSIM={ssim:.3f}")

print("\n📊 Overall Average:")
print(f"PSNR: {np.mean(psnr_scores):.2f} dB")
print(f"SSIM: {np.mean(ssim_scores):.3f}")
