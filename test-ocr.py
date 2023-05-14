import cv2
img = cv2.imread('./detected2/xs_1.jpg')


from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

result = ocr.ocr(img, cls=True)


for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

