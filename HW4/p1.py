import numpy as np
from skimage.transform import radon, iradon

image_size = 600 
square_size = 300  
num_projections = 849  
theta = np.arange(0,180,0.5)

image = np.zeros((image_size, image_size))
start = (image_size - square_size) // 2
end = start + square_size
image[start:end, start:end] = 1  


sinogram = radon(image, theta=theta, circle=False)


reconstructed_image_no_filter = iradon(sinogram, theta=theta, filter=None)
center = reconstructed_image_no_filter.shape[0] // 2
reconstructed_image_no_filter = reconstructed_image_no_filter[
    center-300:center+300, center-300:center+300
]


reconstructed_image = iradon(sinogram, theta=theta, filter='hamming')
center = reconstructed_image.shape[0] // 2
reconstructed_image = reconstructed_image[
    center-300:center+300, center-300:center+300
]

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.axis('off')
plt.imshow(image, cmap="gray")

plt.subplot(2, 2, 2)
plt.title("Sinogram")
plt.axis('off')
plt.imshow(sinogram, cmap="gray", aspect='auto')

plt.subplot(2, 2, 3)
plt.title("Reconstructed Image (No Filtering)")
plt.axis('off')
plt.imshow(reconstructed_image_no_filter, cmap="gray")

plt.subplot(2, 2, 4)
plt.title("Reconstructed Image")
plt.axis('off')
plt.imshow(reconstructed_image, cmap="gray")
plt.show()
