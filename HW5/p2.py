# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:56:34 2024

@author: jeff9
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./images/image2.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

lower_purple = np.array([180, 200, 0])
upper_purple = np.array([255, 255, 255])

mask = cv2.inRange(image_rgb, lower_purple, upper_purple)


kernel = np.ones((8, 8), np.uint8)
mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

segmented = cv2.bitwise_and(image_rgb, image_rgb, mask=mask_cleaned)
segmented2 = cv2.bitwise_xor(image_rgb,segmented)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Segmented Result")
plt.imshow(segmented)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Segmented Result")
plt.imshow(segmented2)
plt.axis('off')

plt.show()
