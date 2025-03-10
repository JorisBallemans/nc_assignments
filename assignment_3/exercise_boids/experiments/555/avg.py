import os
import pandas as pd
import numpy as np

# Path to the eval folder
eval_folder = 'eval/'

# List all CSV files in the eval folder
csv_files = [f for f in os.listdir(eval_folder) if f.endswith('.csv')]

avg_nn_distances = np.zeros(50).tolist()

for csv_file in csv_files:
    df = pd.read_csv(f"{eval_folder}{csv_file}")
    for i in range(1, 51):
        row_time_i = df[df['time'] == i]
        avg_nn_distance = row_time_i['avg_nn_distance'].values[0]
        avg_nn_distances[i-1] += avg_nn_distance

avg_nn_distances = [x / 5 for x in avg_nn_distances]
df = pd.DataFrame({'time': range(1, 51), 'avg_nn_distance': avg_nn_distances})
df.to_csv('avg_nn_distance_000.csv', index=False)