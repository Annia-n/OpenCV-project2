import cv2
import numpy as np
import matplotlib.pyplot as plt


fruit_image = cv2.imread('/Users/anya/Desktop/opencv-project/Grayfruit.png', cv2.IMREAD_GRAYSCALE)

canny_low = cv2.Canny(fruit_image, 50, 150)
canny_high = cv2.Canny(fruit_image, 100, 200)

titles = ['Original Image', 'Canny (50,150)', 'Canny (100,200)']
images = [fruit_image, canny_low, canny_high]


plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
