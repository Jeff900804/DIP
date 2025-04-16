# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:53:54 2024

@author: jeff9
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

def getMotionDsf(shape,angle,dist):
    xCenter = (shape[0]-1)/2
    yCenter = (shape[1]-1)/2
    sinVal = np.sin(angle*np.pi/180)
    cosVal = np.cos(angle*np.pi/180)
    PSF = np.zeros(shape)
    for i in range(dist):
        xoffset = round(sinVal*i)
        yoffset = round(cosVal*i)
        PSF[int(xCenter-xoffset),int(yCenter+yoffset)] = 1
    return PSF/PSF.sum()

def makeBlurred(img,PSF):
    fftimg = np.fft.fft2(img)
    fftPSF = np.fft.fft2(PSF)
    fftBlur = np.fft.ifft2(fftimg*fftPSF)
    fftBlur = np.abs(np.fft.fftshift(fftBlur))
    return fftBlur

def wiener_filter(img, PSF, K=0.01):
    fftimg = np.fft.fft2(img)
    fftPSF = np.fft.fft2(PSF)
    fftWiener = np.conj(fftPSF)/(np.abs(fftPSF)**2+K)
    imgWienerFilter = np.fft.ifft2(fftimg*fftWiener)
    imgWienerFilter = np.abs(np.fft.fftshift(imgWienerFilter))
    return imgWienerFilter

def inverseFilter(img,PSF):
    fftimg = np.fft.fft2(img)
    fftPSF = np.fft.fft2(PSF)
    imgInvFilter = np.fft.ifft2(fftimg/fftPSF)
    imgInvFilter = np.abs(np.fft.fftshift(imgInvFilter))
    return imgInvFilter

img = cv2.imread('./images/test.jpg', 0)  # 灰階讀取
h_img,w_img = img.shape[:2]

PSF = getMotionDsf((h_img,w_img),15,100)
imgBlurred = np.abs(makeBlurred(img, PSF))
imgInvFilter = inverseFilter(imgBlurred , PSF)
imgWienerFilter = wiener_filter(imgBlurred , PSF)

# 顯示結果
plt.figure(figsize=(10,12))
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Blur Image')
plt.imshow(imgBlurred , cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Inverse Filter')
plt.imshow(imgInvFilter, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Wiener Filter')
plt.imshow(imgWienerFilter, cmap='gray')
plt.axis('off')

plt.show()
