#write a program to create a 2D array using numpy and print it
import numpy as np
a=np.array([[2,4,1],[5,6,2],[7,1,2]])
print(a)

p=np.array([[3,1,2],[4,5,6],[9,8,6]])
print(p)
#addition 
c=a+p
print(c)

d=a-p
print(d)

m=a*p
print(m)

m2=np.dot(a,p)
print(m2)

trans_a=np.transpose(a)
print(trans_a)
trans_p=np.transpose(p)
print(trans_p)

deter=np.linalg.det(a)
print(deter)

print(a)
inv=np.linalg.inv(a)
print(inv)

maxx=np.max(a)
print("max:",maxx)

minn=np.min(a)
print("min:",minn)

trace=np.trace(a)
print("trace:",trace)

#write a python program 1)to read number of rows and columns for matrix1
#2)create matrix1 
#3)to read number of rows and columns for matrix2
#4)create matrix2
#5)find dot prod mat1,mat2,trace mat1,mat2  ,rank of mat1,matr2,  trans of m1,m2, determinant of m1,m2 ,inverse of m
