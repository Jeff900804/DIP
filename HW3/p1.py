# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:50:26 2024

@author: jeff9
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

path = './images/Fig0465(a).tif'
img = cv2.imread(path,0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# plt.imshow(magnitude_spectrum ,cmap='gray')
# plt.axis('off')
# plt.show()

mask = np.ones(fshift.shape)

center= [[337,337]]
mask_range = 337
center_range = 30
width = 4

mask[center[0][0]-mask_range:center[0][0]-center_range,center[0][1]-width:center[0][1]+width] = 0
mask[center[0][0]+center_range:center[0][0]+mask_range,center[0][1]-width:center[0][1]+width] = 0


fshift = fshift*mask

ishift = np.fft.ifftshift(fshift)
iimag = np.fft.ifft2(ishift)
iimag = np.abs(iimag)

plt.imshow(iimag ,cmap='gray')
plt.axis('off')
plt.show()

# cv2.imwrite('./images/output/image_2_output.png', iimag)