from agent import Agent
from graph import PopulationGraph
from interaction import INTERACTION_MATRIX, INTERACTION_MATRIX_MINORITY_DEATH
from strategy import Strategy as S
import random

config = {
    "FOOD": 100,
    "COOPERATIVE_COUNT": 20,
    "DOMINANT_COUNT": 5
}

def main():
    NEXT_ID = 1
    #Initialize the population
    population = dict()

    for _ in range(1, config["COOPERATIVE_COUNT"] + 1):
        population[NEXT_ID] = Agent(NEXT_ID, S.COOPERATIVE)
        NEXT_ID += 1
    for _ in range(1, config["DOMINANT_COUNT"] + 1):
        population[NEXT_ID] = Agent(NEXT_ID, S.DOMINANT)
        NEXT_ID += 1
    graph = PopulationGraph(population)
    generation = 0
    
    #Generation loop
    while generation < 100:
        #Make a dictionary of food, assign food to agents
        food_dict = {i: None for i in range(config["FOOD"])}
        food_dict = distribute_food(population, food_dict)
        
        #Agents interact (for all cases where food has 2 agents)
        assign_food_to_agents(population, food_dict)

        #Update the graph
        graph.add_generation(list(population.values()))
        graph.update_plot()

        #Update the population
        new_population, NEXT_ID = update_population(NEXT_ID, population)
            
        for agent in list(new_population.values()):
            agent.set_food(0)
            
        population = new_population
        generation += 1
    return

def update_population(NEXT_ID, population):
    new_population = dict()
    for agent in list(population.values()):
        if random.random() < agent.food:
            new_population[agent.id] = agent
        if random.random() + 1 < agent.food:
            new_population[NEXT_ID] = Agent(NEXT_ID, agent.strategy)
            NEXT_ID += 1
    return new_population, NEXT_ID

def assign_food_to_agents(population, food_dict):
    for food_index in food_dict:
        if food_dict[food_index] is None:
            continue
        if len(food_dict[food_index]) == 2:
            a1 = population[food_dict[food_index][0]]
            a2 = population[food_dict[food_index][1]]
            f1, f2 = INTERACTION_MATRIX_MINORITY_DEATH[(a1.strategy, a2.strategy)]
            print(f"Agent with strategy {a1.strategy} interacts with agent with strategy {a2.strategy} and receives food {f1} and {f2} respectively")
            a1.set_food(f1)
            a2.set_food(f2)
        if len(food_dict[food_index]) == 1:
            a1 = population[food_dict[food_index][0]]
            a1.set_food(2)

def distribute_food(population, food_dict):
    for agent in random.sample(list(population.values()), len(population)):
        food_index = random.randint(0, config["FOOD"] - 1)
        if food_dict[food_index] is None:
            food_dict[food_index] = [agent.id]
        elif len(food_dict[food_index]) < 2:
            food_dict[food_index].append(agent.id)
    return food_dict
    
if __name__ == "__main__":
    main()
