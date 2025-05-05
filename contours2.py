import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
fruit_image = cv2.imread('/Users/anya/Desktop/opencv-project/Grayfruit.png', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(fruit_image, (5, 5), 0)

# Use binary inverse thresholding
_, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on BGR image
contour_img = cv2.cvtColor(fruit_image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

print("Number of objects detected:", len(contours))

# Show results
titles = ['Original', 'Threshold', 'Contours']
images = [fruit_image, thresh, contour_img]

plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray' if i < 2 else None)
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()