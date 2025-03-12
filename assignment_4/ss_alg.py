import random

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
LENGTH = 15
TARGET = "AAAAAAAAAAAAAAA"#"".join(random.choices(ALPHABET, k=LENGTH))
K = 2
POPULATION_SIZE = 200
CROSSOVER_RATE = 1
MUTATION_RATE = 1/LENGTH

class candidate():
    def __init__(self, S, target, string=None):
        self.string = string if string else "".join(random.choices(S, k = len(target)))
        self.fitness = sum([1 for i in range(len(self.string)) if self.string[i] == target[i]])
        self.p_i = 0

    def calculate_p_i(self, total_fitness):
        self.p_i = self.fitness / total_fitness if total_fitness != 0 else 0

    def mutate(self, S, mutation_rate):
        list_string = list(self.string)
        for char in list_string:
            if random.random() < mutation_rate:
                list_string[list_string.index(char)] = random.choice(S)
        self.string = "".join(list_string)

    def __str__(self):
        return f"String: {self.string} with P_i: {self.p_i}"


def string_search(K, S, target, P_c , mu, N):
    population = []
    total_fitness = 0

    # Initialize population
    for _ in range(N):
        population.append(candidate(S, target))

    while True:
        # Calculate total fitness
        total_fitness = sum([c.fitness for c in population])
        
        # Calculate P_i
        for c in population:
            c.calculate_p_i(total_fitness)

        #Gewoon voor de leuk
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
        print(f"Best offspring: {sorted_population[0]}")

        if sorted_population[0] == target:
            print("Found target!")
            return

        #Make new population
        new_population = []
        #Based on p_i
        for _ in range(N - K):
            offspring = random.choices(population, weights=[c.p_i for c in population])[0]
            new_population.append(candidate(S, target, offspring.string))
        #Based on K (random)
        for _ in range(K):
            new_population.append(random.choices(population)[0])
        
        #TODO: Implement random mutations
        for c in new_population:
            c.mutate(S, mu)

        #Update
        population = new_population


if __name__ == "__main__":
    string_search(K, ALPHABET, TARGET, CROSSOVER_RATE, MUTATION_RATE ,POPULATION_SIZE)