#                     Sentiment Analysis


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive (1)\IMDB_Dataset_CLEANED.csv")
print(df.head())
print(df.info())

# Missing values
print(df.isnull().sum())

# Text values
print(df.select_dtypes(include='object').columns)

# Encoding
le=LabelEncoder()
df['sentiment']=le.fit_transform(df['sentiment'])

tf=TfidfVectorizer(max_features=5000)

# Features and target
x=tf.fit_transform(df['review'])
y=df['sentiment']

# Split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=42)

# Model selection
model=MultinomialNB()

# Train
model.fit(x_train,y_train)

# Prediction
pred=model.predict(x_test)

# Accuracy
acc=accuracy_score(y_test,pred)
print('accuracy : ',acc)

# Classification Report
print('Report : ', classification_report(y_test,pred))

# Visualization using count map
sns.countplot(x='sentiment',data=df)
plt.title('sentiment')
plt.show()

# confusion matrix
cm=confusion_matrix(y_test,pred)
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()










