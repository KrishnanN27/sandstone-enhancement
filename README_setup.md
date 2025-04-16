# 🛠️ Setup & Reproducibility Guide

This guide explains how to run the full super-resolution pipeline on sandstone tomogram slices using the ResShift diffusion model.

---

## 📦 Step 1: Set Up the Environment

### 🔹 Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 🔹 Install required Python packages

```bash
pip install -r requirements.txt
```

### ⚠️ If using a GPU with CUDA:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## 🔗 Step 2: Clone the ResShift Model

This project depends on [ResShift (NeurIPS 2023)](https://github.com/zsyOAOA/ResShift) for diffusion-based image enhancement.

Clone it separately:

```bash
git clone https://github.com/zsyOAOA/ResShift.git
```

> ❗ Keep it outside this project folder. We'll reference it from where it's cloned.

---

## 🚀 Step 3: Run the Full Pipeline

### 1️⃣ Extract 2D Slices from `.nc` Dataset

```bash
python save_slices.py

```

The script expects the dataset file to be located at:

```

tomo_R_SSw_SS_nc/block00000001.nc

```

So the downloaded `.nc` file is placed in a folder named `tomo_R_SSw_SS_nc` in the root of this project:

```

project-root/
├── save_slices.py
├── tomo_R_SSw_SS_nc/
│ └── block00000001.nc

```

This script loads the NetCDF tomogram and extracts 2D grayscale PNG slices to `slices1/`.

---

### 2️⃣ Resize Slices for Inference

```bash
python reduce_size.py
```

This creates 128×128 versions of the slices and saves them to `slices_small/`.

---

### 3️⃣ Run ResShift Super-Resolution

From inside the cloned `ResShift/` folder:

```bash
cd ../ResShift
python inference_resshift.py -i ../slices_small -o ../results_small --task realsr --scale 4 --version v3
```

Outputs will be saved in `results_small/`.

---

### 5️⃣ Evaluate Results (PSNR & SSIM)

```bash
python eval_metrics.py
```

This script calculates average PSNR and SSIM across slices.

---

## 📁 Output Summary

| Folder/File        | Description                                |
| ------------------ | ------------------------------------------ |
| `slices_small/`    | Resized input images (128×128)             |
| `results/`         | ResShift-enhanced outputs (512×512)        |
| `comparison_grid/` | Side-by-side before/after image grids      |
| `comparison.gif`   | Animated scroll-through of enhanced slices |
| `metrics output`   | Printed in terminal via `eval_metrics.py`  |

---
