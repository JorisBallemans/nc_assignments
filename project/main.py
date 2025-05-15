from agent import Agent
from graph import PopulationGraph
from strategy import Strategy as S

def main():
    population = []
    population.append(Agent(1, S.COOPERATIVE))
    population.append(Agent(2, S.DOMINANT))
    population.append(Agent(3, S.GREEDY))
    graph = PopulationGraph()
    graph.calculate_population(population)
    
if __name__ == "__main__":
    main()