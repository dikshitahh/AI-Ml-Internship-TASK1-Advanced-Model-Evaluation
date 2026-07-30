# AI-Ml-Internship-TASK1-Advanced-Model-Evaluation

# Advanced Evaluation Metrics for Imbalanced Credit Card Fraud Detection

## Project Overview

This project explores advanced evaluation metrics for highly imbalanced datasets using the Credit Card Fraud Detection dataset. A baseline Random Forest classifier is trained without applying any class balancing techniques to demonstrate why traditional accuracy is not sufficient for evaluating imbalanced classification problems.

The project focuses on evaluating model performance using ROC Curves, Precision-Recall Curves, threshold analysis, and different F1-score averaging methods.

## Business Context

Credit card fraud detection is a critical problem in the banking and financial sector. Fraudulent transactions represent only a very small percentage of all transactions, making the dataset highly imbalanced.

In such scenarios, predicting every transaction as legitimate may still produce very high accuracy while failing to detect actual fraud. Therefore, this project evaluates metrics that better measure the model's ability to identify fraudulent transactions.

## Dataset

Dataset: Credit Card Fraud Detection

The dataset contains anonymized credit card transactions made by European cardholders.

- Total Transactions: 284,807
- Legitimate Transactions: 284,315
- Fraudulent Transactions: 492

Target Variable:

- Class 0 → Legitimate Transaction
- Class 1 → Fraudulent Transaction

Note: The dataset can be downloaded from Kaggle and placed inside the project directory before running the notebook.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Evaluation Metrics

The following evaluation metrics were used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report
- ROC Curve
- ROC-AUC Score
- Precision-Recall Curve
- Average Precision Score
- Macro F1-Score
- Micro F1-Score
- Weighted F1-Score

## Project Workflow

1. Load the Credit Card Fraud Detection dataset.
2. Explore the dataset and verify class imbalance.
3. Split the dataset into training and testing sets.
4. Train a baseline Random Forest classifier.
5. Predict fraud on the test set.
6. Evaluate the model using multiple metrics.
7. Generate ROC and Precision-Recall curves.
8. Analyze precision-recall trade-offs at different thresholds.
9. Compare macro, micro, and weighted F1-scores.
10. Summarize the most suitable evaluation metric for fraud detection.

## Results

The project demonstrates that:

- Accuracy alone is not a reliable metric for highly imbalanced datasets.
- Precision and Recall provide more meaningful insights into fraud detection performance.
- The Precision-Recall Curve is more informative than the ROC Curve for highly imbalanced data.
- Threshold selection significantly affects Precision and Recall.
- Weighted F1-score provides a balanced evaluation while considering class imbalance.

## Conclusion

This project highlights the importance of selecting appropriate evaluation metrics when working with highly imbalanced datasets. For credit card fraud detection, Recall, the Precision-Recall Curve, and the Weighted F1-score provide more meaningful performance evaluation than accuracy alone, helping organizations detect fraudulent transactions more effectively.
