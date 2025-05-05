import cv2
import numpy as np
import matplotlib.pyplot as plt


fruit_image = cv2.imread('/Users/anya/Desktop/opencv-project/Grayfruit.png', cv2.IMREAD_GRAYSCALE)
_, simple_treshold = cv2.threshold(fruit_image, 127, 255, cv2.THRESH_BINARY)

adaptive_treshold = cv2.adaptiveThreshold(fruit_image, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY,
                                    11,
                                    2)

titles = ['Original Image', 'Simple Threshold', 'Adaptive Threshold']
images = [fruit_image, simple_treshold, adaptive_treshold]


plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
