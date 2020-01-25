import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.util import random_noise

img = cv2.imread('../assets/Lenna.png',0)

def salt_pepper_noise(img):

	sum_ = 0

	for i in range(0,5):
		noise_img = random_noise(img, mode='s&p', amount=0.1)
		sum_ = sum_ + noise_img

	noise_img_1 = sum_ / 5
	noise_img_1 = np.array(255*sum_, dtype='uint8')
	X = np.concatenate((img, noise_img_1,), axis=1)

	for i in range(0,10):
		noise_img = random_noise(img, mode='s&p', amount=0.1)
		sum_ = sum_ + noise_img

	noise_img_2 = sum_ / 10
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')
	X = np.concatenate((X, noise_img_2), axis=1)

	for i in range(0,15):
		noise_img = random_noise(img, mode='s&p', amount=0.1)
		sum_ = sum_ + noise_img

	noise_img_3 = sum_ / 15
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')
	X = np.concatenate((X, noise_img_3), axis=1)

	for i in range(0,20):
		noise_img = random_noise(img, mode='s&p', amount=0.1)
		sum_ = sum_ + noise_img

	noise_img_4 = sum_ / 20
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')
	X = np.concatenate((X, noise_img_4), axis=1)

	for i in range(0,25):
		noise_img = random_noise(img, mode='s&p', amount=0.1)
		sum_ = sum_ + noise_img

	noise_img_5 = sum_ / 25
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')
	X = np.concatenate((X, noise_img_5), axis=1)

	for i in range(0,30):
		noise_img = random_noise(img, mode='s&p', amount=0.1)
		sum_ = sum_ + noise_img

	noise_img_6 = sum_ / 30
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')
	X = np.concatenate((X, noise_img_6), axis=1)

	return X

def Additive_Gaussian_noise(img):

	sum_ = 0

	for i in range(0,5):
		noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_1 = sum_ / 5
	noise_img_1 = np.array(255*sum_, dtype='uint8')
	X = np.concatenate((img, noise_img_1,), axis=1)

	for i in range(0,10):
		noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_2 = sum_ / 10
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')
	X = np.concatenate((X, noise_img_2), axis=1)

	for i in range(0,15):
		noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_3 = sum_ / 15
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')
	X = np.concatenate((X, noise_img_3), axis=1)

	for i in range(0,20):
		noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_4 = sum_ / 20
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')
	X = np.concatenate((X, noise_img_4), axis=1)

	for i in range(0,25):
		noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_5 = sum_ / 25
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')
	X = np.concatenate((X, noise_img_5), axis=1)

	for i in range(0,30):
		noise_img = random_noise(img, mode='gaussian', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_6 = sum_ / 30
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')
	X = np.concatenate((X, noise_img_6), axis=1)

	return X

def Speckle_noise(img):

	sum_ = 0

	for i in range(0,5):
		noise_img = random_noise(img, mode='speckle', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_1 = sum_ / 5
	noise_img_1 = np.array(255*sum_, dtype='uint8')
	X = np.concatenate((img, noise_img_1,), axis=1)

	for i in range(0,10):
		noise_img = random_noise(img, mode='speckle', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_2 = sum_ / 10
	noise_img_2 = np.array(255*noise_img_2, dtype='uint8')
	X = np.concatenate((X, noise_img_2), axis=1)

	for i in range(0,15):
		noise_img = random_noise(img, mode='speckle', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_3 = sum_ / 15
	noise_img_3 = np.array(255*noise_img_3, dtype='uint8')
	X = np.concatenate((X, noise_img_3), axis=1)

	for i in range(0,20):
		noise_img = random_noise(img, mode='speckle', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_4 = sum_ / 20
	noise_img_4 = np.array(255*noise_img_4, dtype='uint8')
	X = np.concatenate((X, noise_img_4), axis=1)

	for i in range(0,25):
		noise_img = random_noise(img, mode='speckle', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_5 = sum_ / 25
	noise_img_5 = np.array(255*noise_img_5, dtype='uint8')
	X = np.concatenate((X, noise_img_5), axis=1)

	for i in range(0,30):
		noise_img = random_noise(img, mode='speckle', mean=0, var=0.01)
		sum_ = sum_ + noise_img

	noise_img_6 = sum_ / 30
	noise_img_6 = np.array(255*noise_img_6, dtype='uint8')
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

else:
	print("Not a valid choice")

