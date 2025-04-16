# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:57:43 2024

@author: jeff9
"""


import cv2
import numpy as np
import math

path = './images/T.tif'
path2 = './images/T_transformed.tif'

def img_size_to_540(img):
    output_img = np.zeros((540,540))
    dx = math.floor(540 - len(img))
    dy = math.floor(540 - len(img[0]))
    
    for i in range(len(img)-1):
        for j in range(len(img[0])-1):
            if(dx<0 and dy<0):
                try:
                    output_img[i][j] = img[abs(dx)//2+i][abs(dy)//2+j]
                except:
                    continue
            else:
                output_img[dx//2+i][dy//2+j] = img[i][j]
    return output_img

def cubic_interpolate(p0, p1, p2, p3, t):

    a0 = p3 - p2 - p0 + p1
    a1 = p0 - p1 - a0
    a2 = p2 - p0
    a3 = p1
    return a0 * t**3 + a1 * t**2 + a2 * t + a3


def resize(input_image,scale,interpolation):
    input_height,input_width = len(input_image),len(input_image[0])
    output_height = int(input_height * scale)
    output_width = int(input_width * scale)
    output_image = np.zeros((output_height,output_width))
    
    
    for i in range(output_height-1):
        for j in range(output_width-1):
            if(interpolation == 'nearest_neighbor'):
                output_image[i][j] = input_image[round(i/scale)][round(j/scale)]
            if(interpolation == 'bilinear'):
                l = math.floor(i/scale)
                k = math.floor(j/scale)
                a = (i/scale)-l
                b = (j/scale)-k
                output_image[i][j] = ((1-a)*(1-b)*input_image[l][k]
                                      +a*(1-b)*input_image[l+1][k]
                                      +(1-a)*b*input_image[l][k+1]
                                      +a*b*input_image[l+1][k+1])
            if(interpolation == 'bicubic'):
                x = j / scale
                y = i / scale
    
                x0 = math.floor(x) - 1
                x1 = math.floor(x)
                x2 = math.ceil(x)
                x3 = math.ceil(x) + 1
                
                y0 = math.floor(y) - 1
                y1 = math.floor(y)
                y2 = math.ceil(y)
                y3 = math.ceil(y) + 1
                
                x0 = max(0, min(x0, input_width - 1))
                x1 = max(0, min(x1, input_width - 1))
                x2 = max(0, min(x2, input_width - 1))
                x3 = max(0, min(x3, input_width - 1))
                
                y0 = max(0, min(y0, input_height - 1))
                y1 = max(0, min(y1, input_height - 1))
                y2 = max(0, min(y2, input_height - 1))
                y3 = max(0, min(y3, input_height - 1))
    
                col0 = cubic_interpolate(input_image[y0][x0], input_image[y0][x1], input_image[y0][x2], input_image[y0][x3], x - x1)
                col1 = cubic_interpolate(input_image[y1][x0], input_image[y1][x1], input_image[y1][x2], input_image[y1][x3], x - x1)
                col2 = cubic_interpolate(input_image[y2][x0], input_image[y2][x1], input_image[y2][x2], input_image[y2][x3], x - x1)
                col3 = cubic_interpolate(input_image[y3][x0], input_image[y3][x1], input_image[y3][x2], input_image[y3][x3], x - x1)
    

                output_image[i][j] = cubic_interpolate(col0, col1, col2, col3, y - y1)

                        
    return output_image


def rotate_image(img, angle):
    angle_rad = math.radians(angle)
    height = len(img)
    width = len(img[0])

    new_height = int(abs(width * math.sin(angle_rad)) + abs(height * math.cos(angle_rad)))
    new_width = int(abs(width * math.cos(angle_rad)) + abs(height * math.sin(angle_rad)))
    

    cx, cy = width // 2, height // 2
    new_img = np.zeros((new_height, new_width), dtype=np.uint8)  
    
    new_cx, new_cy = new_width // 2, new_height // 2
    
    for i in range(new_height):
        for j in range(new_width):

            x = (j - new_cx) * math.cos(-angle_rad) - (i - new_cy) * math.sin(-angle_rad) + cx
            y = (j - new_cx) * math.sin(-angle_rad) + (i - new_cy) * math.cos(-angle_rad) + cy

            if 0 <= x < width and 0 <= y < height:
                new_img[i, j] = img[int(y)][int(x)]
                
    return new_img

img = cv2.imread(path,0)

img_rotate = rotate_image(img, 21)

img_result_nn = resize(img_rotate,0.8,'nearest_neighbor')
img_result_bl = resize(img_rotate,0.8,'bilinear')
img_result_bc = resize(img_rotate,0.8,'bicubic')

img_result_nn = img_size_to_540(img_result_nn)
img_result_bl = img_size_to_540(img_result_bl)
img_result_bc = img_size_to_540(img_result_bc)

# imgs = np.hstack([img_result_nn,img_result_bl,img_result_bc])
# cv2.imshow('result',imgs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('./images/output/image_1_nearest_neighbor_output.png', img_result_nn)
cv2.imwrite('./images/output/image_1_bilinearr_output.png', img_result_bl)
cv2.imwrite('./images/output/image_1_bicubic_output.png', img_result_bc)