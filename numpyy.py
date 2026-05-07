# import numpy as np
# a=np.array([1,2,3,4,5])
# print(a)
# print(type(a))

#-------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(type(a))

# --------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a)
#print(a[0,1,2])
# print(type(a))

# ---------------------------------------------------------------------------------------

# import numpy as np
# a=np.array(10)
# b=np.array([1,2,3,4])
# c=np.array([[1,2],[3,4]])
# d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(c.ndim)
# print(b.ndim)
# print(d.ndim)
# print(a.ndim)

# ----------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([1,2,3,4],ndmin=5)
# print(a)
# print('number of dimensions : ',a.ndim)

#  -----------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([1,2,3,4,5])
# print(a)
# print(a[3])

# -----------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a[0,1])

# # -----------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a)
# print(a[0:2,2:4])

# # ---------------------------------------------------------------------------------------------
#
# import numpy as np
# a=np.array(('apple','r'))
# print(a)
# print(a.dtype)
# #
# # -----------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([1.1,2.2,3.3,4.4])
# print(a.astype('i'))
# print(a)


# #---------------------------------------------------------------------------------------
#
#  import numpy as np
#  a=np.array([[1,2,3],[4,5,6]])
#  print(a)
#  print(a.dtype)

# ------------------------------------------------------------------------------------------
                                   #  base
#  import numpy as np
#  a=np.array([1,2,3])
#  x=a.copy()
#  y=a.view()
#  print(a)
#  print(x.base)
# print(y.base)

 # ----------------------------------------------------------------------------------------------
                                    #shape
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.shape)

#---------------------------------------------------------------------------------------------
#                                   shape
# import numpy as np
# a=np.array([1,2,3,4], ndmin=5)
# print(a)
# #print(a.shape)
# print(a.ndim)

#---------------------------------------------------------------------------------------
                                  #reshape
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9,10])
# print(a)
# print(a.reshape(2,5))

# ----------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(' 1 d array : ',a)
# print(a.reshape(2,3,2))

# ---------------------------------------------------------------------------------
                                   #flattening

# import numpy as np
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a)
# print(a.reshape(-1))

# -------------------------------------------------------------------------------------------
                            #iterating 2D array
# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# for i in a:
#     for j in i:
#         print(j)

# _____________________________________________________________________________________
                             #iterating 3D array

# import numpy as np
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a)
# for i in a:
#     for j in i:
#         for k in j:
#             print(k)

#---------------------------------------------------------------------
#                            nditer
# import numpy as np
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# for i in np.nditer(a):
#     print(i)

#-------------------------------------------------------------------------------

# import numpy as np
# a=np.array([[1,2],[3,4]])
# for i in np.nditer(a, flags=['buffered'], op_dtypes='S'):
#     print(i)

#-------------------------------------------------------------------------------

#                                 joining
# concatination

# import numpy as np
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.concatenate((a,b))
# print(c)

# stack

# import numpy as np
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.stack((a,b))
# print(c)
# c=np.hstack((a,b))
# print(c)
# c=np.dstack((a,b))
# print(c)
# c=np.vstack((a,b))
# print(c)
#
#-----------------------------------------------------------------

#                      enumeration

# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# for i,j in np.ndenumerate(a):
#     print(i,j)

#-------------------------------------------------------------------

#                        split array

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# b=np.split(a,3)
# print(b)
# b=np.array_split(a,2)
# print(b)
# c=np.array_split(a,5)
# print(c)

#---------------------------------------------------------------------

#                         search

# import numpy as np
# a=np.array([1,5,2,5,3,5])
# b=np.where(a==5)
# print(a)
# print(b)

#                         search even no and odd no

# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9,10])
# b=np.where(a% 2==0)
# print(a)
# print(b)
# c=np.where(a%2==1)
# print(c)

#---------------------------------------------------------------------------------------
#                                      sort
# import numpy as np
# a=np.array([1,4,6,2,3,8])
#b=np.sort(a)
#print(a)
#print(b)
# c=np.array([[9,5,8,7],[4,7,3,5]])
# d=np.sort(c)
# print(c)
# print(d)

#------------------------------------------------------------------------------------

#                                   searchsorted

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# print(a)
# b=np.searchsorted(a,6)
# print(b)
# c=np.searchsorted(a,3)
# print(c)
# p=np.array([1,3,5,7])
# q=np.searchsorted(p,[2,4,6])
# print(q)
# print(p)

#----------------------------------------------------------------------------------

#          random matrix replace values graterthan 0.5 with 1
#            and rest with 0

# import numpy as np
# from numpy import random
# a=np.random.rand(4,4)
# a=np.where(a>0.5,1,0)
# print(a)

#===================================================================






















