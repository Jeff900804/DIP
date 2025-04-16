# HW2 has four problems  
### Problem 1

An image containing vertical bars like the one shown below was blurred using square box kernels of size 23, 25, and 45 pixels on the side, respectively. The vertical bars are 5 pixels wide, 100 pixels high, and their separation is 20 pixels.  

a) Generate the image according to the specification and Implement the lowpass filtering in Matlab.  

b) If the filters are implemented correctly, you can see a clear separation between the filtered vertical bars for box kernels of size 23 and 45. However, such separation does not exist for the box kernel of size 25. More specifically, the bars have merged. Explain the reason.  

### Problem 2  

The images below were obtained using a combination of filters described in Section 3.8. Now, let’s see if the results can be obtained by histogram matching.  

a) Design a histogram matching algorithm to convert the left image to the middle image.  

b) Design a histogram matching algorithm to convert the left image to the right image.  

Also provide a difference image, probably scaled up to 255, in both cases to show the performance of your algorithm.  

### Problem 3  

Follow the steps outlined in Section 4.7 to repeat Example 4.15, pp. 271-273, using the vertical Sobel kernel shown in Fig. 4.38(a) and the test image “keyboard.tif.” You may use any existing library to compute Fourier transform.  
a) Show the Fourier spectrum of the test image “keyboard.”  

b) Enforce odd symmetry on the kernel. Show the kernel.  

c) Show the result of frequency-domain filtering of the test image using the vertical Sobel kernel.  

d) Compare your result in c) with the result of space-domain filtering.  

e) Show the result of frequency-domain filtering without enforcing odd symmetry on the kernel.  

### Problem 4  

Embedding a 2-D array of even (odd) dimensions into a larger array of zeros of even (odd) dimensions keeps the symmetry of the original array, provided that the centers coincide. Show that this is true also for the following 1-D arrays. That is show that the larger arrays have the same symmetry as the smaller arrays. For arrays of even length, use arrays of 0’s ten elements long. For arrays of odd lengths, use arrays of 0’s nine elements long.  

a) {0, − b, − c, 0, c, b}  

b) {a, b, c, d, c, b}  

c) {0, − b, − c, c, b}






