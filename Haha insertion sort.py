# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:14:38 2021

@author: brand
"""

arrInput = [1, 4, 2, 5, 3, 4, -9, -9, 0]

def InsertionSort(arr):
    ptr = temp = 0
    for i in range(len(arr)):
        ptr = i - 1
        
        while(ptr >= 0 and arr[ptr] > arr[ptr + 1]):
            temp = arr[ptr + 1]
            arr[ptr + 1] = arr[ptr]
            arr[ptr] = temp
            ptr -= 1
    
    return arr
    
print(InsertionSort(arrInput))