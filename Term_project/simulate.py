# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:45:01 2024

@author: jeff9
"""


import numpy as np
import colour
import cv2

# 定義轉換矩陣
class DisplayModel:
    def __init__(self, gamma, transform_matrix):
        self.gamma_r = gamma[0]
        self.gamma_g = gamma[1]
        self.gamma_b = gamma[2]
        self.transform_matrix = transform_matrix
        
    def rgb_to_xyz(self, rgb):
        r_lin = rgb[0] ** self.gamma_r
        g_lin = rgb[1] ** self.gamma_g
        b_lin = rgb[2] ** self.gamma_b
        rgb_lin = np.array([r_lin, g_lin, b_lin])
        xyz = np.dot(self.transform_matrix, rgb_lin)
        return xyz
    
    def xyz_to_rgb(self,xyz):
        rgb_lin = np.clip(np.dot(np.linalg.inv(self.transform_matrix),xyz),0,1)
        r = rgb_lin[0] ** (1/self.gamma_r)
        g = rgb_lin[1] ** (1/self.gamma_g)
        b = rgb_lin[2] ** (1/self.gamma_b)
        rgb = np.array([r,g,b])
        return rgb
    
class Enhance_image:
    def __init__(self,display_model_full,display_model_low):
        self.display_model_full = display_model_full
        self.display_model_low = display_model_low
        
    def Device_Characteristic_Modeling(self,rgb):
        """
        第一層轉換 由 RGB-> XYZ
        """
        xyz = display_model_low.rgb_to_xyz(rgb/255.0)
        return xyz
          
    def Post_Gamut_Mapping(self,xyz):
        """
        第四層轉換 由 XYZ-> RGB
        """
        rgb = np.clip(self.display_model_full.xyz_to_rgb(xyz),0,1)*255
        return rgb
    
    
if __name__ == "__main__":
    # Example display parameters
    gamma_f = [2.4767, 2.4286, 2.3792]
    gamma_l = [2.2212, 2.1044, 2.1835]
    
    transform_matrix_full = np.array([[95.57, 64.67, 33.01],
                                      [49.49, 137.29, 14.76],
                                      [0.44, 27.21, 169.83]])
    
    transform_matrix_low = np.array([[4.61, 3.35, 1.78],
                                      [2.48, 7.16, 0.79],
                                      [0.28, 1.93, 8.93]])
    
    display_model_full = DisplayModel(gamma_f, transform_matrix_full)
    display_model_low = DisplayModel(gamma_l, transform_matrix_low)
    
    input_path = "./images/4862565c2e7fafbef4e6001f6f7605e9_result.jpg"
    input_image = np.array(cv2.imread(input_path))
    
    Enhance = Enhance_image(display_model_full, display_model_low)
    height, width, _ = input_image.shape
    output_image = np.zeros_like(input_image, dtype=np.float32) 
    for i in range(height):
        for j in range(width):
            xyz = Enhance.Device_Characteristic_Modeling(input_image[i,j])
            rgb = Enhance.Post_Gamut_Mapping(xyz)
            output_image[i,j] = rgb
    
    cv2.imwrite(f'{input_path[:-4]}_simulate.jpg',output_image)