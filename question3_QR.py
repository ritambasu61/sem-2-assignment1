#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:31:10 2020

@author: ritambasu
"""

import numpy as np

m=2 #matrix_order

a=np.array([[5.0,-2.0],[-2.0,8.0]])
q,r=np.linalg.qr(a)
d=np.allclose(a, np.dot(q, r))
print("q=",q,"\nr=",r,"\n qr = a is",d)



#defining a fuction to check the matrix is diagonal or not

def diagg(matrix,order):
   k=0
   i=0
   while i < order:
     for j in range(order):
         if j!=i and abs(matrix[i][j])<0.001 :
             k=k+1
     i=i+1
   return k
b=np.array([[5.0,0],[-0,8.0]])   
print(diagg(b,2))


#diagonalization cheacking
"""as no of non diagonal elements in a matrix of order m = m^2-m. So,if diagg_function has the value less 
than (m^2-m) then loop starts.i.e the input matrix is not diagonal """

while diagg(a,m)!=((m**2)-m):
    Q,R=np.linalg.qr(a)
    Qt=np.transpose(Q)
    a=np.linalg.multi_dot([Qt,a,Q])


#print_command
"""cheacking is based on eigh header file of numpy 
and look this nice I have personally used one trick though this trick will not 
work in general m*m order matrices"""

print("eigenvalues are:\n")
for i in range(m):
    if i==0:
        print("lambda",i+1,"=",a[i+1][i+1])
    if i==1:
        print("lambda",i+1,"=",a[i-1][i-1])
    
    print("original lambda ",i+1,"=",np.linalg.eigh(a)[0][i],"\n")    
    
       
       



    
    

    
    
     
     
             
           
       
        