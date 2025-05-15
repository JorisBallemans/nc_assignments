import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np
from agent import Agent
import pandas as pd

class PopulationGraph:
    def __init__(self, xlabel = "Generation", ylabel = "Population size"):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.fig, self.ax = plt.subplots()
        self.historical_data = pd.DataFrame()
        
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.set_title("Population dynamics")
        plt.plot(self.historical_data)
        plt.show()

    def calculate_population(self, population: list[Agent]):
        strategies = [agent.strategy.name.lower() for agent in population]
        strategy_counts = pd.Series(strategies).value_counts().to_dict()
        self.historical_data._append(strategy_counts, ignore_index=True)
        print(self.historical_data)
