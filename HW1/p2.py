# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:50:26 2024

@author: jeff9
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

path = './images/image_2.bmp'
img = cv2.imread(path,0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

mask = np.ones(fshift.shape)

center= [[385,474],[435,524]]
mask_range = 10

# mask[center[0][0]-mask_range:center[0][0]+mask_range,center[0][1]-mask_range:center[0][1]+mask_range] = 0
# mask[center[1][0]-mask_range:center[1][0]+mask_range,center[1][1]-mask_range:center[1][1]+mask_range] = 0

# for i in range(mask_range):
    # mask[center[0][0]-mask_range+i:center[0][0]+mask_range-i,center[0][1]-i:center[0][1]+i]=0
    # mask[center[1][0]-mask_range+i:center[1][0]+mask_range-i,center[1][1]-i:center[1][1]+i]=0
        
mask[center[0][0]-mask_range:center[0][0]+mask_range,center[0][1]] = 0
mask[center[1][0]-mask_range:center[1][0]+mask_range,center[1][1]] = 0
mask[center[0][0],center[0][1]-mask_range:center[0][1]+mask_range] = 0
mask[center[1][0],center[1][1]-mask_range:center[1][1]+mask_range] = 0

fshift = fshift*mask

ishift = np.fft.ifftshift(fshift)
iimag = np.fft.ifft2(ishift)
iimag = np.abs(iimag)

plt.imshow(magnitude_spectrum ,cmap='gray')
plt.axis('off')
plt.show()

# cv2.imwrite('./images/output/image_2_output.png', iimag)