import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, precision_recall_curve
def plot_curves(y_true, y_prob):
    """
    Plot ROC and Precision-Recall curves side by side.
    """
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    precision, recall, _ = precision_recall_curve(y_true, y_prob)
    plt.figure(figsize=(12,5))

    # ROC Curve
    plt.subplot(1,2,1)
    plt.plot(fpr, tpr)
    plt.plot([0,1],[0,1],'--')
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    # Precision-Recall Curve
    plt.subplot(1,2,2)
    plt.plot(recall, precision)
    plt.title("Precision-Recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.tight_layout()
    plt.savefig("roc_pr_curves.png")
    plt.show()
