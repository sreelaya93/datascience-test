
#                    LinearRegression
#                   project 1


# Data visualization project using numpy,pandas,matplotlib and seaborn

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# a={'maths':[49,76,55,40,89,99,68,65,69,88],'science':[64,84,93,43,44,35,77,75,89,71],
#    'english':[96,61,81,92,56,99,69,88,78,53],'history':[66,44,79,81,84,43,35,43,81,55]}
# i=['stud1','stud2','stud3','stud4','stud5','stud6','stud7','stud8','stud9','stud10']
# stud=pd.DataFrame(a,index=i)
# print(stud)
# avg_mark=stud.mean()
# print(avg_mark)
#
# #     bar plot
#
# c=['red','blue','green','yellow']
# plt.title('Average Marks per Subject')
# plt.bar(avg_mark.index,avg_mark.values,color=c)
# #plt.show()
#
# #   line plot  ( performance trend for first 3 students )
#
# a=stud.head(3).T
# a.plot(kind='line',marker='*')
# plt.show()
#
# #           subject contribution over all average ( pie plot )
#
# plt.pie(x=avg_mark.values,labels=avg_mark.index,autopct='%1f%%',startangle=90,explode=[.2,0,0,0],shadow=True)
# plt.show()
#
# #    distribution of marks across subject
#
# plt.figure(figsize=[1,2])
# sns.boxplot(data=stud)
# plt.show()
#
# #     correlation heat map
#
# plt.figure(figsize=[12,8])
# sns.heatmap(data=stud)
# plt.show()
#
# #       using pair plot
#
# sns.pairplot(data=stud)
# plt.show()

#-----------------------------------------------------------------------------------------------------------------------

#                              Scikit learn - Linear regression


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import linear_model
#
# # Load data
# df = pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive\Housing.csv")
#
# # Scatter plot (first 5 rows)
# a = df.head()
# plt.xlabel('Area (sqft)')
# plt.ylabel('Price (US $)')
# plt.scatter(x=a.area, y=a.price, marker='*', color='green')
# plt.show()
#
# # Linear Regression
# model = linear_model.LinearRegression()
# model.fit(df[['area']], df['price'])
#
# # Print model parameters
# print('Coefficient (slope):', model.coef_)
# print('Intercept:', model.intercept_)
#
# # Predict for specific values
# print('Predicted prices for 8000 & 8500 sqft:', model.predict(np.array([[8000], [8500]])))
#
# # Regression line with all data
# plt.xlabel('Area (sqft)')
# plt.ylabel('Price (US $)')
# plt.scatter(x=df['area'], y=df['price'], marker='*', color='green')
# plt.grid(color='yellow')
# plt.plot(df['area'], model.predict(df[['area']]), color='black')
# plt.show()

#-----------------------------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import linear_model
#
# df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive\Housing.csv")
#
#
# plt.xlabel('area')
# plt.ylabel('price')
# plt.title('house pricing')
#
#
# plt.scatter(x=df.area,y=df.price,marker='*')
# plt.show()
#
# reg_model=linear_model.LinearRegression()
# reg_model.fit(df[['area']],df.price)
#
# print(reg_model.coef_)
# print(reg_model.intercept_)
#
# reg_model.predict([[8000],[8500]])
#
# pre=reg_model.predict(df[['area']])
#
# plt.xlabel('area')
# plt.ylabel('price')
# plt.scatter(df.area,df.price,marker='*',color='red')
# plt.plot(df.area,pre,color='black')
# plt.show()

#-------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
#
# a={'area':[1000,1500,2000,2500,3000],'price':[150000,200000,250000,280000,310000]}
# df=pd.DataFrame(a)
# print(df)
#
# x=df[['area']]
# y=df['price']
#
# model=LinearRegression()
# model.fit(x,y)
# predicted_price=model.predict([[2200]])
# print('predicted price for 2200:',predicted_price[0])
#
# plt.scatter(x=df['area'],y=df['price'],marker='*',color='green')
# plt.plot(df['area'],model.predict(x),color='black')
# plt.show()

#-------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import linear_model
#
# data=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive\Housing.csv")
# print(data.head())
#
# median_=data.bedrooms.median()
# data.bedrooms=data.bedrooms.fillna(median_)
# model=linear_model.LinearRegression()
# model.fit(data[['area']],data.price)
# model.predict([[8000]])
# pre=model.predict(data[['area']])
#
# plt.xlabel('area')
# plt.ylabel('price')
# plt.scatter(data.area,data.price,marker='*',color='green')
# plt.plot(data.area,pre,color='black')
#
# plt.show()

