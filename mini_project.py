from cProfile import label
from statistics import linear_regression, LinearRegression  # project 1

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
# sc=ax.scatter(df['bedrooms'],df['area'],df['price'],c=df['bathrooms'],cmap='viridis',s=50,alpha=0.6)
# plt.colorbar(sc,label='Bathrooms')   # legend for color
#
# ax.set_xlabel('Bedrooms')
# ax.set_ylabel('Area')
# ax.set_zlabel('Price')
# plt.title('home price')
# plt.show()

#--------------------------------------------------------------------------------------------------------

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

a=sns.load_dataset('tips')
df=a
print(df)

x=df[['size']]
y=df['total_bill']

model=linear_model.LinearRegression()
model.fit(x,y)
pre=model.predict([[6]])
print('predicted total bill : ',pre[0])

plt.xlabel('size')
plt.ylabel('total bill')
plt.title('tips')

plt.scatter(df['size'],df.total_bill,marker='*',color='yellow')
plt.plot(df['size'],model.predict(x),color='black')
plt.show()











