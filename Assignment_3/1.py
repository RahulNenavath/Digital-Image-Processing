import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../assets/Lenna.png',0)

height, width = img.shape
print(height, width)

# j = float(input('Scaling by a factor of: '))

# bilinear_img = cv2.resize(img,(0,0), fx=j,fy=j ,interpolation = cv2.INTER_LINEAR)

cv2.imshow("Resized image by factor 1", cv2.resize(img, None, fx=1, fy=1, interpolation = cv2.INTER_LINEAR))
cv2.imshow("Resized image by factor 2", cv2.resize(img,None, fx=2,fy=2, interpolation = cv2.INTER_LINEAR))
cv2.imshow("Resized image by factor 0.5", cv2.resize(img, None, fx=0.5,fy=0.5, interpolation = cv2.INTER_LINEAR))

def GetBilinearPixel(imArr, posX, posY):
	out = []
	modXi = int(posX)
	modYi = int(posY)
	modXf = posX - modXi
	modYf = posY - modYi
	modXiPlusOneLim = min(modXi+1,imArr.shape[1]-1)
	modYiPlusOneLim = min(modYi+1,imArr.shape[0]-1)
 
	for chan in range(imArr.shape[2]):
		bl = imArr[modYi, modXi, chan]
		br = imArr[modYi, modXiPlusOneLim, chan]
		tl = imArr[modYiPlusOneLim, modXi, chan]
		tr = imArr[modYiPlusOneLim, modXiPlusOneLim, chan]
		b = modXf * br + (1. - modXf) * bl
		t = modXf * tr + (1. - modXf) * tl
		pxf = modYf * t + (1. - modYf) * b
		out.append(int(pxf+0.5))
 
	return out

im = cv2.imread('../assets/Lenna.png')
enlargedShape = list(map(int, [im.shape[0], im.shape[1], im.shape[2]])) #scale by 1
enlargedImg = np.empty(enlargedShape, dtype=np.uint8)
rowScale = float(im.shape[0]) / float(enlargedImg.shape[0])
colScale = float(im.shape[1]) / float(enlargedImg.shape[1])

for r in range(enlargedImg.shape[0]):
	for c in range(enlargedImg.shape[1]):
		orir = r * rowScale 
		oric = c * colScale
		enlargedImg[r, c] = GetBilinearPixel(im, oric, orir)
cv2.imshow("Scaled Image - 1x",enlargedImg)

enlargedShape = list(map(int, [im.shape[0]*2, im.shape[1]*2, im.shape[2]])) #scale by 2
enlargedImg = np.empty(enlargedShape, dtype=np.uint8)
rowScale = float(im.shape[0]) / float(enlargedImg.shape[0])
colScale = float(im.shape[1]) / float(enlargedImg.shape[1])
 
for r in range(enlargedImg.shape[0]):
	for c in range(enlargedImg.shape[1]):
		orir = r * rowScale 
		oric = c * colScale
		enlargedImg[r, c] = GetBilinearPixel(im, oric, orir)
cv2.imshow("Scaled Image - 2x",enlargedImg)

enlargedShape = list(map(int, [im.shape[0]*0.5, im.shape[1]*0.5, im.shape[2]])) #scale by 0.5
enlargedImg = np.empty(enlargedShape, dtype=np.uint8)
rowScale = float(im.shape[0]) / float(enlargedImg.shape[0])
colScale = float(im.shape[1]) / float(enlargedImg.shape[1])
 
for r in range(enlargedImg.shape[0]):
	for c in range(enlargedImg.shape[1]):
		orir = r * rowScale 
		oric = c * colScale
		enlargedImg[r, c] = GetBilinearPixel(im, oric, orir)
cv2.imshow("Scaled Image - 0.5x",enlargedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

