import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np
from agent import Agent
import pandas as pd

class PopulationGraph:
    def __init__(self, population, xlabel = "Generation", ylabel = "Population size"):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.historical_data = pd.DataFrame()
        self.add_generation(population)

        self.fig, self.ax = plt.subplots()
        self.plot = self.ax.plot(self.historical_data)[0]

        self.ax.set_xlim(0, 50)
        self.ax.set_ylim(0, 100)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.set_title("Population dynamics")

    def add_generation(self, population: list[Agent]):
        strategies = [agent.strategy.name.lower() for agent in population]
        strategy_counts = pd.Series(strategies).value_counts()
        self.historical_data = pd.concat([self.historical_data, strategy_counts.to_frame().T], ignore_index=True)

    def update_plot(self):
        self.plot.remove()
        self.plot = plt.plot(self.historical_data)[0]
        self.ax.set_xlim(0, len(self.historical_data))
        plt.pause(0.5)
        
