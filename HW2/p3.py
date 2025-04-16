# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:59:40 2024

@author: jeff9
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftshift, fft2, ifft2

# 讀取圖像
image = cv2.imread('./images/keyboard.tif', cv2.IMREAD_GRAYSCALE)

# 1. 計算圖像的傅里葉頻譜
def fourier_spectrum(image):
    f_transform = fft2(image)
    f_transform_shifted = fftshift(f_transform)
    magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)
    return magnitude_spectrum

# 2. 創建垂直 Sobel 核
sobel_kernel = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])

# 施加奇對稱
def enforce_odd_symmetry(kernel):
    # 檢查 kernel 是否已奇對稱，否則轉換
    kernel_flipped = np.flip(kernel)
    return (kernel - kernel_flipped) / 2

# =============================================================================
# # 3. 頻域濾波
# def frequency_filtering(image, kernel):
#     kernel_padded = np.pad(kernel, [(image.shape[0] - kernel.shape[0]) // 2,
#                                     (image.shape[1] - kernel.shape[1]) // 2], mode='constant')
#     kernel_f_transform = fft2(kernel_padded)
#     image_f_transform = fft2(image)
#     
#     # 濾波
#     filtered_f_transform = image_f_transform * kernel_f_transform
#     filtered_image = np.abs(ifft2(filtered_f_transform))
#     
#     return filtered_image
# =============================================================================
    # 3. 頻域濾波
def frequency_filtering(image, kernel):
    # 獲取圖像的大小
    image_shape = image.shape
    
    # 創建一個與圖像大小相同的核，並在中間放置Sobel核，其他地方填充0
    padded_kernel = np.zeros_like(image)
    kernel_shape = kernel.shape
    
    # 計算放置Sobel核的起點
    x_start = (image_shape[0] - kernel_shape[0]) // 2
    y_start = (image_shape[1] - kernel_shape[1]) // 2
    
    # 把Sobel核放在圖像大小的零矩陣中
    padded_kernel[x_start:x_start + kernel_shape[0], y_start:y_start + kernel_shape[1]] = kernel
    
    # 對圖像和核進行傅里葉變換
    kernel_f_transform = fft2(padded_kernel)
    image_f_transform = fft2(image)
    
    # 進行頻域濾波
    filtered_f_transform = image_f_transform * kernel_f_transform
    
    # 逆傅里葉變換得到濾波後的圖像
    filtered_image = np.abs(ifft2(filtered_f_transform))
    
    return filtered_image

# 4. 空間域濾波
def spatial_filtering(image, kernel):
    return cv2.filter2D(image, -1, kernel)

# 1. 顯示原圖像傅里葉頻譜
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(122), plt.imshow(fourier_spectrum(image), cmap='gray'), plt.title('Fourier Spectrum')
plt.axis('off')
plt.show()

# 2. 對垂直 Sobel 核施加奇對稱並顯示
odd_sobel_kernel = enforce_odd_symmetry(sobel_kernel)
plt.figure()
plt.title('Odd Symmetry Sobel Kernel')
plt.axis('off')
plt.imshow(odd_sobel_kernel, cmap='gray')
plt.show()

# 3. 頻域濾波結果 (施加奇對稱)
filtered_image_frequency = frequency_filtering(image, odd_sobel_kernel)
plt.figure()
plt.title('Frequency-Domain Filtering (Odd Symmetry)')
plt.axis('off')
plt.imshow(filtered_image_frequency, cmap='gray')
plt.show()

# 4. 空間域濾波結果
filtered_image_spatial = spatial_filtering(image, sobel_kernel)
plt.figure()
plt.title('Spatial-Domain Filtering')
plt.axis('off')
plt.imshow(filtered_image_spatial, cmap='gray')
plt.show()

# 5. 頻域濾波結果 (不施加奇對稱)
filtered_image_frequency_no_symmetry = frequency_filtering(image, sobel_kernel)
plt.figure()
plt.title('Frequency-Domain Filtering (No Symmetry)')
plt.axis('off')
plt.imshow(filtered_image_frequency_no_symmetry, cmap='gray')
plt.show()