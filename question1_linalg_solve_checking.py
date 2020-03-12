#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:14:20 2020

@author: ritambasu
"""
#writing the code:
import numpy as np
a = np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
b = np.array([2,2,2])
x = np.linalg.solve(a,b)
true_solved_solution = np.array([1.0,1.0,1.0])
print (x)
#checking Ax=b is true or false:
y = np.allclose(np.dot(a, x), b, true_solved_solution )
print ("Is the solution matched with the true one?",y)