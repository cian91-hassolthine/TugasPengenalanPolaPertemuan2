import numpy as np
# mengubah dari 1D menjadi matrik 2D 
a = np.arange(1,21,1)
c = a.reshape((4,5))
print(c)