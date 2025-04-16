# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:06:20 2024

@author: jeff9
"""


import numpy as np
import matplotlib.pyplot as plt
import cv2

# 1. 生成垂直條紋圖像
def generate_stripes_image(image_height, image_width, bar_width, bar_separation):
    img = np.ones((image_height, image_width)) * 255  # 白色背景
    num_bars = image_width // (bar_width + bar_separation)  # 計算有多少黑線
    for i in range(num_bars):
        start_x = i * (bar_width + bar_separation)
        img[:, start_x:start_x + bar_width] = 0  # 黑色條紋
    return img

# 設置圖片參數
image_height = 100  # 圖片高度
image_width = 200   # 圖片寬度
bar_width = 5       # 黑線寬度
bar_separation = 20 # 黑線之間的距離（白色部分）

# 生成圖片
stripes_img = generate_stripes_image(image_height, image_width, bar_width, bar_separation)

# 顯示原始圖片
plt.figure(figsize=(10, 5))
plt.title('Original Stripes Image')
plt.imshow(stripes_img, cmap='gray')
plt.axis('off')
plt.show()

# 2. 應用不同大小的方形框核進行模糊處理
def apply_box_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))
    # return cv2.GaussianBlur(image, (kernel_size, kernel_size),0)

# 定義方形框核的大小
kernel_sizes = [23, 25, 45]

# 對圖片應用不同的模糊效果
fig, axes = plt.subplots(1, len(kernel_sizes)+1, figsize=(15, 5))
axes[0].imshow(stripes_img, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off')

# 遍歷不同的核尺寸，應用濾波器並顯示結果
for i, kernel_size in enumerate(kernel_sizes):
    blurred_img = apply_box_filter(stripes_img, kernel_size)
    axes[i+1].imshow(blurred_img, cmap='gray')
    axes[i+1].set_title(f'Kernel Size: {kernel_size}')
    axes[i+1].axis('off')

plt.show()