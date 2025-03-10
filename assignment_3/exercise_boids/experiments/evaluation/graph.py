import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory containing the CSV files
csv_dir = '/home/jorisballemans/Documents/Uni/2024-2025/Q3/Natural Computing/nc_assignments/assignment_3/exercise_boids/experiments/evaluation/'

# List to store dataframes
dataframes = []

# Read all CSV files in the directory
for file in os.listdir(csv_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(csv_dir, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Plot avg_nn_distance for each dataframe
plt.figure(figsize=(10, 6))
for df in dataframes:
    plt.plot(df.index / 20, df['avg_nn_distance'])

plt.xlabel("Time steps (t)")
plt.ylabel('Average Nearest Neighbor Distance')
plt.title('Average Nearest Neighbor Distance Over Time')
plt.legend()
plt.savefig("plot.png")
