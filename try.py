import cv2
import numpy as np
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
img = cv2.imread('a.jpg')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(_, blackWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
blackWhiteImage = cv2.copyMakeBorder(src=blackWhiteImage, top=100, bottom=100, left=50, right=50, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))
blackWhiteImage = cv2.morphologyEx(blackWhiteImage, cv2.MORPH_CLOSE, np.ones((3,3),np.uint8))
cv2.imshow('Image result', blackWhiteImage)
cv2.waitKey(0)
data = pytesseract.image_to_data(blackWhiteImage, config="-c tessedit_char_whitelist=0123456789 --psm 7")
originalImage = cv2.cvtColor(blackWhiteImage, cv2.COLOR_GRAY2BGR)

text = []
for z, a in enumerate(data.splitlines()):
    if z != 0:
        a = a.split()
        if len(a) == 12:
            x, y = int(a[6]), int(a[7])
            w, h = int(a[8]), int(a[9])
            cv2.rectangle(originalImage, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(originalImage, a[11], (x, y - 2), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)
            text.append(a[11]);

print("Text result: \n", text)
