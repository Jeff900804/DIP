# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:16:25 2024

@author: jeff9
"""


import numpy as np
import matplotlib.pyplot as plt

def is_symmetric(array):
    """檢查數組是否為偶對稱或奇對稱"""
    
    # 檢查是否為偶對稱
    is_even = True
    for i in range(1, len(array) // 2):
        if array[i] != array[len(array) - i]:
            is_even = False
            break
    
    # 檢查是否為奇對稱
    is_odd = (array[0] == 0)  # 第一個元素必須為0
    if is_odd:
        for i in range(1, len(array) // 2):
            if array[i] != -array[len(array) - i]:
                is_odd = False
                break
    
    if is_even:
        return 'even'
    elif is_odd:
        return 'odd'
    else:
        return 'False'

def embed_array(small_array, large_length):
    """將小數組嵌入到更大的數組中，並保持對稱"""
    large_array = np.zeros(large_length)  # 創建一個全部為0的較大數組
    small_length = len(small_array)
    
    # 計算中心點的起始索引，使數組中心對齊
    start_index = (large_length - small_length) // 2
    large_array[start_index:start_index + small_length] = small_array
    
    return large_array

# 定義一個包含負數的偶數長度數組，並嵌入到長度為10的數組
array1 = np.array([0, -2, -3, 0, 3, 2])  # 偶數對稱數組，包含負數
array1_expansion = embed_array(array1, 10)

# 定義一個包含負數的偶數長度數組，並嵌入到長度為10的數組
array2 = np.array([1, 2, 3, 4, 3, 2])  # 偶數對稱數組，包含負數
array2_expansion = embed_array(array2, 10)

# 定義一個包含負數的奇數長度數組，並嵌入到長度為9的數組
array3 = np.array([0, -2, -1, 1, 2])  # 奇數對稱數組，包含負數
array3_expansion = embed_array(array3, 9)

# 檢查對稱性
print("Is the array1 Even or Odd Array Symmetric?:", is_symmetric(array1_expansion))
print("Is the array2 Even or Odd Array Symmetric?:", is_symmetric(array2_expansion))
print("Is the array3 Even or Odd Array Symmetric?:", is_symmetric(array3_expansion))

