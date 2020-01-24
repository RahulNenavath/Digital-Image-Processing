import cv2

#cv2.imread('Image_name', flag)

#Flag determines how the images are opened. Three flags are available: 
#                  -1: Read the unchanged image, including alpha channels, 
#                   0: Read as Grayscale image
#                   1: Read the Color image 

img = cv2.imread('../assets/Lenna.png',0)

cv2.imshow('Image', img)

k = cv2.waitKey(0) and 0xFF 

if k == 27: # close window when esc key is pressed
  cv2.destroyAllWindows()

elif k == ord('s'): # writes a file when 'S' is pressed (To save) then closes
	cv2.imwrite('../assets/Lenna_grayscale.png', img)
	cv2.destroyAllWindows()