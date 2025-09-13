#                                   matplotlib

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([0,10])
# y=np.array([0,50])
# plt.plot(x,y)
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

import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,2,3,4])
y=np.array([2,5,6,7])
plt.plot(y,y,marker='*')
plt.show()

