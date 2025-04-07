import random
import statistics

POPULATION_SIZE = 100
MUTATION_PROB = 0.001
K = 2
NUM_ITER = 2000

def import_cities(filename):
    with open(filename) as f:
        return [tuple(map(float, line.split())) for line in f]
    
def fitness(tour):
    # Fitness = 1/sum of distances
    distance = 0
    for i in range(len(tour) - 1):
        distance += ((tour[i][0] - tour[i + 1][0]) ** 2 + (tour[i][1] - tour[i + 1][1]) ** 2) ** 0.5
        return 1/distance
    
def order_crossover(parent1, parent2):
    # Get 2 random cut points
    cut_points = random.sample(range(1, len(parent1) - 1), 2)
    cut_points.sort()
    
    child1 = [0 for _ in range(len(parent1))]
    child2 = [0 for _ in range(len(parent2))]
    
    # Keep what is inbetween cut points
    child1[cut_points[0]:cut_points[1]] = parent1[cut_points[0]:cut_points[1]]
    child2[cut_points[0]:cut_points[1]] = parent2[cut_points[0]:cut_points[1]]
    
    # Get complement from other parent
    parent1_complement = [city for city in parent1 if city not in child2]
    parent2_complement = [city for city in parent2 if city not in child1]
    
    # Fill gaps starting from second cut
    child1[cut_points[1]:] = parent2_complement[:len(child1[cut_points[1]:])]
    child2[cut_points[1]:] = parent1_complement[:len(child2[cut_points[1]:])]
    
    child1[:cut_points[0]] = parent2_complement[len(child1[cut_points[1]:]):]
    child2[:cut_points[0]] = parent1_complement[len(child2[cut_points[1]:]):]
    
    # Check that all points in children are unique
    assert len(child1) == len(set(child1)), "Child 1 not unique"
    assert len(child2) == len(set(child2)), "Child 2 not unique"
    
    return [child1, child2]

def mutate_child(child):
    # Generate 2 random positions and swap them
    positions = random.sample(range(0, len(child)), 2)
    temp = child[positions[0]]
    child[positions[0]] = child[positions[1]]
    child[positions[1]] = temp
    return child

def simple_ea(cities):
    population = [random.sample(cities, k=len(cities)) for _ in range(POPULATION_SIZE)]
    for i in range(NUM_ITER):
        # Generate random tours and calculate fitnesses
        fitnesses = [fitness(p) for p in population]
        total_fitness = sum(fitnesses)
        probabilities = [f/total_fitness for f in fitnesses]
        
        new_population = []
        for _ in range(int(POPULATION_SIZE/2)):
            # Tournament selection for parents with K=2
            parents = []
            for _ in range(2):
                candidates = random.choices(population, probabilities, k=K)
                parents.append(candidates[0] if fitness(candidates[0]) > fitness(candidates[1]) else candidates[1])
                
            # Make children
            children = order_crossover(parents[0], parents[1])
            for child in children:
                if random.random() < MUTATION_PROB:
                    child = mutate_child(child)
                new_population.append(child)
        
        population = new_population
        # Printing to show progress
        print(f'Iteration {i}, best fitness: {max(fitnesses)}, avg fitness: {statistics.mean(fitnesses)}')

cities = import_cities('./file-tsp.txt')
simple_ea(cities)