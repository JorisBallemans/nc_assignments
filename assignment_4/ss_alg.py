import random, math
import pandas as pd

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
LENGTH = 15
TARGET = "AAAAAAAAAAAAAAA"#"NATURALCOMPUTING"#"".join(random.choices(ALPHABET, k=LENGTH))
K = 2
POPULATION_SIZE = 200
CROSSOVER_RATE = 1
MUTATION_RATE = 1/LENGTH
MAX_GEN = 200

class Candidate():
    def __init__(self, S, target, string=None):
        self.string = string if string else "".join(random.choices(S, k = len(target)))
        self.fitness = self.update_fitness(target)
        self.p_i = 0

    def update_fitness(self, target):
        # fitness function y = x^2 with x the number of matching characters
        return sum([1 for i in range(len(self.string)) if self.string[i] == target[i]]) ** 2

    def calculate_p_i(self, total_fitness):
        self.p_i = self.fitness / total_fitness if total_fitness != 0 else 0

    def mutate(self, S, mutation_rate, target):
        list_string = list(self.string)
        for i, _ in enumerate(list_string):
            if random.random() < mutation_rate:
                list_string[i] = random.choice(S)
        self.string = "".join(list_string)
        self.fitness = self.update_fitness(target)
        

    def __str__(self):
        return f"String: {self.string} with P_i: {self.p_i} with fitness: {self.fitness}"

def shannon_entropy(population : Candidate):


def avg_distance(population :list[Candidate]):
    total = 0
    for i in range(len(population)):
        for j in range(i + 1, len(population)):
            total += sum([1 for k in range(len(population[i].string)) if population[i].string[k] != population[j].string[k]]) ** 2
    return total / (len(population) * (len(population) - 1) / 2)


def shannon_entropy(population :list[Candidate], index):   
    total = 0
    for s in ALPHABET:
        fraction =  sum([1 for c in population if c.string[index] == s]) / len(population)
        total += math.log(fraction) * fraction if fraction > 0 else 0
    return -total

def string_search(K, S, target, P_c , mu, N):
    data = pd.DataFrame(columns=["gen", "avg_distance", "shannon_entropy"])
    population = []
    total_fitness = 0

    # Initialize population
    for _ in range(N):
        population.append(Candidate(S, target))    

    generation = 0

    while generation < MAX_GEN:
        # Calculate metrics
        avg_dist = avg_distance(population)
        shannon_ent = sum([shannon_entropy(population, i) for i in range(len(target))])

        # Add metrics to dataframe
        data = pd.concat([data, pd.DataFrame({
            "gen": [generation],
            "avg_distance": [avg_dist],
            "shannon_entropy": [shannon_ent]
        })], ignore_index=True)

        total_fitness = sum([c.fitness for c in population])
        
        # Calculate P_i
        for c in population:
            c.calculate_p_i(total_fitness)

        # Sort population for debugging
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)

        if sorted_population[0].string == target:
            return data

        # Make new population
        new_population = []
        
        while len(new_population) < N:
            K_population = random.choices(population, k=K)

            K_population

            return

            
            # Crossover or mutate
            if random.random() < P_c:
                # Crossover
                split = random.randint(1, len(target) - 1)
                o1 = Candidate(S, target, p1.string[:split] + p2.string[split:])
                o2 = Candidate(S, target, p2.string[:split] + p1.string[split:])
                new_population.append(o1)
                new_population.append(o2)
        
        # Update
        population = new_population
        generation += 1

    return data

if __name__ == "__main__":
    for mu_rate in [0, 1/LENGTH, 3/LENGTH]:
        for i in range(10):
            results = string_search(K, ALPHABET, TARGET, CROSSOVER_RATE, mu_rate ,POPULATION_SIZE)
            results.to_csv(f"results/{mu_rate}_run_{i}.csv", index=False)

    # string_search(K, ALPHABET, TARGET, CROSSOVER_RATE, MUTATION_RATE ,POPULATION_SIZE) 
