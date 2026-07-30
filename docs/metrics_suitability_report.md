# Metric Suitability Report for Imbalanced Credit Card Fraud Detection

## 1. Introduction

Credit card fraud detection is a real-world classification problem where fraudulent transactions are extremely rare compared to legitimate transactions. In this project, the Credit Card Fraud Detection dataset was used to evaluate a baseline Random Forest classifier without applying any class balancing techniques.
The objective of this project is to understand how different evaluation metrics behave on highly imbalanced datasets and determine which metrics are most appropriate for business decision-making.

## 2. Dataset Overview

The dataset contains credit card transactions made by European cardholders.

- Total Transactions: 284,807
- Legitimate Transactions (Class 0): 284,315
- Fraudulent Transactions (Class 1): 492

This means that only about **0.17%** of all transactions are fraudulent, making the dataset highly imbalanced.

## 3. Why Accuracy is Misleading

Accuracy measures the percentage of correctly classified samples.
Although the model achieved a very high accuracy, accuracy alone is not a reliable metric for fraud detection. Since the majority of transactions are legitimate, a model could classify almost every transaction as genuine and still achieve very high accuracy while failing to detect fraudulent transactions.
Therefore, additional evaluation metrics are necessary.

## 4. ROC Curve Analysis

The Receiver Operating Characteristic (ROC) Curve illustrates the relationship between the True Positive Rate (Recall) and the False Positive Rate at different classification thresholds.
The ROC-AUC score summarizes the overall classification performance.
A ROC-AUC score close to 1 indicates that the model can effectively distinguish fraudulent transactions from legitimate ones.
The plotted ROC curve remained well above the diagonal reference line, indicating strong classification performance.

## 5. Precision-Recall Curve Analysis

For highly imbalanced datasets, the Precision-Recall (PR) Curve provides a more informative evaluation than the ROC Curve.
Precision measures how many predicted fraud cases are actually fraudulent.
Recall measures how many actual fraud cases were successfully detected.
Since fraudulent transactions are rare, maintaining high recall is extremely important because missing fraud can result in financial losses.
The Precision-Recall curve clearly demonstrated the trade-off between precision and recall as the classification threshold changes.

## 6. Threshold Analysis

Different classification thresholds were evaluated to observe changes in precision and recall.

- Lower thresholds increased recall by identifying more fraudulent transactions but also increased false positives.
- Higher thresholds improved precision by reducing false alarms but missed some fraudulent transactions, lowering recall.

This demonstrates that selecting an appropriate threshold depends on the specific business objective.
For fraud detection, a lower threshold is often preferred because detecting fraudulent transactions is generally more important than avoiding additional investigations.

## 7. Comparison of Macro, Micro, and Weighted F1 Scores

Three averaging methods were used to evaluate model performance.

### Macro F1 Score

Macro F1 calculates the F1-score independently for each class and assigns equal importance to both legitimate and fraudulent transactions.
This metric highlights performance on minority classes but does not account for class imbalance.

### Micro F1 Score

Micro F1 aggregates all predictions before computing the F1-score.
For binary classification, Micro F1 is usually very similar to overall accuracy.

### Weighted F1 Score

Weighted F1 calculates the F1-score for each class and weights them according to the number of samples in each class.
Since the dataset is highly imbalanced, Weighted F1 provides a more balanced overall evaluation while considering the distribution of the classes.

## 8. Most Suitable Evaluation Metric

For the credit card fraud detection problem, Recall is the most important evaluation metric because failing to detect fraudulent transactions may result in financial losses.
The Precision-Recall Curve is also highly suitable because it focuses specifically on the minority (fraud) class and provides a clearer picture of classifier performance than accuracy alone.
Weighted F1-score serves as a useful overall metric because it balances precision and recall while accounting for the class imbalance.

## 9. Conclusion

This project demonstrated that traditional accuracy is not sufficient for evaluating models trained on highly imbalanced datasets.
ROC Curve, Precision-Recall Curve, Recall, and Weighted F1-score provide a more meaningful assessment of fraud detection performance.
The threshold analysis further showed that increasing recall generally reduces precision, illustrating the trade-off that organizations must consider based on their business priorities.
For financial fraud detection, maximizing recall while maintaining acceptable precision is the preferred strategy because detecting fraudulent transactions is more valuable than minimizing false alarms.
