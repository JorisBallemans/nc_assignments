from agent import Agent
from graph import PopulationGraph
from strategy import Strategy as S
import time
import random

config = {"food": 2}

def main():
    #Initialize the population
    population = []
    population.append(Agent(1, S.COOPERATIVE))
    population.append(Agent(2, S.DOMINANT))
    population.append(Agent(3, S.GREEDY))
    graph = PopulationGraph(population)

    #Generation loop
    while True:
        #Make a dictionary of food
        food_dict = {i: None for i in range(config["food"])}

        #Assign food to agents
        for agent in population:
            food_index = random.randint(0, config["food"] - 1)
            if food_dict[food_index] is None:
                food_dict[food_index] = [agent.id]
            elif len(food_dict[food_index]) < 2:
                food_dict[food_index].append(agent.id)
        print("Food dict:", food_dict)
        return
        #Agents interact (for all cases where food has 2 agents)

        #Update the population
        time.sleep(1)
    
if __name__ == "__main__":
    main()