import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#Reading rent prices csv
houses_file_path='House_Rent_Dataset.csv'
houses_data=pd.read_csv(houses_file_path)

#Drop all dataframe rows that are missing values to clean up data.
houses_data=houses_data.dropna(axis=0)

#Glimpse and summary of input data
print(houses_data.describe())
print(houses_data.head())

#Now, let us split off our training set from our validation set
train, test = train_test_split(houses_data, test_size=0.05)

#Pick our targets
trainY=train.Rent
validateY = test.Rent

#Pick our features
house_features=['BHK','Size','Bathroom']
trainX=train[house_features]
validateX=test[house_features]


print("\nCreating model...")
forest_model = RandomForestRegressor(random_state=1)
print("Model created!")


print("\nTraining model...")
forest_model.fit(trainX,trainY)

print("Model trained!")

print("\nModel generating predictions...")
predictions = forest_model.predict(validateX)
print("Predictions generated!")

print("\nThe MAE of the model is:", mean_absolute_error(validateY,predictions),"\n")