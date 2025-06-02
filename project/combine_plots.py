import os
import re
from PIL import Image

def extract_first_number(s):
    match = re.search(r'\d+', s)
    return int(match.group()) if match else float('inf')

data_folder = os.path.join(os.path.dirname(__file__), 'data')
png_files = [f for f in os.listdir(data_folder) if f.lower().endswith('.png')]
png_files.sort(key=extract_first_number)

# Load images
images = [Image.open(os.path.join(data_folder, f)) for f in png_files[:4]]

# Resize all images to the size of the first one using high-quality resampling
w, h = images[0].size
try:
    resample = Image.Resampling.LANCZOS  # Pillow >= 10
except AttributeError:
    resample = Image.LANCZOS  # Pillow < 10

images = [img.resize((w, h), resample=resample) for img in images]

# Create a new blank image for 2x2 grid
combined = Image.new('RGBA', (w*2, h*2), (255,255,255,0))

# Paste images
positions = [(0,0), (w,0), (0,h), (w,h)]
for img, pos in zip(images, positions):
    combined.paste(img, pos)

# Save combined image with maximum quality
combined.save(os.path.join(data_folder, 'combined.png'), quality=100)