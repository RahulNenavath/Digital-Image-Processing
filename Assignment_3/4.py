import cv2
from matplotlib import pyplot as plt
from skimage.exposure import match_histograms

dark_img = cv2.imread('../assets/pout-dark.jpg',0) # Source
bright_img = cv2.imread('../assets/pout-bright.jpg',0) # Reference

matched = match_histograms(dark_img, bright_img, multichannel=True)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()

ax1.imshow(dark_img)
ax1.set_title('Source')
ax2.imshow(bright_img)
ax2.set_title('Reference')
ax3.imshow(matched)
ax3.set_title('Matched')

plt.tight_layout()
plt.show()

