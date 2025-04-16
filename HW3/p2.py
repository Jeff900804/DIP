import matplotlib.pyplot as graph
import numpy as np
from numpy import fft
import math
import cv2

# 運動模糊的點擴散函數 (PSF) 生成函數
def motion_process(image_size, motion_angle):
    PSF = np.zeros(image_size)
    center_position_h = (image_size[0] - 1) / 2
    center_position_w = (image_size[1] - 1) / 2

    slope_tan = math.tan(motion_angle * math.pi / 180)
    slope_cot = 1 / slope_tan
    if slope_tan <= 1:
        for i in range(15):
            offset = round(i * slope_tan)
            PSF[int(center_position_h + offset), int(center_position_w - offset)] = 1
    else:
        for i in range(15):
            offset = round(i * slope_cot)
            PSF[int(center_position_h - offset), int(center_position_w + offset)] = 1

    return PSF / PSF.sum()
# Wiener 濾波器函數
def wiener(input_img, PSF, eps, K):
    input_fft = fft.fft2(input_img)
    PSF_fft = fft.fft2(PSF) + eps
    PSF_fft_1 = np.conj(PSF_fft) / (np.abs(PSF_fft) ** 2 + K)
    result = fft.ifft2(input_fft * PSF_fft_1)
    result = np.abs(fft.fftshift(result))
    return result

# 銳化函數
def unsharp_mask(image, amount):
    blurred = cv2.GaussianBlur(image, (0, 0), 3)
    sharpened = cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)
    return np.clip(sharpened, 0, 255)

# 讀取圖片並轉換成灰階
image = cv2.imread('./images/test2.jpg',0)


img_h, img_w = image.shape

fig, ax = graph.subplots(1, 2, figsize=(10, 5))
ax[0].set_title("Original Image")
ax[0].imshow(image, cmap='gray')
ax[0].axis('off')

# 參數設置
angle = 160      
k = 0.5 
eps = 0           
sharpness = 1.0  

# 生成 PSF
PSF = motion_process((img_h, img_w), angle)

# 應用 Wiener 濾波器
result = wiener(image, PSF, eps, k)

# 應用銳化
result = unsharp_mask(result.astype(np.uint8), sharpness)

# 顯示處理後的圖像
ax[1].set_title("Wiener Deblurred")
ax[1].imshow(result, cmap='gray')
ax[1].axis('off')

graph.show()
