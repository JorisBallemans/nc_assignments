import os
import re
import imageio

# Ask the user for the input directory
input_dir = input("Enter the directory containing PNG images: ").strip()

# Ask for the output GIF filename
gif_name = input("Enter the output GIF filename (without extension): ").strip() + ".gif"

# Define the output directory
output_dir = "output-gif"
os.makedirs(output_dir, exist_ok=True)  # Create if it doesn't exist

# Extract numbers from filenames and sort numerically
def extract_number(filename):
    match = re.search(r'boids-t(\d+)\.png', filename)
    return int(match.group(1)) if match else float('inf')

# Get and sort image files
images = sorted(
    [img for img in os.listdir(input_dir) if img.endswith(".png")],
    key=extract_number
)

# Read and convert images to a GIF
frames = [imageio.imread(os.path.join(input_dir, img)) for img in images]

# Save as GIF in the output directory
output_gif_path = os.path.join(output_dir, gif_name)
imageio.mimsave(output_gif_path, frames, duration=0.1)

print(f"GIF saved as {output_gif_path}")
