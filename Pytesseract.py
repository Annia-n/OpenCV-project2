import cv2
import pytesseract

image_path = "/Users/anya/Downloads/photo_5825632626445240577_y.jpg"

img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

text = pytesseract.image_to_string(thresh, lang='eng')  

print(" text detected:")
print(text)

output_img = img.copy()
cv2.putText(output_img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

cv2.imshow("Image with OCR", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()