#------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.pyplot import viridis
# from sklearn.linear_model import LinearRegression
# from mpl_toolkits.mplot3d import Axes3D
#
# df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive\Housing.csv")
# print(df)
# x=df[['area','bedrooms','bathrooms']]
# y=df['price']
#
# model=LinearRegression()
# model.fit(x,y)
#
# # 3d scatter plot
#
# fig=plt.figure()
# ax=fig.add_subplot(111,projection='3d')
#
# # scatter plot (use color to represent the 3rd  x  variable )
#
# sc=ax.scatter(df['bedrooms'],df['area'],df['price'],c=df['bathrooms'],cmap='viridis',s=30,alpha=0.5)
# plt.colorbar(sc,label='Bathrooms')   # legend for color
#
# ax.set_xlabel('Bedrooms')
# ax.set_ylabel('Area')
# ax.set_zlabel('Price')
# plt.title('home price')
# plt.show()

#--------------------------------------------------------------------------------------------------------

# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import linear_model
#
# a=sns.load_dataset('tips')
# df=a
# print(df)
#
# x=df[['size']]
# y=df['total_bill']
#
# model=linear_model.LinearRegression()
# model.fit(x,y)
# pre=model.predict([[6]])
# print('predicted total bill : ',pre[0])
#
# plt.xlabel('size')
# plt.ylabel('total bill')
# plt.title('tips')
#
# plt.scatter(x,y,marker='*',color='yellow')
# plt.plot(x,model.predict(x),color='black')
# plt.show()

#--------------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# from sklearn import linear_model
#
# df=sns.load_dataset('diamonds')
# print(df)
#
# a=df['price'].mean()
# df['price']=df['price'].fillna(a)
# print(df['price'])
#
# x=df[['carat']]
# y=df['price']
#
# model=linear_model.LinearRegression()
# model.fit(x,y)
# pre=model.predict([[0.23]])
# print('predicted price : ',pre[0])
#
# plt.xlabel('carat')
# plt.ylabel('price')
# plt.title('Diamonds')
#
# plt.scatter(df['carat'],df['price'],marker='*',color='green')
# plt.plot(df['carat'],model.predict(x),color='black')
# plt.show()

#------------------------------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt
# from  sklearn import linear_model
#
# a={'town':['monroe township','monroe township','monroe township','west windsor','west windsor','west windsor','robbinsville','robbinsville','robbinsville'],
#     'area':[2600,3000,3200,3600,4000,2600,2800,3300,3600],'price':[550000,565000,610000,680000,725000,585000,615000,650000,710000]}
# data=pd.DataFrame(a)
# print(data)
#
# dummies=pd.get_dummies(data.town)
# merge=pd.concat([data,dummies],axis=1)
# merge=merge.drop(['town'],axis=1)
# print(merge)
#
# x=merge.drop(['price'],axis=1)
# y=merge.price
# model=linear_model.LinearRegression()
# model.fit(x,y)
# pre=model.predict([[3000,0,0,1]])
# print('predicted price : ',pre[[0]])
# model.score(x,y)
#
# plt.scatter(data.area,data.price,marker='*',color='green')
# plt.plot(data.area,model.predict(x),color='red')
# plt.show()

#--------------------------------------------------------------------------------------------------
 #                        Linear Regression
# import pandas as pd
# from sklearn import linear_model
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
#
# df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive (2)\BMW sales data (2010-2024) (1).csv")
# print(df)
# print(df.columns)
#
# x=df[['Mileage_KM','Year']]
# y=df[['Price_USD']]
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.3)
#
# model=linear_model.LinearRegression()
# model.fit(xtrain,ytrain)
# pre=model.predict(xtest)
# print(ytest)
# print('predicted price = ',pre)
# error=mean_squared_error(pre,ytest)
# print('error : ',error)

#--------------------------------------------------------------------------------------------------

# import pandas as pd
# from sklearn import linear_model
# from sklearn.model_selection import train_test_split
#
# df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\archive (2)\BMW sales data (2010-2024) (1).csv")
# #print(df)
# x=df[['Mileage_KM']]
# y=df['Price_USD']
#
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
#
# model=linear_model.LinearRegression()
# model.fit(x_train,y_train)
# pre=model.predict(x_test)
# print('Actual price : ',y_test.values)
# print('predicted price : ',pre)
# print('accuracy : ',model.score(x_test,y_test))

