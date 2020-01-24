import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('../assets/Lenna.png',-1)

plt.subplot(221)
plt.imshow(img)

plt.subplot(222)
plt.hist(img.ravel(), 256,[0,256])

plt.show()