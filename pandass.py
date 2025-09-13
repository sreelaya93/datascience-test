# from pydoc import describe
#
# #                                          pandas with dataframe
#
#
# # import pandas as pd
# # emp={'id':[1,2,3,4],'name':['a','b','c','d'],'age':[10,10,11,23],'salary':[1000,2000,3000,4000]}
# # df=pd.DataFrame(emp)
# # print(df)
#
# #---------------------------------------------------------------------------------------------------------
#
# # import pandas as pd
# # s={'name':['a','b','c'],'roll':[1,2,3],'mark':[10,20,30]}
# # d=pd.DataFrame(s)
# # #print(d)
# # #print(d['roll'])
# # print(d['name'])
#
# # ---------------------------------------------------------------------------------------------------------------
#
# # import pandas as pd
# # emp=[('p',1,1000),('q',2,2000),('r',3,3000),('s',4,4000)]
# # d=pd.DataFrame(emp,columns=['name','id','salary'])
# # print(d)
#
# #------------------------------------------------------------------------------------
#
# # import pandas as pd
# # s=[{'name':'a','id':1},{'name':'b','id':2},{'name':'c','id':3}]
# # d=pd.DataFrame(s)
# # print(d)
#
# # -------------------------------------------------------------------------------------------------
#
# # import pandas as pd
# # stud={'name':['laya','kala','diya','chiya'],'mark':[30,334,32,31]}
# # d=pd.DataFrame(stud)
# # print(d)
#
# # import pandas as pd
# # v={'veg':['tomato','onion','potato','chilly'],'quantity':[1,1,1,1],'price':[20,32,24,15]}
# # d=pd.DataFrame(v)
# # print(d)
#
# #-----------------------------------------------------------------------------------------------------
# #                                 Series
#
# # import  pandas as pd
# # a=[10,20,30,40,50]
# # i=['a','b','c','d','e']
# # f=pd.Series(a,index=i)
# # print(f)
# # or
# # for i in f:
# #     print(i)
#
# #-------------------------------------------------------------------------------------
#
# # import pandas as pd
# # a={'name':['laya','mridul','diya','dev'],'age':[31,37,4,8]}
# # f=pd.DataFrame(a)
# # print(f)
#
# #----------------------------------------------------------------------------------------------
#
# #                         csv file reading
#
# # import pandas as pd
# #
# #
# # df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv")
# # # df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv",na_values=['n.a.','not available'])
# # #df.shape
# # #print(df.head(3))
# # #print(df.tail())
# # #df.tail(3)
# # print(df)
#
# #----------------------------------------------------------------------------------------------------------------------------------------------
#
# import pandas as pd
# a={'name':['aa','bb','cc','dd'],'mark':[10,20,15,23]}
# df=pd.DataFrame(a)
# print(df)
# print(df['mark'].max())
# print(df['mark'].min())
# print(df['mark'].mean())
# print(df['mark'].sum())
# print(df['mark'].std())
#print(df.describe(thing=1))
#print(df[df.mark>15])
# new_df=df.fillna(0)
# print(new_df)
# print(df.head(2))
# print(df.tail(1))

#
# #--------------------------------------------------------------------------------------------------------------
#
# # import pandas as pd
# # df=pd.read_excel(r"C:\Users\Sreelaya K P\Downloads\FSI-2023-DOWNLOAD.xlsx",header=1,names=['country','job',])
# # print(df)
#
# #----------------------------------------------------------------------------------------------------------------
# #
# # import pandas as pd
# # a={'name':['aaa','bbb','ccc','ddd','eee'],'age':[10,15,13,12,16],'city':['pdl','pnr','chm','knr','krl']}
# # df=pd.DataFrame(a)
# # print(df)
#
# #-------------------------------------------------------------------------------------------------------------------

#                                 dataframe with csv files

# import pandas as pd
# df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\titanic (1).csv")

# print(df.head(10))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# cm=df[['name','age']]
# print(cm)
#print(df[df.age>30])
# print(df.drop_duplicates(inplace=True))
# print(df.drop('survived',axis=1))
# df['salary']=1000
# print(df)
# df['age']=df['age'].fillna(df['age'].mean())
# print(df['age'])

#---------------------------------------------------------------------------------------------------




























