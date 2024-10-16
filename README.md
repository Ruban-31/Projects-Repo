This project aims to predict the sales of products in various Big Mart outlets using regression models. The dataset contains information such as product details, outlet identifiers, and sales figures. The goal is to build models that can accurately forecast the sales based on the provided features.

Project Overview
In this project, I have explored multiple regression techniques to predict sales. These include:

Linear Regression
Random Forest Regressor
XGBoost Regressor
Key Metrics:
Best Accuracy: 59% (using XGBoost)
Mean Absolute Error (MAE): 528
Dataset
The dataset used for this project comes from a Big Mart sales dataset, typically found in competitions like Kaggle. It consists of:

Target Variable:
Item_Outlet_Sales: The sales of the product in a specific outlet.
Features:
Item_Identifier: Unique product ID.
Item_Weight: Weight of the product.
Item_Fat_Content: Whether the product is low-fat or regular.
Item_Visibility: The percentage of total display area of all products allocated to this particular product.
Item_Type: The category of the product.
Item_MRP: Maximum Retail Price of the product.
Outlet_Identifier: Unique store ID.
Outlet_Establishment_Year: The year the outlet was established.
Outlet_Size: Size of the outlet (small/medium/large).
Outlet_Location_Type: Type of city in which the outlet is located.
Outlet_Type: Whether the outlet is a grocery store or a supermarket.
Project Workflow
Data Preprocessing:

Handled missing values (e.g., imputation of missing weights).
Categorical encoding (e.g., label encoding for Outlet_Identifier).
Feature scaling for numerical features.
Feature engineering: Created new features, such as Outlet_Age.
Model Building:

Built and trained models using:
Linear Regression: A simple model that assumes a linear relationship between features and target.
Random Forest Regressor: An ensemble model that builds multiple decision trees and averages their predictions.
XGBoost Regressor: A gradient boosting technique that optimizes model performance by reducing bias and variance.
Model Evaluation:

Evaluation metrics used:
Mean Absolute Error (MAE)
R-squared (R²)
Best results were achieved with the XGBoost Regressor, yielding:
R² = 0.59
MAE = 528
