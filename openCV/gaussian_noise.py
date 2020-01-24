import cv2
import numpy as np 
from skimage.util import random_noise

img = cv2.imread('../assets/Lenna.png',-1)

noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)

noise_img = np.array(255*noise_img, dtype='uint8')

cv2.imwrite('../assets/blur_Lenna.png', noise_img)

cv2.imshow('blur', noise_img)

k = cv2.waitKey(0) and 0xFF 

if k == 27: # close window when esc key is pressed
  cv2.destroyAllWindows()