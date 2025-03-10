import pandas as pd
import numpy as np

data = pd.read_csv("50_10_25_1_1_1.csv")

data["norm_vec_x"] = data["x"] / np.sqrt(np.power(data["x"],2) + np.power(data["y"],2))
data["norm_vec_y"] = data["y"] / np.sqrt(np.power(data["x"],2) + np.power(data["y"],2))

grouped_time = data.groupby("time")

order_values = []

for time in range(1, 51):
    time_step = grouped_time.get_group(time)
    sum_norm_vec_x = time_step["norm_vec_x"].sum()
    sum_norm_vec_y = time_step["norm_vec_y"].sum()
    order = np.sqrt(np.power(sum_norm_vec_x, 2) + np.power(sum_norm_vec_y, 2)) / 50
    order_values.append({"time": time, "order": order})

order_df = pd.DataFrame(order_values)
print(order_df)
