import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#Get all files in the data directory
data_files = [os.path.join("data", f) for f in os.listdir("data") if f.endswith(".csv")]

#Calculate the average of all runs
dfs = [pd.read_csv(f) for f in data_files]
average_df = pd.concat(dfs).groupby(level=0).mean().reset_index(drop=True)

# Calculate the standard deviation for each row across all dataframes
std_df = pd.concat(dfs).groupby(level=0).std().reset_index(drop=True)

#Plot the average of all runs
# plt.plot(average_df)
# plt.title("Average of Runs")
# plt.xlabel("Generation")
# plt.ylabel("Population size")
# plt.legend(average_df.columns, loc="lower right")
# plt.show()
print(std_df)
plt.plot(std_df, label="Average + std")
plt.title("Standard Deviation of Runs")
plt.xlabel("Generation")
plt.ylabel("Population size")   
plt.legend(average_df.columns, loc="lower right")
# plt.show()
plt.savefig("average_runs_std.png")