import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.util import random_noise

img = cv2.imread('../assets/Lenna.png',0)

def salt_pepper_noise(img):

	noise_img_1 = random_noise(img, mode='s&p', amount=0.1)
	noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	for i in range(0,4):
		noise_img_1 = random_noise(noise_img_1, mode='s&p', amount=0.1)
		noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	noise_img_1 = noise_img_1 / 5
	noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/S&P/s&p_Lenna_1.png', noise_img_1)

	X = np.concatenate((img, noise_img_1,), axis=1)


	noise_img_2 = random_noise(img, mode='s&p', amount=0.1)
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')
	
	for i in range(0,9):
		noise_img_2 = random_noise(noise_img_2, mode='s&p', amount=0.1)
		noise_img_2 = np.array(255*noise_img_2, dtype='uint8')

	noise_img_2 = noise_img_2 / 10
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/S&P/s&p_Lenna_2.png', noise_img_2)

	X = np.concatenate((X, noise_img_2), axis=1)

	noise_img_3 = random_noise(img, mode='s&p', amount=0.1)
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')
	
	for i in range(0,14):
		noise_img_3 = random_noise(noise_img_3, mode='s&p', amount=0.1)
		noise_img_3 = np.array(255*noise_img_3, dtype='uint8')

	noise_img_3 = noise_img_3 / 15
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/S&P/s&p_Lenna_3.png', noise_img_3)

	X = np.concatenate((X, noise_img_3), axis=1)

	noise_img_4 = random_noise(img, mode='s&p', amount=0.1)
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')
	
	for i in range(0,19):
		noise_img_4 = random_noise(noise_img_4, mode='s&p', amount=0.1)
		noise_img_4 = np.array(255*noise_img_4, dtype='uint8')

	noise_img_4 = noise_img_4 / 20
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/S&P/s&p_Lenna_4.png', noise_img_4)

	X = np.concatenate((X, noise_img_4), axis=1)

	noise_img_5 = random_noise(img, mode='s&p', amount=0.1)
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')
	
	for i in range(0,24):
		noise_img_5 = random_noise(noise_img_5, mode='s&p', amount=0.1)
		noise_img_5 = np.array(255*noise_img_5, dtype='uint8')

	noise_img_5 = noise_img_5 / 25
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/S&P/s&p_Lenna_5.png', noise_img_5)

	X = np.concatenate((X, noise_img_5), axis=1)


	noise_img_6 = random_noise(img, mode='s&p', amount=0.1)
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')
	
	for i in range(0,29):
		noise_img_6 = random_noise(noise_img_6, mode='s&p', amount=0.1)
		noise_img_6 = np.array(255*noise_img_6, dtype='uint8')

	noise_img_6 = noise_img_6 / 30
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/S&P/s&p_Lenna_6.png', noise_img_6)

	X = np.concatenate((X, noise_img_6), axis=1)

	return X


	# sumNoise_img = (noise_img_1 + noise_img_2 + noise_img_3 + noise_img_4 + noise_img_5 + noise_img_6)
	# sumNoise_img = np.array(255*sumNoise_img, dtype='uint8')

	# avgNoise_img = sumNoise_img / 6
	# avgNoise_img = np.array(255*avgNoise_img, dtype='uint8')

	# cv2.imwrite('../assets/Assignment_2/S&P/AVG_s&p_Lenna.png', avgNoise_img)



def Additive_Gaussian_noise(img):

	noise_img_1 = random_noise(img, mode='gaussian', mean=0, var=0.01)
	noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	for i in range(0,4):
		noise_img_1 = random_noise(noise_img_1, mode='gaussian', mean=0, var=0.01)
		noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	noise_img_1 = noise_img_1 / 5
	noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Gaussian/gaussian_Lenna_1.png', noise_img_1)
	X = np.concatenate((img, noise_img_1,), axis=1)

	noise_img_2 = random_noise(img, mode='gaussian', mean=0, var=0.01)
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')
	
	for i in range(0,9):
		noise_img_2 = random_noise(noise_img_2, mode='gaussian', mean=0, var=0.01)
		noise_img_2 = np.array(255*noise_img_2, dtype='uint8')

	noise_img_2 = noise_img_2 / 10
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Gaussian/gaussian_Lenna_2.png', noise_img_2)
	X = np.concatenate((X, noise_img_2), axis=1)

	noise_img_3 = random_noise(img, mode='gaussian', mean=0, var=0.01)
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')
	
	for i in range(0,14):
		noise_img_3 = random_noise(noise_img_3, mode='gaussian', mean=0, var=0.01)
		noise_img_3 = np.array(255*noise_img_3, dtype='uint8')

	noise_img_3 = noise_img_3 / 15
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Gaussian/gaussian_Lenna_3.png', noise_img_3)
	X = np.concatenate((X, noise_img_3), axis=1)

	noise_img_4 = random_noise(img, mode='gaussian', mean=0, var=0.01)
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')
	
	for i in range(0,19):
		noise_img_4 = random_noise(noise_img_4, mode='gaussian', mean=0, var=0.01)
		noise_img_4 = np.array(255*noise_img_4, dtype='uint8')

	noise_img_4 = noise_img_4 / 20
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Gaussian/gaussian_Lenna_4.png', noise_img_4)
	X = np.concatenate((X, noise_img_4), axis=1)


	noise_img_5 = random_noise(img, mode='gaussian', mean=0, var=0.01)
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')
	
	for i in range(0,24):
		noise_img_5 = random_noise(noise_img_5,mode='gaussian', mean=0, var=0.01)
		noise_img_5 = np.array(255*noise_img_5, dtype='uint8')

	noise_img_5 = noise_img_5 / 25
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Gaussian/gaussian_Lenna_5.png', noise_img_5)
	X = np.concatenate((X, noise_img_5), axis=1)

	noise_img_6 = random_noise(img, mode='gaussian', mean=0, var=0.01)
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')
	
	for i in range(0,29):
		noise_img_6 = random_noise(noise_img_6,mode='gaussian', mean=0, var=0.01)
		noise_img_6 = np.array(255*noise_img_6, dtype='uint8')

	noise_img_6 = noise_img_6 / 30
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Gaussian/gaussian_Lenna_6.png', noise_img_6)
	X = np.concatenate((X, noise_img_6), axis=1)

	# sumNoise_img = (noise_img_1 + noise_img_2 + noise_img_3 + noise_img_4 + noise_img_5 + noise_img_6)
	# sumNoise_img = np.array(255*sumNoise_img, dtype='uint8')

	# avgNoise_img = sumNoise_img / 6
	# avgNoise_img = np.array(255*avgNoise_img, dtype='uint8')

	# cv2.imwrite('../assets/Assignment_2/Gaussian/AVG_guassian_Lenna.png', avgNoise_img)

	return X

