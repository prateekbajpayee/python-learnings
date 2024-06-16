#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:05:07 2024

@author: prateekbajpayee
"""



""" 
Calculate fibonacci series
1 1 2 3 5 8 13 21 34

"""

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
 
"""
Write a Python program to sum up the numbers you type in. The program should stop when you enter ‘0’
"""
def sumNum():
    total = 0
    while 1:
        a = int(input("Enter Number:"))
        if a != 0:
            total+=a
        else:
            return total
        
"""
Write a Python function to compute the compound interest, the principal and interest rates are to be entered by the user. 
"""
def calCompoundInt(principal,duration,rateOfInterest):
    return round(principal*((1+(rateOfInterest/100)) ** duration),2)

#print("SUM -- ",sumNum())

#print("fibonacci of Number 10 - ", fibonacci(10))

print("Total Amount - ", calCompoundInt(float(input("principal")),
      float(input("duration")),
      float(input("rateOfInterest"))))
