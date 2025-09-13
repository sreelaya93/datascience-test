
#                      numpy array with 20 elements .reshape it 4*5

# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# print(a)
# print(a.reshape(4,5))
# print(a.shape)

#========================================================================

#                     to find mean,meadian,sum,standard deviation

# import numpy as np
# a=np.array([20,40,39,12,46,50,72,11,8,66])
# print('mean of the no : ',a.mean())
# print('sum of the no : ',a.sum())
# print('standard deviation : ',a.std())
# m=np.median(a)
# print('median of the no : ',m)

#========================================================================

#                  to find add,sub,mul,divi of elements in two array

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.add(a,b)
# print('addition : ',c)
# d=np.subtract(a,b)
# print('sub : ',d)
# e=np.multiply(a,b)
# print('mult : ',e)
# f=np.divide(a,b)
# print('dev : ',f)

#========================================================================

#               flatten a 3d array to 1d array

# import numpy as np
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a.reshape(-1))

#==========================================================================

#                5*5 identity matrix

# import numpy as np
# a=np.identity(5)
# print(a)


#============================================================================

#                 extract 2,3 rows

# import numpy as np
# a=np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(a[1:3])

#============================================================================

#              3*3 matrix and matrix multiplication

# import numpy as np
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# c=np.multiply(a,b)
# print(c)

#===========================================================================

#                    pandas

# import pandas as pd
# df=pd.DataFrame({'name':['a','b','c','d','e'],'age':[30,31,34,32,35],'city':['aa','bb','cc','dd','ee'],
#                  'salary':[5900,6000,5500,5200,5100]})
# print(df)

#============================================================================

#                         read csv file

import pandas as pd
df=pd.read_csv(r"C:\Users\Sreelaya K P\Downloads\titanic.csv")
print(df)
print(df.head(10))
print(df[df['Age']>25])
print(df[['Name','Age']])
































