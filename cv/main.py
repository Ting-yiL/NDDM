from detector.circle_detector import CircleDetector
import cv2

'''
for i in range(10):
    cd1 = CircleDetector()
    cd1.readImg(rf"./resources/images/N45/NG/NG{i}.jpg")
    cd1.detectCircle()
'''



cd2 = CircleDetector()
cd2.readImg(r"./resources/images/N45/NG_group.jpg")
cd2.detectCircle()