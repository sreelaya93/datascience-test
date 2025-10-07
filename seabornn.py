
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.displot([0,1,2,3,4,5])
# plt.show()

#------------------------------------------------------

# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.displot([10,20,30,40,50,],kind='kde')
# plt.show()

#--------------------------------------------------------

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.array([10,20,30,40])
# y=np.array([12,60,25,36])
# sns.displot([x,y])
# plt.show()

#-------------------------------------------------------------------------

#                tips datafram

# import matplotlib.pyplot as plt
# import seaborn as sns
# df=sns.load_dataset('tips')
# print(df.head())
# sns.scatterplot(y='tip',x='sex',data=df,hue='time',palette='rainbow')
# plt.show()

#==================================================================================

#           Relational plot -> lineplot and scatterplot

#print(df['species'])
# sns.lineplot(x='sepal_length',y='sepal_width',data=df,hue='species')
#sns.scatterplot(x='sepal_length',y='sepal_width',data=df,hue='species',palette='rainbow')
# plt.grid(ls=':',color='black')
#plt.show()

#------------------------------------------------------------------------------------

#         Categorical plot -> barplot and boxplot and violin plot

# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df=sns.load_dataset('iris')
# sns.barplot(x='species',y='sepal_length',data=df,hue='species',saturation=.1)
#sns.boxplot(x='sepal_length',y='sepal_width',data=df,hue='species',palette='deep')
# sns.violinplot(x='species',y='sepal_width',data=df,hue='species')
#plt.show()

#------------------------------------------------------------------------------------------

#                        distribution plot -> hist plot, kde plot


# import matplotlib.pyplot as plt
# import seaborn as sns
# df=sns.load_dataset('iris')
# sns.histplot(data=df,x='sepal_length',kde=True,hue='species')
# plt.show()

#================================================================================

#                       kde plot (kernel destini estimate plot

# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # df=sns.load_dataset('tips')
#
# # sns.kdeplot(data=df,x='total_bill' )
#
# df=sns.load_dataset('iris')
#
# plt.show()

#---------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df=sns.load_dataset('iris')
# sns.lineplot(x='sepal_length',y='sepal_width',data=df,hue='species')
#
#
# plt.title('Iris Flowers')
#
# plt.show()

#---------------------------------------------------------------------------------





