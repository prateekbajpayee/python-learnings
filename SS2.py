#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:17:41 2024

@author: prateekbajpayee
"""

""" 
Write a Python program to determine whether the matrix entered by you is sparse.
"""

def calculateSparseMatrix(matrix):
    zCount=0
    mSize=0
    for ml in matrix :
        zCount += ml.count(0)
        mSize += len(ml)
    if mSize - zCount > zCount:
        print("Not Sparse Matrix")
        return
    print("Is Sparse Matrix")
    
    
#myMatrix = [[0,1,3],[0,1,3],[0,1,2]]
#calculateSparseMatrix(myMatrix)

"""
Write a Python program to count the number of foreign city names 
entered by you and determine the longest name among the cities. 
The user should be able to stop entering the city names by typing "Stop."
"""
def citiesInput():
    cityNames =[]
    cityMaxName = ''
    cityMaxCount = 0
    while True:
        cityName = str(input("Enter a city Name:"))
        if cityName == 'Stop':
            print(cityMaxName)
            return cityMaxName
        cityNames.append(cityName)
        if cityMaxCount < len(cityName) :
            cityMaxName = cityName
            cityMaxCount = len(cityName)


#citiesInput()