import random
import matplotlib.pyplot as plt

LENGTH = 100
MUTATION_RATE = 1/LENGTH
ITERATIONS = 1500

def fitness(x, y):
    return sum([1 for i in range(len(x)) if x[i] == y[i]]) 

def random_bitseq(length):
    return [random.randint(0, 1) for _ in range(length)]

def copy_invert(x, mutation_rate):
    x_m = x.copy()
    for i in range(len(x)):
        if random.random() < mutation_rate:
            x_m[i] = 1 - x_m[i]
    return x_m

def plot_fitness(data, filename):
    # plt.figure(num=1, clear=True)
    # plt.set_xlim()
    plt.grid(True)
    plt.xlabel("Iterations")
    plt.ylabel("Fitness")
    plt.plot(data)
    plt.title("Fitness of the best individual over time")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.savefig(f"images/{filename}.png")

def experiment_1():
    fitness_scores = []
    goal_seq = [1] * LENGTH
    x = random_bitseq(LENGTH)
    for i in range(ITERATIONS):
        x_m = copy_invert(x, MUTATION_RATE)
        if fitness(x_m, goal_seq) > fitness(x, goal_seq):
            x = x_m
        fitness_scores.append(fitness(x, goal_seq))
    return fitness_scores

def experiment_2():
    fitness_scores = []
    goal_seq = [1] * LENGTH
    x = random_bitseq(LENGTH)
    for i in range(ITERATIONS):
        x_m = copy_invert(x, MUTATION_RATE)
        x = x_m
        fitness_scores.append(fitness(x, goal_seq))
    return fitness_scores
    

if __name__ == "__main__":
    data = experiment_1()
    plot_fitness(data, "experiment_1")
    data = experiment_2()
    plot_fitness(data, "experiment_2")
