from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def fitness_image(particle, image):
    pixels = image.reshape(-1, 3)
    particle = particle.reshape(-1, 3)
    
    # Assign each pixel to the nearest cluster centroid
    distances = np.linalg.norm(pixels[:, np.newaxis] - particle, axis=2)
    closest_centroids = np.min(distances, axis=1)
    
    # Sum of squared distances to centroids 
    return np.sum(closest_centroids ** 2)

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
    
print(f"Fitness: {fitness_image(kmeans.cluster_centers_, image)}")