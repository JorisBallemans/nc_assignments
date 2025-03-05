import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

input_img = np.array(Image.open("image.png"))

def fitness(particle, image, i):
    original_pixel = image.reshape(-1, 3)[i]
    distance = np.linalg.norm(particle - original_pixel)
    return distance**2

def pso_color_quantization(image, w, a1, a2):
    pixels = image.reshape(-1, 3)

    particles = np.random.randint(0, 256, (len(pixels), 3))
    velocities = np.zeros_like(particles)
    local_best = np.zeros_like(particles)
    global_best = 0
    
    not_happy = True
    j = 100

    while not_happy:
        j -= 1
        print(j)
        if j == 0:
            not_happy = False
        for i in range(len(particles)):
            r1 = np.random.uniform(0, 1, 3)
            r2 = np.random.uniform(0, 1, 3)
            velocities[i] = (w * velocities[i] + a1 * r1 * (local_best[i] - particles[i]) + a2 * r2 * (global_best - particles[i]))
        for i in range(len(particles)):
            new_particles = np.zeros_like(particles)
            new_particles[i] = particles[i] + velocities[i]
            if fitness(new_particles[i], image, i) < fitness(particles[i], image, i):
                local_best[i] = new_particles[i]
            if fitness(new_particles[i], image, i) < fitness(global_best, image, i):
                global_best = new_particles[i]

    return local_best


particles = pso_color_quantization(input_img, 0.7, 1.5,  1.5)
plt.imshow(particles.reshape(input_img.shape))
plt.savefig("output.png")
