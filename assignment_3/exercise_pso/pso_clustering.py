import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#HUH WAT WERKT HIER NIET????
input_img = np.array(Image.open("image.png"))

def fitness(particle, image, i):
    original_pixel = image.reshape(-1, 3)[i]
    return np.sum((original_pixel - particle) ** 2)

def pso_color_quantization(image, w, a1, a2):
    pixels = image.reshape(-1, 3)

    particles = np.random.randint(0, 256, (len(pixels), 3))
    velocities = np.zeros_like(particles)
    local_best = np.zeros_like(particles)
    global_best = np.array([0, 0, 0])
    
    not_happy = True
    j = 10

    while not_happy:
        j -= 1
        print(j)
        if j == 0:
            not_happy = False
        for i in range(len(particles)):
            r1 = np.random.uniform(0, 1, 3)
            r2 = np.random.uniform(0, 1, 3)
            velocities[i] = (w * velocities[i] + a1 * r1 * (local_best[i] - particles[i]) + a2 * r2 * (global_best - particles[i]))
        new_particles = np.zeros_like(particles)
        for i in range(len(particles)):
            new_particles[i] = np.clip(particles[i] + velocities[i], 0, 255)
            fitness_new = fitness(new_particles[i], image, i)
            fitness_old = fitness(particles[i], image, i)
            fitness_global = fitness(global_best, image, i)
            if fitness_new < fitness_old:
                local_best[i] = new_particles[i]
            if fitness_new < fitness_global:
                global_best = new_particles[i]
        particles = new_particles

    return local_best
        
     


particles = pso_color_quantization(input_img, 0.73, 1.5, 1.5)
plt.imshow(particles.reshape(input_img.shape))
plt.savefig("output.png")