#----------------------------------------------------------------------------------------

  #                                Logistic Regression

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# data=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\insurance_data.csv")
# x=data[['age']]
# y=data['bought_insurance']
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
#
# plt.scatter(x,y,marker='*',color='red')
# plt.xlabel('age')
# plt.ylabel('insurance')
# plt.show()
#
# model=LogisticRegression()
# model.fit(x_train,y_train)
# y_pre=model.predict(x_test)
#
# print(y_test)
# print(model.score(x_test,y_test))

#----------------------------------------------------------------------------------------------

#                                           Decision Tree

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import tree
# from sklearn.preprocessing import LabelEncoder
#
#
# data={'age':['young','young','middle','senior','senior','middle'],
#     'income':['high','medium','high','medium','low','low'],
#     'buys_com':['no','no','yes','yes','no','yes']
#     }
# df=pd.DataFrame(data)
# print(df)

# #        convert categorical data to numeric
#
# le_age=LabelEncoder()
# le_income=LabelEncoder()
# le_buy=LabelEncoder()
#
# df['age_n']=le_age.fit_transform(df['age'])
# df['income_n']=le_income.fit_transform(df['income'])
# df['buy_n']=le_buy.fit_transform(df['buys_com'])
#
# #        define features(x) and target(y)
#
# x=df[['age_n','income_n']]
# y=df['buy_n']
#
# #        create and train the decision tree model
#
# model=tree.DecisionTreeClassifier(criterion='entropy')
# model.fit(x,y)
#
# #         make a prediction (eg:- predict for a new person (age=senior,income=medium) )
#
# pre=model.predict([[le_age.transform(['senior'])[0],le_income.transform(['medium'])[0]]])
#
# print('prediction : ',le_buy.inverse_transform(pre)[0])
#
# #          visualize the tree
#
# plt.figure(figsize=(8,6))
# tree.plot_tree(model,feature_names=['age','income'],class_names=le_buy.classes_,filled=True)
# plt.show()

#------------------------------------------------------------------------------------------------------------------



#                                     Decision Tree

# import pandas as pd
# from sklearn import tree
# from sklearn.preprocessing import LabelEncoder
# data=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\Salary.csv")
# print(data)
# inputs=data.drop(['salary_more_then_100k'],axis='columns')
# target=data['salary_more_then_100k']
# le_data=LabelEncoder()
# company_l=le_data.fit_transform(inputs['company'])
# job_l=le_data.fit_transform(inputs['job'])
# degree_l=le_data.fit_transform(inputs['degree'])
# inputs['company']=company_l
# inputs['job']=job_l
# inputs['degree']=degree_l
# model=tree.DecisionTreeClassifier()
# model.fit(inputs,target)
# print('accuracy : ',model.score(inputs,target))
# print('prediction : ',model.predict([[2,0,0]]))
# print(inputs)

#-------------------------------------------------------------------------------------------


# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# iris=load_iris()
# from sklearn.svm import SVC
# dir(iris)
# print(iris.feature_names)
# data=pd.DataFrame(iris.data,columns=iris.feature_names)
# data['targets']=iris.target
# print(iris.target_names)
# data['flower_name']=data.targets.apply(lambda x:iris.target_names[x])
# data0=data[data.targets==0]
# data1=data[data.targets==1]
# data2=data[data.targets==2]
#
# plt.scatter(data0['sepal length (cm)'],data0['sepal width (cm)'],marker='*', color='green')
# plt.show()
# plt.scatter(data1['sepal length (cm)'],data1['sepal width (cm)'],marker='*', color='green')
# plt.show()
# plt.scatter(data2['sepal length (cm)'],data2['sepal width (cm)'],marker='*', color='green')
# plt.show()
#
# x=data.drop(['targets','flower_name'],axis='columns')
# y=data.targets
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
# model=SVC()
# model.fit(xtrain,ytrain)
# print(model.score(xtest,ytest))
# print(model.predict(xtest))


#---------------------------------------------------------------------------------------------------------

#                     support vector machine

# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report
#
# # Sample dataset (emails & labels: 1 for spam, 0 for not spam)
# emails = ["Win a lottery now", "Meeting scheduled for tomorrow", "Get discount on medicines",
#           "Your bank account is updated", "Urgent: Update your password"]
# labels = [1, 0, 1, 0, 1]  # Spam = 1, Not Spam = 0
#
# # Convert text data into numerical form using TF-IDF Vectorizer
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(emails)
#
# # Splitting dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
#
# # Train the SVM model
# model = SVC(kernel='linear', C=1.0)
# model.fit(X_train, y_train)
#
# # Make predictions
# y_pred =model.predict(X_test)
#
# # Evaluate performance
# accuracy = accuracy_score(y_test, y_pred)
# report = classification_report(y_test, y_pred)
#
# print("Model Accuracy:", accuracy)
# print("Classification Report:\n", report)

