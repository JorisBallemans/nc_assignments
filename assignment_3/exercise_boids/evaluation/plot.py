import pandas as pd
import glob
import os

import matplotlib.pyplot as plt

# csv_dir = os.path.dirname(os.path.abspath(__file__))
# csv_files = glob.glob(os.path.join(csv_dir, '*.csv'))
csv_files = ["50_10_25_0_0_0_evaluation.csv", "50_10_25_0.5_0.5_0.5_evaluation.csv", "50_10_25_1_1_1_evaluation.csv"]

# print(csv_files)

plt.figure(figsize=(10, 6))

# Iterate over each CSV file and extract data
for file in csv_files:
    df = pd.read_csv(file)
    df["time"] = df["time"] * 20
    label = "A: 0, S: 0, C: 0"
    if file[:-10] == "50_10_25_0.5_0.5_0.5_eval":
        label = "A: 0.5, S: 0.5, C: 0.5"
    if file[:-10] == "50_10_25_1_1_1_eval":
        label = "A: 1, S: 1, C: 1"
    plt.plot(df["time"], df["avg_nn_distance"], label=label)

plt.xlabel('Time in steps (t)')
plt.ylabel('Average Nearest Neighbor Distance')
plt.title('Average Nearest Neighbor Distance over Time')
plt.grid(True)
plt.legend()
plt.savefig("plot.png")