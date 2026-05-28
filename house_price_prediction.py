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

# Visualization  Actual value vs Predicted value
plt.scatter(y_test, pre, alpha=0.4, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted House Values')
plt.show()

# Step 1 - Filter first
Q1 = df['total_rooms'].quantile(0.25)
Q3 = df['total_rooms'].quantile(0.75)
IQR = Q3 - Q1
filtered_df = df[df['total_rooms'] < (Q3 + 1.5 * IQR)].copy()

# Step 2 - Then plot
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['total_rooms'],filtered_df['median_house_value'],alpha=0.05,color='blue',s=10)

# Step 3 - Trend line
z = np.polyfit(filtered_df['total_rooms'].values,filtered_df['median_house_value'].values, 1)
p = np.poly1d(z)
sorted_rooms = np.sort(filtered_df['total_rooms'].values)
plt.plot(sorted_rooms, p(sorted_rooms),
         "r--", linewidth=2, label='Trend Line')

plt.xlabel('Total Rooms (per Block)')
plt.ylabel('Median House Value')
plt.title('Total Rooms vs Median House Value')
plt.legend()
plt.tight_layout()
plt.show()

# Plot 3
fig, ax = plt.subplots(figsize=(10, 6))

xgb.plot_importance(model, max_num_features=10, ax=ax)

ax.set_title('Top 10 Important Features', fontsize=14)
ax.set_xlabel('Importance Score', fontsize=12)
ax.set_ylabel('Features', fontsize=12)
ax.tick_params(axis='y', labelsize=11)

plt.tight_layout()
plt.show()





