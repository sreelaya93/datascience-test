# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
#
# df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive (2)\BMW sales data (2010-2024) (1).csv")
# print(df.head())
#
# x=df[['Mileage_KM']]
# y=df['Price_USD']
#
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.2,random_state=42)
#
# model=LinearRegression()
# model.fit(xtrain,ytrain)
# pre=model.predict(xtest)
#
# print('prediction : ',pre)
# print('accuracy : ',model.score(xtest,ytest))
#
# plt.scatter(x,y,marker='*',color='yellow')
# plt.plot(x,model.predict(x))
# plt.xlabel('milage')
# plt.ylabel('price')
#
# plt.show()

# ==========================================================================================

#
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
#
# df=sns.load_dataset('diamonds')
# print(df)
#
# x=df[['carat']]
# y=df['price']
#
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.2,random_state=42)
#
# model=LinearRegression()
# model.fit(xtrain,ytrain)
# pre=model.predict([[.25]])
#
# print('prediction : ',pre[0])
# print('accuracy : ',model.score(xtest,ytest))
#
# sns.regplot(data=df,x='carat',y='price')
# plt.show()

#===========================================================================================

# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
#
# # Load and explore Dataset
#
# df=sns.load_dataset('tips')
# print(df)
#
# # Shows first and last 5 rows
#
# print(df.head())
# print(df.tail())
#
# # Handle missing values
#
# print('missing values : ',df.isnull().sum())
# df['tip']=df['tip'].fillna(df['tip'].mean())
#
# x=df[['total_bill']]
# y=df['tip']
#
# #  Split features and target
#
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=42)
#
# model=LinearRegression()
# model.fit(x_train,y_train)
# pre=model.predict(x_test)
# single_pre=model.predict(pd.DataFrame([[50]],columns=['total_bill']))
#
# # Evaluate the performance
#
# print('prediction for bill=50 : ', single_pre[0])
# print('R2 score : ', model.score(x_test,y_test))
# error=mean_squared_error(y_test,pre)
# print('MSE : ',error)
#
# #     Visualization
#
# sns.regplot(data=df,x='total_bill',y='tip')
# plt.title('Total bill vs Tip')
# plt.xlabel('Total bill')
# plt.ylabel('Tip')
# plt.show()

#==========================================================================================

# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
#
# df = sns.load_dataset('iris')
# df['sepal_length']=df['sepal_length'].fillna(df['sepal_length'].mean())
# print(df.head())
# print(df.isnull().sum())
# x=df[['sepal_length','sepal_width']]
# y=df['species']
#
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)
#
# model=LogisticRegression()
# model.fit(xtrain,ytrain)
# pre=model.predict(xtest)
#
# print('prediction :',pre[0])
# print('accuracy : ',model.score(xtest,ytest))
#
# sns.scatterplot(data=df , x='sepal_length' , y='sepal_width' , hue='species')
# plt.show()

# ================================================================================================





























