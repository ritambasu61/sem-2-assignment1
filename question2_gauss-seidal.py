#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 03:04:53 2020

@author: ritambasu
"""

import numpy as np

x=np.zeros(5) #initial guess
xsol=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
a=np.array([[0.2,0.1,1,1,0],[0.1,4.0,-1,1,-1],[1,-1,60.0,0,-2],[1,1,0,8.0,4],[0,-1,-2,4,700.0]])
b=np.array([1.0,2.0,3.0,4.0,5.0])
count=0



#construction of loop to define the recurance sum and to satisfy the condition to converge in 0.01
while max(abs(x-xsol))>=0.01: 
        s=np.zeros(5)      
        for i in range(0,len(a)): 
            for j in range(0,len(a)):
                if j != i:
                    s[i] = s[i]-(a[i][j]*x[j])
            x[i]=((s[i]+b[i])/(a[i][i]))
        count=count+1
print(x)
print("no. of iteration=",count)    
