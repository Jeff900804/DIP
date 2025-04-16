# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:43:46 2024

@author: jeff9
"""


import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure, io

# 讀取圖像
image1 = io.imread('./images/image_2-1.jpg', as_gray=True)  
image2 = io.imread('./images/images_2-2.jpg', as_gray=True)  
image3 = io.imread('./images/images_2-3.jpg', as_gray=True)  

def difference_image(matched_image,image2):
    g = abs(matched_image-image2)
    gm = g-np.min(g)
    gs = 255*(gm/np.max(gm))
    return gs

def histogram_matching(image1, image2):
    # 進行直方圖匹配
    matched_image = exposure.match_histograms(image1, image2, multichannel=False)
    
    # 顯示原圖像、匹配後的圖像和目標圖像
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(image1, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    axes[1].imshow(matched_image, cmap='gray')
    axes[1].set_title('Histogram Matched Image')
    axes[1].axis('off')
    
    diff_image = difference_image(matched_image, image2)
# =============================================================================
#     axes[2].imshow(image2, cmap='gray')
#     axes[2].set_title('Target Image')
#     axes[2].axis('off')
# =============================================================================
    axes[2].imshow(diff_image, cmap='gray')
    axes[2].set_title('Difference Image')
    axes[2].axis('off')
    plt.show()

histogram_matching(image1, image2)
histogram_matching(image1, image3)