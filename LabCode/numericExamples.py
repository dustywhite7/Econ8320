#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:42:24 2017

@author: dusty
"""

def dotProd(v1, v2): # Define our function and arguments
  if len(v1) is len(v2): # Test equality of vector length
    dp = 0               # Initialize Dot Product Value
    for i in range(len(v1)): # Loop over all elements
      dp += v1[i]*v2[i]      # Add elements of the sum
    return dp            # Return the dot product
  else: # If vetors are of unequal length, return error
    raise RuntimeError("Vectors must be of equal length")
        
        
def matMul(a, b): # Define function, take 2 matrices
  for i in range(len(a)): # Make sure a is matrix
    if len(a[i]) is not len(a[0]): # If not,
      raise RuntimeError( # Raise an error
        "Matrix A is not correctly spefified")
  for i in range(len(b)): # Make sure b is a matrix
    if len(b[i]) is not len(b[0]): # If not,
      raise RuntimeError( # Raise an error
        "Matrix B is not correctly spefified")
  matrix = [] # Initialize new empty matrix
  if len(a[0]) is len(b): # Test for conformability
    for i in range(len(a)): # Iterate over rows of a
      row = [] # Create row of new matrix
      for j in range(len(b[0])): # Iterate over columns
        row.append(dotProd(a[i], # Append elements of col
          [b[n][j] for n in range(len(b))]))
      matrix.append(row) # Append rows to matrix
    return matrix # Return the newly calculated matrix
  else: # If matrices are nonconforming
    raise RuntimeError( #Raise an error
      "Matrices are nonconformable for multiplication")
        
a = [[1,2],[3,4],[5,6],[7,8],[9,10]]
b = [[6, 10, 11, 1],[5, 4, 3, 2]]