#-----------------------------------------------------------------------------------------------

#                               Random Forest

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# from sklearn.datasets import load_digits
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# digits=load_digit()
# for i in range(3):
#     plt.matshow(digits.images[i])
# print(digits.target)
# print(digits.target_names)
#
# data=pd.DataFrame(digits.data)
# data['target']=digits.target
# x=data.drop(['target'],axis=1)
# y=data.target
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.2)
# model=RandomForestClassifier()
# model.fit(xtrain,ytrain)
# print(model.score(xtest,ytest))
# y_truth=ytest
# y_predicted=model.predict(xtest)
# from sklearn.metrics import confusion_matrix
# cm=confusion_matrix(y_truth,y_predicted)
# plt.figure(figsize=(10,7))
# seaborn.heatmap(cm,annot=True)
# plt.show()

#------------------------------------------------------------------------

# import pandas as ps
# from seaborn import load_dataset
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import seaborn as sns
#
# titanic_data=sns.load_dataset('titanic')
# titanic_data=titanic_data.dropna(subset=['survived'])
# print(titanic_data)
# x=titanic_data[['pclass','sex','age','sibsp','parch','fare']]
# y=titanic_data['survived']
# x['sex']=x['sex'].map({'female':0,'male':1})
# x['age']=x['age'].fillna(x['age'].median())
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.2,random_state=42)
# rf_classifier=RandomForestClassifier(n_estimators=100,random_state=42)
# rf_classifier.fit(xtrain,ytrain)
# y_pred=rf_classifier.predict(xtest)
# accuracy=accuracy_score(ytest,y_pred)
# classification_rep=classification_report(ytest,y_pred)
#
# print('accuracy:{accuracy :.2f}')
# print('\n classification report : \n',classification_rep)
# sample=xtest.iloc[0:1]
# prediction=rf_classifier.predict(sample)

#-------------------------------------------------------------------------------

# import pandas as pd
# from pyexpat import features
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_iris
# from sklearn.metrics import accuracy_score, classification_report
#
# data=load_iris()
# x=data.data
# y=data.target
#
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.25,random_state=42)
# model=RandomForestClassifier(n_estimators=150,max_depth=5,random_state=42)
# model.fit(xtrain,ytrain)
# pre=model.predict(xtest)
#
# print('accuracy : ',accuracy_score(ytest,pre))
# print('classification report : ',classification_report(ytest,pre))
#
# #feature important
# feature_imp=pd.DataFrame({'feature':data.feature_names,
#                           'importance':model.feature_importances_}).sort_values(by='importance',ascending=False)
# print(feature_imp)
#
# # sample prediction
#
# sample=[[5.0,3.5,1.3,0.2]]
# prediction=model.predict(sample)
# print('predicted species : ',data.target_names[prediction][0])

#----------------------------------------------------------------------------------------------------------------------

#                               K Nearest Neighbour

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
#
# data={'maths':[20,30,40,50,60,70,80,90],
#       'science':[25,35,45,55,65,75,85,95],
#       'result':['fail','fail','fail','fail','pass','pass','pass','pass']
#       }
#
# df=pd.DataFrame(data)
# print(df)
#
# x=df[['maths','science']]
# y=df['result']
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
#
# model=KNeighborsClassifier(n_neighbors=3)
# model.fit(xtrain,ytrain)
# pre=model.predict(xtest)
#
# print('prediction : ',pre)
# print('actual : ',ytest)
# print('accuracy : ',model.score(xtest,ytest))

#-----------------------------------------------------------------------------------

#                           k means clustering algorithm (Unsupervised Learning Algorithm)

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
#
# data={'age':[20,21,22,23,24,25],
#       'income':[2000,2100,2200,2300,2400,2500]
#       }
# df=pd.DataFrame(data)
# print(df)
#
# xtrain,xtest=train_test_split(df,test_size=0.2,random_state=1)
#
# model=KMeans(n_clusters=2,random_state=1)
# model.fit(xtrain)
# pre=model.predict(xtest)
# print('test data : ',pre)
#
# plt.scatter(df['age'],df['income'],c=model.predict(df),marker='*')
# plt.title('K means clustering')
# plt.xlabel('age')
# plt.ylabel('income')
# plt.show()









