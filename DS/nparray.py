import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)
print(a.shape)
a1=a.reshape(2,3)
print(a1)
print(a1.shape)
a2=np.array([10,20,30,40])
print(a2.shape)
a3=a2.reshape(4,1)
print(a3)

a4=a3.reshape(1,-1)#first param 1 row second -1 calculates no. of columns
print(a4)


a5=np.array([10,20,30,40,50,60])
print(a5.shape)

a6=a5.reshape(1,-1)
print(a6)
print(a6.shape)