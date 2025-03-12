import matplotlib.pyplot as plt
import pandas as pd

data = [[0.222, 0.333, 0.444], [0.138, 0.310, 0.552], [0.138, 0.310, 0.552], [0.242, 0.293, 0.364]]

df = pd.DataFrame(data, columns=["P(2)", "P(3)", "P(4)"], index=["f(x) = |x|", "f(x) = x^2", "f(x) = 2x^2", "f(x) = x^2+20"])
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

for i, (index, row) in enumerate(df.iterrows()):
    ax = axs[i // 2, i % 2]
    row.plot(kind='pie', ax=ax, autopct='%1.1f%%', textprops={'fontsize': 14})  # Set text size to 14
    ax.set_ylabel('')
    ax.set_title(index, fontsize=16) 


plt.tight_layout()
# plt.title("Pie charts for different fitness functions")
plt.savefig("images/pieplot.png")