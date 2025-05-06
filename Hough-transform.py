import cv2
import numpy as np


fruit_image = cv2.imread('/Users/anya/Desktop/opencv-project/Grayfruit.png', cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(fruit_image, (9, 9), 2)

circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=20,
    param1=100,
    param2=40,
    minRadius=10,
    maxRadius=100
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(fruit_image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(fruit_image, (x, y), 2, (0, 0, 255), 3)

else:
    print(" no circles detected")

cv2.imshow("Detected Circles", fruit_image)
cv2.waitKey(0)
cv2.destroyAllWindows()