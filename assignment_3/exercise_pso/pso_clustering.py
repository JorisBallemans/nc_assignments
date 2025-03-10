import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pso import quantize_image

input_img = np.array(Image.open("image.png"))

def fitness_image(particle, image):
    pixels = image.reshape(-1, 3)
    particle = particle.reshape(-1, 3)
    
    # Assign each pixel to the nearest cluster centroid
    distances = np.linalg.norm(pixels[:, np.newaxis] - particle, axis=2)
    closest_centroids = np.min(distances, axis=1)
    
    # Sum of squared distances to centroids 
    return np.sum(closest_centroids ** 2)


def pso_color_quantization_new(image, w, a1, a2):  
    # N = 200 (arbitrarily chosen) particles representing palettes
    particles = np.random.randint(0, 256, (200, 4, 3))
    velocities = np.zeros_like(particles)
    local_best = np.zeros_like(particles)
    global_best = np.zeros((4, 3))
    
    global_best_fitness = np.inf
    repeat = 0

    # Save for visualization
    global_best_history = []

    # Repeat until no further improvement
    while repeat < 5:
        improved = False

        for i in range(len(particles)):
            r1 = np.random.uniform(0, 1, 3)
            r2 = np.random.uniform(0, 1, 3)
            velocities[i] = (w * velocities[i] + a1 * r1 * (local_best[i] - particles[i]) + a2 * r2 * (global_best - particles[i]))
            # Clip velocities to avoid too large changes
            velocities[i] = np.clip(velocities[i], -50, 50)

        for i in range(len(particles)):
            new_particle = np.clip(particles[i] + velocities[i], 0, 255)
            new_fitness = fitness_image(new_particle, image)
            old_fitness = fitness_image(particles[i], image)

            if new_fitness < old_fitness:
                local_best[i] = new_particle
            
            if new_fitness < global_best_fitness:
                global_best = new_particle
                global_best_fitness = new_fitness
                improved = True

            particles[i] = new_particle

        global_best_history.append((global_best.copy(), global_best_fitness))

        repeat = 0 if improved else repeat + 1

        print(f"Iteration {len(global_best_history)}, Best Fitness: {global_best_fitness}")

    return quantize_image(image, global_best), global_best_history
        
def plot_all_iterations(image, global_best_history, plot_every=10):
    # Filter iterations to plot
    iterations = [(i, palette) for i, (palette, _) in enumerate(global_best_history) if i % plot_every == 0]

    # Set up the figure size dynamically based on the number of iterations
    num_plots = len(iterations)
    fig, axes = plt.subplots(1, num_plots, figsize=(4 * num_plots, 6))
    
    if num_plots == 1:
        axes = [axes]  # Ensure axes is iterable even with 1 plot
    
    for ax, (iteration, palette) in zip(axes, iterations):
        quantized_image = quantize_image(image, palette)
        ax.imshow(quantized_image)
        ax.set_title(f"Iteration {iteration}")
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

best_image, global_best_history = pso_color_quantization_new(input_img, 0.73, 1.5, 1.5)
plot_all_iterations(input_img, global_best_history, plot_every=10)
        
plt.imshow(best_image)
plt.axis("off")
plt.savefig("output.png", bbox_inches="tight", pad_inches=0)

