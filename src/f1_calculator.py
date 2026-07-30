from sklearn.metrics import f1_score
def calculate_f1_scores(y_true, y_pred):
    """
    Calculate Macro, Micro and Weighted F1 Scores.
    """
    macro = f1_score(y_true, y_pred, average="macro")
    micro = f1_score(y_true, y_pred, average="micro")
    weighted = f1_score(y_true, y_pred, average="weighted")
    print("Macro F1    :", round(macro,4))
    print("Micro F1    :", round(micro,4))
    print("Weighted F1 :", round(weighted,4))

if __name__ == "__main__":
    print("Import this module into your notebook and call calculate_f1_scores(y_true, y_pred).")
