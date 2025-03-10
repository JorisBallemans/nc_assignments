import pandas as pd
import glob
import os

import matplotlib.pyplot as plt

csv_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = glob.glob(os.path.join(csv_dir, '*.csv'))
# csv_files = ["50_10_25_0_0_0_evaluation.csv", "50_10_25_0.5_0.5_0.5_evaluation.csv", "50_10_25_1_1_1_evaluation.csv"]

# print(csv_files)

plt.figure(figsize=(10, 6))

colors = [
    'b', 'g', 'r'
]

for i, file in enumerate(csv_files):
    df = pd.read_csv(file)
    df["time"] = df["time"] * 20
    plt.plot(df["time"], df["avg_nn_distance"], label = file[120:-4],color=colors[i % len(colors)])
    print(f"{colors[i % len(colors)]}: {file}")

# Iterate over each CSV file and extract data
for file in csv_files:
    df = pd.read_csv(file)
    df["time"] = df["time"] * 20
    plt.plot(df["time"], df["avg_nn_distance"])

plt.xlabel('Time in steps (t)')
plt.ylabel('Average Nearest Neighbor Distance')
plt.title('Average Nearest Neighbor Distance over Time')
plt.grid(True)
plt.legend()
plt.savefig("plot.png")