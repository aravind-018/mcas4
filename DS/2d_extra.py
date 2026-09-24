#write a python program 1)to read number of rows and columns for matrix1
#2)create matrix1 
#3)to read number of rows and columns for matrix2
#4)create matrix2
#5)find dot prod mat1,mat2,trace mat1,mat2  ,rank of mat1,matr2,  trans of m1,m2, determinant of m1,m2 ,inverse of m


import numpy as np
rows,cols=map(int,input("number of rows and columns :").split())
a=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        value=int(input(f"enter value of [{i}],[{j}]"))
        row.append(value)
    a.append(row)

a=np.array(a)
print(a)