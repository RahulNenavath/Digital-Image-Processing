import cv2

# To play any video from the file or capture the live feed from the camera.

# cap = cv2.VideoCapture(0) # Arguments: 'my_video.mp4' for playing the video from file, 0 or -1 for capturing live feed from the camera. 0 and 1 here is the index where the camera device is stored

# # To capture the live feed from the camera:

# print(cap.isOpened())
# while(cap.isOpened()):
#   ret, frame = cap.read() # ret -> true/false if the frame is availale to capture, frame -> frame captured from the read method.

#   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts the live color feed to gray scale video

#   cv2.imshow('Camera',gray)
  
#   #cv2.imshow('Camera',frame) # colored original image

#   #cap.get(cv2.CAP_PROP_FRAME_WIDTH) # To get the width of the frame
#   #cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # To get the height of the frame

#   if (cv2.waitKey(1) and 0xFF) == ord('q'):
#   	break

# cap.release() # After reading the video, always release the object
# cv2.destroyAllWindows()


# To capture the live feed and save the video

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../assets/output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):
  ret, frame = cap.read()

  if ret == True:
  	print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  	print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  	out.write(frame)

  	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  	cv2.imshow('Camera',gray)

  	if (cv2.waitKey(1) and 0xFF) == ord('q'):
  		break
  else:
  	break

cap.release()
out.release()
cv2.destroyAllWindows()
		