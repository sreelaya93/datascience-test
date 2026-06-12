             #    California House price prediction

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Load dataset
df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive (1)\housing.csv")

print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)
print(df.isnull().sum())

# Fill missing values
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
print(df.isnull().sum())

# Finding text values
print(df.select_dtypes(include='object').columns)

# Encode
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Use ALL features
x = df.drop('median_house_value', axis=1)
y = df['median_house_value']

# Split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# Model selection
model=XGBRegressor(n_estimators=500,learning_rate=0.05,max_depth=6,random_state=42)

# Train
model.fit(x_train,y_train)

# Prediction
pre=model.predict(x_test)

# Evaluation
mse = mean_squared_error(y_test, pre)
rmse = math.sqrt(mse)

print('R2 Score : ', model.score(x_test, y_test))
print('MSE      : ', mse)
print('RMSE     : ', rmse)

# Visualization using xgb
xgb.plot_importance(model)
plt.title('Feature Importance')
plt.xlabel('Score')
plt.ylabel('Features')
plt.show()

# Scatter plot
plt.scatter(y_test, pre, alpha=0.5)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.show()