def Speckle_noise(img):

	noise_img_1 = random_noise(img, mode='speckle', mean=0, var=0.01)
	noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	for i in range(0,4):
		noise_img_1 = random_noise(noise_img_1, mode='speckle', mean=0, var=0.01)
		noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	noise_img_1 = noise_img_1 / 5
	noise_img_1 = np.array(255*noise_img_1, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Speckle/speckle_Lenna_1.png', noise_img_1)
	X = np.concatenate((img, noise_img_1,), axis=1)

	noise_img_2 = random_noise(img, mode='speckle', mean=0, var=0.01)
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')
	
	for i in range(0,9):
		noise_img_2 = random_noise(noise_img_2, mode='speckle', mean=0, var=0.01)
		noise_img_2 = np.array(255*noise_img_2, dtype='uint8')

	noise_img_2 = noise_img_2 / 10
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Speckle/speckle_Lenna_2.png', noise_img_2)
	X = np.concatenate((X, noise_img_2), axis=1)

	noise_img_3 = random_noise(img, mode='speckle', mean=0, var=0.01)
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')
	
	for i in range(0,14):
		noise_img_3 = random_noise(noise_img_3, mode='speckle', mean=0, var=0.01)
		noise_img_3 = np.array(255*noise_img_3, dtype='uint8')

	noise_img_3 = noise_img_3 / 15
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Speckle/speckle_Lenna_3.png', noise_img_3)
	X = np.concatenate((X, noise_img_3), axis=1)

	noise_img_4 = random_noise(img, mode='speckle', mean=0, var=0.01)
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')
	
	for i in range(0,19):
		noise_img_4 = random_noise(noise_img_4, mode='speckle', mean=0, var=0.01)
		noise_img_4 = np.array(255*noise_img_4, dtype='uint8')

	noise_img_4 = noise_img_4 / 20
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Speckle/speckle_Lenna_4.png', noise_img_4)
	X = np.concatenate((X, noise_img_4), axis=1)


	noise_img_5 = random_noise(img, mode='speckle', mean=0, var=0.01)
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')
	
	for i in range(0,24):
		noise_img_5 = random_noise(noise_img_5,mode='speckle', mean=0, var=0.01)
		noise_img_5 = np.array(255*noise_img_5, dtype='uint8')

	noise_img_5 = noise_img_5 / 25
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Speckle/speckle_Lenna_5.png', noise_img_5)
	X = np.concatenate((X, noise_img_5), axis=1)

	noise_img_6 = random_noise(img, mode='speckle', mean=0, var=0.01)
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')
	
	for i in range(0,29):
		noise_img_6 = random_noise(noise_img_6,mode='speckle', mean=0, var=0.01)
		noise_img_6 = np.array(255*noise_img_6, dtype='uint8')

	noise_img_6 = noise_img_6 / 30
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')

	#cv2.imwrite('../assets/Assignment_2/Speckle/speckle_Lenna_6.png', noise_img_6)
	X = np.concatenate((X, noise_img_6), axis=1)

	return X

print("Enter Which Noise should be added on the Lenna image?")
request = int(input('1) Salt and Pepper Noise 2) Additive Gaussian Noise 3) Speckle Noise : '))

if request == 1:

	X = salt_pepper_noise(img)
	plt.imshow(X)
	plt.show()

elif request == 2:

	X = Additive_Gaussian_noise(img)
	plt.imshow(X)
	plt.show()

elif request == 3:

	X = Speckle_noise(img)
	plt.imshow(X)
	plt.show()









