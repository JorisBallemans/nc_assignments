import numpy as np
from scipy.stats import sem, t
import os
import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
from matplotlib import pyplot as plt
import re

folders = [os.path.join("data", d) for d in os.listdir("data") if os.path.isdir(os.path.join("data", d))]

def calculate_mean_ci(data_dir="data", ci=0.95):
    data_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".csv")]
    all_runs = [pd.read_csv(f) for f in data_files]
    average_run = pd.concat(all_runs).groupby(level=0).mean().reset_index(drop=True)
    average_run.columns = [col.capitalize() for col in average_run.columns]
    
    runs_stack = np.stack([df.values for df in all_runs])

    mean_runs = np.mean(runs_stack, axis=0)
    confidence_intervals = sem(runs_stack, axis=0) * t.ppf((1 + ci) / 2, len(all_runs) - 1)
    return average_run, mean_runs, confidence_intervals

color_map = {"Dominant": "r", "Cooperative": "g"}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  

def extract_first_number(s):
    match = re.search(r'\d+', s)
    return int(match.group()) if match else float('inf')

folders.sort(key=extract_first_number)

for idx, folder in enumerate(folders):
    avg_run, mean_runs, ci_runs = calculate_mean_ci(ci=0.95, data_dir=folder)

    x = range(mean_runs.shape[0])
    for index, col_name in enumerate(avg_run.columns):
        color = color_map.get(col_name, None)
        mean_run = mean_runs[:, index]
        ci_run = ci_runs[:, index]
        plt.fill_between(x, mean_run - ci_run, mean_run + ci_run, alpha=0.3, label=f"{col_name} 95% CI", color=color)
        plt.plot(x, mean_run, label=f"{col_name} mean", color=color)

    if avg_run.iloc[0].min() == 5:
        plt.ylim([0, avg_run.iloc[0].sum() * 1.5])
    elif avg_run.iloc[0].min() == 50:
        plt.ylim([50, avg_run.iloc[0].min() * 1.7])
    elif avg_run.iloc[0].min() == 25:
        plt.ylim([20, avg_run.iloc[0].min() * 2])    
    elif avg_run.iloc[0].min() == 500:
        plt.ylim([500, avg_run.iloc[0].min() * 1.55])
    else:
        plt.ylim([avg_run.iloc[0].min(), avg_run.iloc[0].min() * 1.6])
    plt.title("Mean of 50 runs with 95% Confidence Intervals", fontsize=16)
    plt.xlabel("Generation", fontsize=12)
    plt.ylabel("Population size", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)
    # Add label (e.g., 'a', 'b', ...) in the top left corner of the plot
    if idx < len(labels):
        plt.text(0.02, 0.95, labels[idx], transform=plt.gca().transAxes, fontsize=18, fontweight='bold', va='top', ha='left')
    # plt.legend(loc="lower right")
    plt.savefig(f"{folder}_mean_ci_plot.png")
    plt.close()