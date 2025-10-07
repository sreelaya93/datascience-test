#                      plot with x label,y label,title,font dict

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([0,10])
# y=np.array([5,50])
# plt.plot(x,y,marker="*")
#
# font1={'family':'serif','color':'red','size':20}
# font2={'family':'serif','color':'blue','size': 10}
# plt.xlabel('Year',fontdict=font2)
# plt.ylabel('Age',fontdict=font2)
# plt.title('Chart',fontdict=font1)
# plt.show()

#---------------------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([30,200])
# y=np.array([35,250])
# plt.plot(x,y,marker='p')
# plt.show()

#----------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# y=np.array([10,20,9,24])
# x=np.array([2,5,39,5,])
# plt.plot(x,y,marker='*')
# plt.show()

#------------------------------------------------------------------------------------

#                  marker edge color(mec) and marker face color(mfc)

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([30,50,60,78])
# y=np.array([23,45,78,90])
# plt.plot(x,y,marker='*',color='y',mfc='g',ms=10,mec='r')
# plt.show()

#-----------------------------------------------------------------------------------

#                    line style(ls)

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([12,23,3])
# y=np.array([10,22,12])
# plt.plot(x,y,ls=':',color='y',marker='*',ms=10,mfc='b',mec='r')
# plt.show()

#--------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# y=np.array([1,2,3,4])
# y=np.array([2,5,6,7])
# plt.plot(y,y,marker='*')
# plt.show()

#===============================================================================

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([24,34,45,52])
# y=np.array([12,20,30,35])
# plt.plot(y,x,ls="-",color='red',marker='*',mfc='yellow',mec='green',ms=8)
# plt.show()




#------------------------------------------------------------------------------

#                                 grid function

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([30,35,38,39])
# y=np.array([40,45,48,50])
# plt.grid(axis='y',color='black',ls=':')
# plt.xlabel('aaa')
# plt.ylabel('bbb')
# plt.title('Chart',loc="left")
# plt.plot(x,y)
# plt.show()

#============================================================================

# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.array([10,20,30,40])
# y=np.array([30,40,50,60])
# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title('chart1')
#
# x=np.array([30,20,30,20])
# y=np.array([40,50,45,55])
# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.title('chart2')
#
# plt.suptitle('Job Opportunity')
# plt.show()

#==============================================================================

#                     subplot


# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.array([1,2,3,4])
# y=np.array([30,31,32,33])
# plt.subplot(1,3,1)
# plt.plot(x,y,marker='*')
# plt.title('chart 1')
#
# x=np.array([5,6,7,8])
# y=np.array([45,46,47,48])
# plt.subplot(1,3,2)
# plt.plot(x,y,marker='*')
# plt.title('chart 2')
#
# x=np.array([1,5,10,15])
# y=np.array([20,25,20,35])
# plt.subplot(1,3,3)
# plt.plot(x,y,marker='*')
# plt.title('chart 3')
#
# plt.suptitle('CHARTS')
# plt.show()
#============================================================================

#                   scatter

# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.array([1,2,3,4])
# y=np.array([5,6,7,8])
# plt.scatter(x,y)
# plt.show()

#---------------------------------------------------------------------------

#                        bar

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4])
# y=np.array([5,4,6,3])
# plt.bar(x,y,width=.5)
# # plt.barh(x,y,color='yellow')
# plt.show()

#-----------------------------------------------------------

#                     histogram

# import matplotlib.pyplot as plt
# import numpy as np
# a=np.random.normal(170,10,250)
# plt.hist(a)
# plt.show()

#-----------------------------------------------------------

#                  pie plot

# import matplotlib.pyplot as  plt
# import numpy as np

# x=np.array([30,25,25,20])
# mylabels=['a','b','c','d']
# myex=[.2,0,0,0]
# plt.pie(x,labels=mylabels,explode=myex,shadow=True)
# plt.show()

#---------------------------------------------------------------

#                             heatmap

# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df=sns.load_dataset('iris')
# corr=df.corr(numeric_only=True)
#
# sns.heatmap(corr,annot=True,cmap='coolwarm')
# plt.show()





































































































