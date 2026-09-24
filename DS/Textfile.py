#prg to save a given array to a text file and load it 
import numpy as np
l=np.arange(1,20)
np.savetxt("text.txt",l,fmt="%d")#saving text file
print(np.loadtxt("text.txt",dtype=int))
# np.loadtxt()#loading 