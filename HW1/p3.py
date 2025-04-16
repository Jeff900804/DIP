# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:36:12 2024

@author: jeff9
"""


import cv2
import numpy as np

path = './images/image_3.png'
path2 = './images/image_3_Result.tif'

img = cv2.imread(path,0)
img_ref = cv2.imread(path2,0)

def Intensity_level_slicing(img,value):
    img_result = img.copy()
    rows,cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if (img_result[i][j]>value[0] and img_result[i][j]<value[1]):
                img_result[i][j] = 0

    return img_result
 
img_result = Intensity_level_slicing(img, [80,165])

# =============================================================================
# imgs =  np.hstack([img,img_result,img_ref])          
# cv2.imshow('result',imgs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================
cv2.imwrite('./images/image_3_output.png',img_result)
# np.savetxt('img.csv', img, delimiter=',')