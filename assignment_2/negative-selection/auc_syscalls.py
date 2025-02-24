import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import os

# Function to compute ROC curve and save the plot
def generate_roc_curve(avg_file, label_file, output_file):
    avgs = np.loadtxt(avg_file)
    labels = np.loadtxt(label_file)
    fpr, tpr, thresholds = metrics.roc_curve(labels, avgs, pos_label=1)
    roc_auc = metrics.auc(fpr, tpr)

    print(fpr)
    print(tpr)
    plt.figure()
    plt.plot(fpr, tpr, color="darkorange", lw=2, label=f"ROC curve (area = {roc_auc:.2f})")
    plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("1 - Specificity")
    plt.ylabel("Sensitivity")
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.legend(loc="lower right")
    plt.savefig(output_file)
    plt.close()

# Loop through all file pairs and generate ROC curves
for i in range(1, 7):
    avg_file = f"output_averages_r{i}.txt"
    label_file = f"syscalls/snd-cert/snd-cert.1.labels"
    output_file = f"roc_curve_r{i}.png"

    if os.path.exists(avg_file) and os.path.exists(label_file):
        generate_roc_curve(avg_file, label_file, output_file)
        print(f"Generated {output_file}")
    else:
        print(f"Files {avg_file} or {label_file} not found. Skipping iteration {i}.")