from PIL import Image
import pytesseract
import numpy as np
import cv2


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

video=cv2.VideoCapture(0)

while True:
    hasFrame, image = video.read()

    img1 = np.array(image)
    text = pytesseract.image_to_string(img1)
    if len(text)>3:
        print("Text is ",text)
        break

    # cv2.imshow("object detection", image)
    # cv2.waitKey()

# filename = 'sample5.png'
#
# # import cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
# # img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
# # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
# # img = cv2.GaussianBlur(img, (1, 1), 0)
#
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)
# print(text)

