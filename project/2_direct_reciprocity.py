from agent import Agent
from graph import PopulationGraph
from strategy import Strategy as S
import random
import pandas as pd
import argparse
import os

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-f",   "--food",   type=int, help = "Defines the count of food", default=100)
    parser.add_argument("-g",   "--greedy", type=int, help = "Defines the count of greedy agents", default=50)
    parser.add_argument("-c",   "--coop",   type=int, help = "Defines the count of cooperative agents", default=50)
    parser.add_argument("-gc",  "--gen",    type=int, help = "Defines the count of generations", default=200)
    parser.add_argument("-r",   "--runs",   type=int, help = "Defines the count of runs", default=0)
    args = parser.parse_args()

    #DATA GENERATION MODE
    if args.runs > 0:
        print("Data generation mode activated.")
        print("No graph will be shown.")
        print("Bleep bloop, I am a robot.")
        print(f"Running {args.runs} runs with {args.coop} cooperative and {args.greedy} greedy agents for {args.gen} generations with {args.food} food each.")
        
        os.makedirs(f"data/f_{args.food}_c_{args.coop}_g_{args.greedy}_gen_{args.gen}", exist_ok=True)
        
        interactions = pd.DataFrame()

        for iter_run in range(args.runs):
            historical_data = pd.DataFrame()
            total_interactions = 0
            total_changed_interactions = 0
            NEXT_ID = 1
            #Initialize the population
            population = dict()

            for _ in range(1, args.coop + 1):
                population[NEXT_ID] = Agent(NEXT_ID, S.COOPERATIVE)
                NEXT_ID += 1
            for _ in range(1, args.greedy + 1):
                population[NEXT_ID] = Agent(NEXT_ID, S.DOMINANT)
                NEXT_ID += 1
            generation = 0
            
            #Generation loop
            while generation < args.gen:
                #Make a dictionary of food, assign food to agents
                food_dict = {i: None for i in range(args.food)}
                food_dict = distribute_food(population, food_dict, args.food)
                
                #Agents interact (for all cases where food has 2 agents)
                rep_interactions, changed_interactions = assign_food_to_agents(population, food_dict)
                total_interactions += rep_interactions
                total_changed_interactions += changed_interactions
                
                #Generate historical data
                strategies = [agent.strategy.name.lower() for agent in list(population.values())]
                strategy_counts = pd.Series(strategies).value_counts()
                all_strategies = [s.name.lower() for s in S]
                for strategy in all_strategies:
                    if strategy not in strategy_counts:
                        strategy_counts[strategy] = 0
                historical_data = pd.concat([historical_data, strategy_counts.to_frame().T], ignore_index=True)

                #Update the population
                new_population, NEXT_ID = update_population(NEXT_ID, population)
                    
                for agent in list(new_population.values()):
                    agent.set_food(0)
                    
                population = new_population
                generation += 1
            print(f"Run {iter_run + 1} completed.")
            historical_data.to_csv(f"data/f_{args.food}_c_{args.coop}_g_{args.greedy}_gen_{args.gen}/run_{iter_run}.csv", index=False)
            interactions = pd.concat([interactions, pd.DataFrame({"run": iter_run + 1, "rep_interactions": total_interactions, "changed_interactions": total_changed_interactions}, index=[0])], ignore_index=True)
        interactions.to_csv(f"data/f_{args.food}_c_{args.coop}_g_{args.greedy}_gen_{args.gen}/interactions.csv", index=False)
        return

    #NORMAL MODE
    else:
        NEXT_ID = 1
        #Initialize the population
        population = dict()

        for _ in range(1, args.coop + 1):
            population[NEXT_ID] = Agent(NEXT_ID, S.COOPERATIVE)
            NEXT_ID += 1
        for _ in range(1, args.greedy + 1):
            population[NEXT_ID] = Agent(NEXT_ID, S.DOMINANT)
            NEXT_ID += 1
        graph = PopulationGraph(population)
        generation = 0
        
        #Generation loop
        while generation < args.gen:
            #Make a dictionary of food, assign food to agents
            food_dict = {i: None for i in range(args.food)}
            food_dict = distribute_food(population, food_dict, args.food)
            
            #Agents interact (for all cases where food has 2 agents)
            rep_interactions, changed_interactions = assign_food_to_agents(population, food_dict)
            # print(f"Generation {generation}: {rep_interactions} rep interactions, {changed_interactions} changed interactions")

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
    changed_interactions = 0
    rep_interactions = 0
    for food_index in food_dict:
        if food_dict[food_index] is None:
            continue
        if len(food_dict[food_index]) == 2:
            # Get agents
            a1 = population[food_dict[food_index][0]]
            a2 = population[food_dict[food_index][1]]
            
            a1_strategy = a1.strategy
            a2_strategy = a2.strategy
            # Change strategies of agents based on direct reciprocity
            rep_interaction, changed_interaction = tit_for_tat(a1, a2)
            
            changed_interactions += changed_interaction
            rep_interactions += rep_interaction
            
            # Give food
            a1.interact_with(a2)
            
            # Update information about interaction
            a1.update_positive_last_interaction(a2)
            a2.update_positive_last_interaction(a1)
            
            # Give agents original strategy back
            a1.set_strategy(a1_strategy)
            a2.set_strategy(a2_strategy)
        if len(food_dict[food_index]) == 1:
            a1 = population[food_dict[food_index][0]]
            a1.set_food(2)
    return rep_interactions, changed_interactions

def tit_for_tat(a1, a2):
    strategy_interactions = 0
    rep_interactions = 0
    if a1.get_positive_last_interaction(a2) is not None:
        rep_interactions += 1
        positive = a1.get_positive_last_interaction(a2)
        new_strategy = S.COOPERATIVE if positive else S.DOMINANT
        if a1.strategy != new_strategy:
            a1.set_strategy(new_strategy)
            strategy_interactions += 1

    if a2.get_positive_last_interaction(a1) is not None:
        rep_interactions += 1
        positive = a2.get_positive_last_interaction(a1)
        new_strategy = S.COOPERATIVE if positive else S.DOMINANT
        if a2.strategy != new_strategy:
            a2.set_strategy(new_strategy)
            strategy_interactions += 1

    return rep_interactions, strategy_interactions

def distribute_food(population, food_dict, food_count):
    for agent in random.sample(list(population.values()), len(population)):
        food_index = random.randint(0, food_count - 1)
        if food_dict[food_index] is None:
            food_dict[food_index] = [agent.id]
        elif len(food_dict[food_index]) < 2:
            food_dict[food_index].append(agent.id)
    return food_dict
    
if __name__ == "__main__":
    main()
