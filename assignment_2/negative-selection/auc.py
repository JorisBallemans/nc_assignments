import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc
import os

# Function to compute ROC curve and save the plot
def generate_roc_curve(english_file, tagalog_file, output_file):
    english_scores = np.loadtxt(english_file)
    tagalog_scores = np.loadtxt(tagalog_file)

    english_label = np.zeros(len(english_scores))
    tagalog_label = np.ones(len(tagalog_scores))

    scores = np.concatenate((english_scores, tagalog_scores))
    distinct_scores = np.unique(scores)

    labels = np.concatenate((english_label, tagalog_label))
    zipped_scores_labels = list(zip(scores, labels))

    zipped_scores_labels.sort(key=lambda x: x[0])

    sensitivity = [1]
    specificity = [0]

    for distinct_score in distinct_scores:
        tp = sum(1 for score, label in zipped_scores_labels if score >= distinct_score and label == 1)
        fn = sum(1 for score, label in zipped_scores_labels if score < distinct_score and label == 1)
        tn = sum(1 for score, label in zipped_scores_labels if score < distinct_score and label == 0)
        fp = sum(1 for score, label in zipped_scores_labels if score >= distinct_score and label == 0)

        sensitivity.append(tp / (tp + fn) if (tp + fn) > 0 else 0)
        specificity.append(tn / (tn + fp) if (tn + fp) > 0 else 0)

    sensitivity.append(0)
    specificity.append(1)
    roc_auc = auc(1 - np.array(specificity), np.array(sensitivity))

    plt.figure()
    plt.plot(1 - np.array(specificity), np.array(sensitivity), color="darkorange", lw=2, label=f"ROC curve (area = {roc_auc:.2f})")
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
for i in range(2, 6):
    english_file = f"english_r{i}_output.txt"
    tagalog_file = f"xhosa_r{i}_output.txt"
    output_file = f"roc_curve_r{i}_xhosa.png"

    if os.path.exists(english_file) and os.path.exists(tagalog_file):
        generate_roc_curve(english_file, tagalog_file, output_file)
        print(f"Generated {output_file}")
    else:
        print(f"Files {english_file} or {tagalog_file} not found. Skipping iteration {i}.")