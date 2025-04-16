# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:38:50 2024

@author: jeff9
"""


import cv2  

input_path = "./images/FigP0917(noisy_rectangle).tif" 
 

img_A = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE) 
  
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (58, 58))  # 假設結構元素是小圓形 
 

C = cv2.erode(img_A, kernel, iterations=1) 

D = cv2.dilate(C, kernel, iterations=1) 
 
E = cv2.dilate(D, kernel, iterations=1) 

F = cv2.erode(E, kernel, iterations=1) 
 
output_paths = { 
    "C": "./images/output/result_C.png", 
    "D": "./images/output/result_D.png", 
    "E": "./images/output/result_E.png", 
    "F": "./images/output/result_F.png" 
} 
 
cv2.imwrite(output_paths["C"], C) 
cv2.imwrite(output_paths["D"], D) 
cv2.imwrite(output_paths["E"], E) 
cv2.imwrite(output_paths["F"], F) 
 