import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/pout-dark.jpg',0)

equ = cv2.equalizeHist(img) 

X = np.concatenate((img, equ), axis=1)

cv2.imshow('Image',X) 
plt.show()
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 