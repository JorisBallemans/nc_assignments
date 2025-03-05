import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import pairwise_distances_argmin_min

def quantize_image(image, palette):
    #Flatmap the image
    pixels = image.reshape(-1, 3)
    quantized_pixels = np.zeros_like(pixels)
    
    for i, pixel in enumerate(pixels):
        #Calculate the distance between the pixel and the palette
        distances = np.linalg.norm(palette - pixel, axis=1)

        #Get the closest distance
        closest_color_idx = np.argmin(distances)
        
        #Update the pixel with the closest color
        quantized_pixels[i] = palette[closest_color_idx]
    
    #Unflatmap the image
    quantized_image = quantized_pixels.reshape(image.shape)
    
    return quantized_image

input_img = np.array(Image.open("image.png"))

palette = np.array([
    [175, 198, 114],
    [ 83,  20,  14],
    [185,  49,  40],
    [124, 148,  71]
])

plt.imshow(input_img)
plt.axis("off")
plt.savefig("image_.png", bbox_inches="tight", pad_inches=0)

quantized_img = quantize_image(input_img, palette)

plt.imshow(quantized_img)
plt.axis("off")
plt.savefig("image_quantized_.png", bbox_inches="tight", pad_inches=0)

