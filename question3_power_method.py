#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:50:01 2020

@author: ritambasu
"""
import numpy as np 

a= np.array([[2.0,-1,0],[-1,2.0,-1],[0,-1,2.0]])
x= np.array([1,1.0,1.0])
y= np.array([1,1.0,1.0])
maximum_eigenvalue= max(np.linalg.eigh(a)[0])

k=1
i=0
ax=np.dot(a,x)
dominant_eigvalue=np.dot(ax,x)/np.dot(x,x)

accuracy=1.2 #arbitary error is defined here to start the loop( actually in c we can do it using do_while loop but python does not have it)

while accuracy > 1.0:
    m=np.dot(np.dot(np.linalg.matrix_power(a,(i+1)),x),y) #here m= < A^(k+1)*x , y >
    n=np.dot(np.dot(np.linalg.matrix_power(a,i),x),y)     #here m= < A^(k)*x , y > 
    eigenvalue=float(m)/float(n)
    accuracy=(abs(maximum_eigenvalue-eigenvalue)/maximum_eigenvalue)*100
    i=i+1
z=np.dot(np.linalg.matrix_power(a,i),x)
eigen_vector=z/np.linalg.norm(z)


print("lialg.eigh eigenvalue:",maximum_eigenvalue,"\neigenvalue using power method:",eigenvalue,
      "\nnormalized eigen vectorby power method:",eigen_vector)



