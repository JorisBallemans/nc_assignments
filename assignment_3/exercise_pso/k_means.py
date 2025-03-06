from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

image = np.array(Image.open("image.png"))
pixels = image.reshape(-1, 3)

kmeans = KMeans(n_clusters = 4)
kmeans.fit(pixels)

cluster_pixels = kmeans.cluster_centers_[kmeans.labels_]
cluster_image = cluster_pixels.reshape(image.shape).astype(np.uint8)

clustered_image_pil = Image.fromarray(cluster_image)
clustered_image_pil.save("k_means.png")

for color in kmeans.cluster_centers_:
    print(f"Color: {np.round(color).astype(int)}")