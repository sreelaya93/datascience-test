#                        Customer churn prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive\WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.head())

# Finding null values
print(df.isnull().sum())

# Finding text vales
print(df.select_dtypes(include='object').columns)

# Encoding
le=LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Features and target
x=df.drop('Churn',axis=1)
y=df['Churn']

# Split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=42)

# Model selection
model=RandomForestClassifier(class_weight='balanced',n_estimators=200,max_depth=10,random_state=42)

# Train
model.fit(x_train,y_train)

# Prediction
pred=model.predict(x_test)

# Accuracy
acc=accuracy_score(y_test,pred)
print('Accuracy : ',acc)

print(classification_report(y_test,pred))

# Visualization
# Count plot
sns.countplot(x='Churn',data=df) # 0 - no churn , 1 - churn
plt.title('customer churn distribution')
plt.show()

# Boxplot
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()










