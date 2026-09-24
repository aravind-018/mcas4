#prg to create matrix and to compute some of all elements, some of each column and each row
import numpy as np
l=np.arange(1,21).reshape(5,4)
print(np.sum(l))
print(np.sum(l,axis=0))
print(np.sum(l,axis=1))
