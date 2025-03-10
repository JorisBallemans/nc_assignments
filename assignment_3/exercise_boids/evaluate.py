import pandas as pd
import numpy as np
import os

def analyse(input_file):
    data = pd.read_csv(input_file)

    data["norm_vec_x"] = data["x"] / np.sqrt(np.power(data["x"],2) + np.power(data["y"],2))
    data["norm_vec_y"] = data["y"] / np.sqrt(np.power(data["x"],2) + np.power(data["y"],2))

    grouped_time = data.groupby("time")

    order_values = []

    for time in range(1, 51): 
        time_step = grouped_time.get_group(time)
        min_distances = []
        for i, boid in time_step.iterrows():
            distances = []
            for j, other_boid in time_step.iterrows():
                if i != j:
                    distance = np.sqrt((boid["x"] - other_boid["x"])**2 + (boid["y"] - other_boid["y"])**2)
                    distances.append(distance)
            min_distance = min(distances) if distances else np.nan
            min_distances.append(min_distance)
        sum_norm_vec_x = time_step["norm_vec_x"].sum()
        sum_norm_vec_y = time_step["norm_vec_y"].sum()
        order = np.sqrt(np.power(sum_norm_vec_x, 2) + np.power(sum_norm_vec_y, 2)) / 50
        avg_nn_distance = sum(min_distances) / len(min_distances)
        order_values.append({"time": time, "order": order, "avg_nn_distance": avg_nn_distance})

    order_df = pd.DataFrame(order_values)
    order_df.to_csv(f"{input_file[:-4]}_evaluation.csv", index=False)

input_folder = "experiments/555"
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

for csv_file in csv_files:
    analyse(f"{input_folder}/{csv_file}")

