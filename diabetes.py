#                        Diabetes Prediction

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier


# Load dataset
df = pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive (3)\diabetes.csv")

print(df.head())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Finding text vales
print(df.select_dtypes(include='object').columns)

# Features and target
x = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split data
xtrain, xtest, ytrain, ytest = train_test_split(x, y,test_size=0.2,random_state=42,stratify=y)

# Model
model = XGBClassifier(n_estimators=300,learning_rate=0.05,max_depth=5,subsample=0.8,colsample_bytree=0.8,random_state=42)

# Train
model.fit(xtrain, ytrain)

# Prediction
pred = model.predict(xtest)

# Accuracy
acc = accuracy_score(ytest, pred)

print("Accuracy:", acc)

# Report
print(classification_report(ytest, pred))

# Visualization
#  diabetic vs non-diabetic patients using count plot
sns.countplot(x="Outcome", data=df)
plt.title("Diabetes Outcome Count")
plt.show()       # 0 - non diabetic , 1 - diabetic

#  BMI vs outcome using boxplot
sns.boxplot(x="Outcome", y="BMI", data=df)
plt.title("BMI vs Diabetes")
plt.show()      # diabetic patients have higher BMI





