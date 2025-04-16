from PIL import Image
import os

input_dir = "slices1"
output_dir = "slices_small"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        img = Image.open(os.path.join(input_dir, filename))
        img = img.resize((128, 128))
        img.save(os.path.join(output_dir, filename))
