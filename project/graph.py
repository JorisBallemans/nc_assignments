import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np
from agent import Agent
import pandas as pd
import sys

class PopulationGraph:
    def __init__(self, population, xlabel="Generation", ylabel="Population size"):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.historical_data = pd.DataFrame()
        self.add_generation(list(population.values()))

        self.fig, self.ax = plt.subplots()
        self.colors = ['red', 'green', 'blue']
        
        self.plot_lines = []
        for color, column in zip(self.colors, self.historical_data.columns):
            line, = self.ax.plot([], [], label=column, color=color)
            self.plot_lines.append(line)

        self.ax.set_xlim(0, 50)
        self.ax.set_ylim(0, 100)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.set_title("Population dynamics")
        self.ax.legend()

    def add_generation(self, population: list[Agent]):
        strategies = [agent.strategy.name.lower() for agent in population]
        strategy_counts = pd.Series(strategies).value_counts()
        self.historical_data = pd.concat([self.historical_data, strategy_counts.to_frame().T], ignore_index=True)

    def update_plot(self):
        x_data = range(len(self.historical_data))
        
        for line, column in zip(self.plot_lines, self.historical_data.columns):
            line.set_data(x_data, self.historical_data[column].values)
        print(self.historical_data)
        self.ax.set_xlim(0, len(self.historical_data))
        self.ax.relim()
        self.ax.autoscale_view()
        plt.pause(0.2)

