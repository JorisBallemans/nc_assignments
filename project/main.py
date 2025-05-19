from agent import Agent
from graph import PopulationGraph
from strategy import Strategy as S
import time
import random

config = {"food": 100}

def main():
    #Initialize the population
    population = []
    population.append(Agent(1, S.COOPERATIVE))
    population.append(Agent(2, S.COOPERATIVE))
    population.append(Agent(3, S.COOPERATIVE))
    population.append(Agent(4, S.DOMINANT))
    population.append(Agent(5, S.DOMINANT))
    population.append(Agent(6, S.DOMINANT))
    population.append(Agent(7, S.GREEDY))
    population.append(Agent(9, S.DOMINANT))
    population.append(Agent(10, S.DOMINANT))
    graph = PopulationGraph(population)
    generation = 0
    next_id = len(population) + 1

    #Generation loop
    while generation < 100:
        #Make a dictionary of food
        food_dict = {i: None for i in range(config["food"])}

        #Assign food to agents
        for agent in population:
            food_index = random.randint(0, config["food"] - 1)
            if food_dict[food_index] is None:
                food_dict[food_index] = [agent.id]
            elif len(food_dict[food_index]) < 2:
                food_dict[food_index].append(agent.id)
        # print(food_dict)
        #Agents interact (for all cases where food has 2 agents)
        for food_index in food_dict:
            # print(food_dict[food_index])
            if food_dict[food_index] is None:
                # print("skipped")
                continue
            if len(food_dict[food_index]) == 2:
                agent1 = find_agent_in_population(food_dict[food_index][0], population)
                agent2 = find_agent_in_population(food_dict[food_index][1], population)
                agent1.interact_with(agent2)
                # print("interacted: ", agent1.food, agent2.food)
            if len(food_dict[food_index]) == 1:
                agent1 = find_agent_in_population(food_dict[food_index][0], population)
                agent1.set_food(2)
                # print("Food for agent: ", agent1.food)
        
        #Update the graph
        graph.add_generation(population)
        graph.update_plot()
        #Update the population
        new_population = []
        for i in range(len(population)):
            if population[i].food == 0.5 and random.random() > 0.5:
                new_population.append(population[i])
            if population[i].food == 1:
                new_population.append(population[i])
            if population[i].food == 1.5 and random.random() > 0.5:
                new_population.append(population[i])
                new_population.append(Agent(next_id, population[i].strategy))
                next_id += 1
            if population[i].food == 2:
                new_population.append(population[i])
                new_population.append(Agent(next_id, population[i].strategy))
                next_id += 1
            
        for agent in new_population:
            agent.set_food(0)
            
        population = new_population
        generation += 1
    return

def find_agent_in_population(agent_id, population):
    for agent in population:
        if agent.id == agent_id:
            return agent
    
if __name__ == "__main__":
    main()