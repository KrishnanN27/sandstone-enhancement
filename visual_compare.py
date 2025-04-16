from PIL import Image
import os

input_dir = "slices_small"
output_dir = "results_small"
compare_dir = "comparison_grid"

os.makedirs(compare_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if fname.endswith(".png") and os.path.exists(os.path.join(output_dir, fname)):
        lr = Image.open(os.path.join(input_dir, fname)).convert("L").resize((256, 256))
        sr = Image.open(os.path.join(output_dir, fname)).convert("L").resize((256, 256))

        grid = Image.new("L", (512, 256))
        grid.paste(lr, (0, 0))
        grid.paste(sr, (256, 0))
        grid.save(os.path.join(compare_dir, fname))

print("✅ Comparison grids saved to:", compare_dir)
