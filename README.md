## Overview
I made this project to learn about decision trees and RandomForestRegressor. The dataset I am using and the idea for this challenge are both from Kaggle. The project uses Python along with libraries like Pandas and scikit-learn.

## Dependencies
- Python
- Pandas: For data manipulation and analysis.
- scikit-learn: For machine learning model building and evaluation.

## Dataset
The dataset, named `House_Rent_Dataset.csv`, includes various attributes of houses and their corresponding rent prices.

## Data Preprocessing Steps
1. **Data Reading**: Utilizing Pandas to read the data.
2. **Data Cleaning**: Dropping rows with missing values to enhance data quality.
3. **Data Splitting**: Dividing the dataset into training (95%) and validation (5%) sets.

## Features
The model considers the following features for rent prediction:
- `BHK`: Number of bedrooms, halls, and kitchens.
- `Size`: The size of the house in square feet.
- `Bathroom`: Number of bathrooms.

## Model Building and Evaluation
1. **Model Creation**: A RandomForestRegressor model is instantiated.
2. **Model Training**: The model is trained on the training set.
3. **Prediction**: The model predicts rent prices on the validation set.
4. **Evaluation**: The Mean Absolute Error (MAE) metric is used for model evaluation.

## Usage Instructions
- Read and preprocess the data.
- Split the data into training and validation sets.
- Define features and the target variable (Rent).
- Train the RandomForestRegressor model.
- Predict and evaluate the model using the validation set.

## Output
- The model outputs predicted rent values.
- The model's performance is measured using the Mean Absolute Error (MAE).

## Conclusion
This project demonstrates a structured approach to predict house rent prices using RandomForestRegressor. The model, trained on key house features, provides a viable solution for rent prediction with an assessable performance metric, MAE.
