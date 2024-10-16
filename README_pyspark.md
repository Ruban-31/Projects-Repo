# Cardiovascular Disease Prediction using SVM with PySpark and Python

## Project Overview
This project aims to compare the execution time and performance of machine learning model training using **PySpark** and **Python** (without Spark) on a 
large cardiovascular dataset. The dataset contains **70,000 rows** of cardiovascular health records, and the task is to predict whether a
person will experience a cardiac arrest based on various health features.

The machine learning model used is a **Support Vector Machine (SVM)**, and the achieved accuracy is approximately **72%**.

## Dataset
The dataset consists of cardiovascular health data including features such as:
- Age
- Gender
- Blood pressure
- Cholesterol level
- Smoking habits
- Physical activity level
- BMI (Body Mass Index)
- Other relevant health parameters


## Methods Used
1. **Support Vector Machine (SVM)** for binary classification of cardiovascular arrest risk.
2. **Feature Scaling**:
   - **MinMax Scaler**: Scales features to a fixed range (usually [0, 1]).
   - **Standard Scaler**: Standardizes features by removing the mean and scaling to unit variance.

### Impact of Scaling on Model Accuracy
- **MinMax Scaler**: Resulted in smoother convergence of the SVM model but gave a slightly lower accuracy compared to standard scaling.
- **Standard Scaler**: Led to better separation of data in feature space, improving the model's performance and contributing to the final accuracy of approximately **72%**.

## Comparison: PySpark vs. Python
### PySpark
- **Execution Time**: Faster on large datasets, especially when distributed across multiple nodes.
- **Scalability**: Handles larger datasets more efficiently.
- **Accuracy**: The final model trained with PySpark achieved an accuracy close to **72%**, matching the result of the Python implementation.

### Python (Without Spark)
- **Execution Time**: Slower due to single-threaded execution.
- **Scalability**: Limited by the size of memory and computational power of the machine.
- **Accuracy**: Similar accuracy of around **72%** but with longer training times.


### Results:
Accuracy: Approximately 72%.
Execution Time: PySpark executed the model training significantly faster than Python, especially on larger datasets.
Feature Scaling: Standard scaling led to better performance compared to MinMax scaling.

### Conclusion: 
This project demonstrates the effectiveness of PySpark in handling large datasets and reducing execution time while maintaining similar accuracy 
to traditional Python-based machine learning. It also highlights the impact of different feature scaling techniques on SVM model performance.
