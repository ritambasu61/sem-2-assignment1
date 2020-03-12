#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 04:00:29 2020

@author: ritambasu
"""
import numpy as np
import timeit
starttime=timeit.default_timer()


#defining function for m*n matrix
def svd(matrix,row,col):
    
    aTa=np.dot(np.transpose(matrix),matrix)
    aaT=np.dot(matrix,np.transpose(matrix))
    aTa_eig=np.linalg.eigh(aTa)
    aaT_eig=np.linalg.eigh(aaT)
 
    
    #constructing the diagonal D matrix
    D=np.zeros(min(row,col))
    minimum=min(row,col)
    if minimum==row:
        for i in range(minimum):
            D[i]=np.sqrt(aaT_eig[0][i])
    else:
        for i in range(minimum):
            D[i]=np.sqrt(aTa_eig[0][i])
    
    U=np.transpose(aaT_eig[1])
    
    VT=aTa_eig[1]
    return (U,D,VT)


#determining singular values of a matrix A
a=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,1],[1,0,1]])
u,d,vt=svd(a,5,3)
print ("U = \n",u,"\n \nsingular values of a :\n",d," \n \n V = \n",vt)


#time taken for my code to run
print("Time taken by this code : ",timeit.default_timer()-starttime)



#comparing results with linalg.svt
U,D,V=np.linalg.svd(a)
print("linalg u= \n",U,"\n\nlinalg d=\n",D,"\n\nlinalg v=\n",V)




# use of timeit for calculating the time taken by np.linalg.svd()

linalg_svtcode='''
import numpy as np
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,1],[1,0,1]])
U,D,V=np.linalg.svd(A)
'''
print("\nTime taken by np.linalg.svd() : ",timeit.timeit(linalg_svtcode))


    
                   
    