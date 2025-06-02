from agent import Agent
from graph import PopulationGraph
from interaction import INTERACTION_MATRIX, INTERACTION_MATRIX_MINORITY_DEATH
from strategy import Strategy as S
import random

config = {
    "FOOD": 500,
    "COOPERATIVE_COUNT": 100,
    "DOMINANT_COUNT": 400
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
    while generation < 500:
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
            # Get agents
            a1 = population[food_dict[food_index][0]]
            a2 = population[food_dict[food_index][1]]
            # Change strategies of agents based on indirect reciprocity
            image_scoring(a1, a2)
            image_scoring(a2, a1)
            
            # Give food
            a1.interact_with(a2)
            
            # Update information about interaction
            cooperative_a1 = a1.strategy == S.COOPERATIVE
            cooperative_a2 = a2.strategy == S.COOPERATIVE
            a1.update_reputation(cooperative_a1)
            a2.update_reputation(cooperative_a2)
            
        if len(food_dict[food_index]) == 1:
            a1 = population[food_dict[food_index][0]]
            a1.set_food(2)

def image_scoring(a1, a2):
    if a1.reputation > 0:
        a2.set_strategy(S.COOPERATIVE)
        print(f"Agent {a2.id} is now cooperative")
    if a1.reputation < 0:
        a2.set_strategy(S.DOMINANT)
        print(f"Agent {a2.id} is now dominant")

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
