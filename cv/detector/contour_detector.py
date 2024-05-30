import cv2
import numpy as np
import logging

class ContourDetector:
    def __init__(self) -> None:
        pass

    def detectContour(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_blurred = cv2.blur(gray, (10, 10)) 
        cv2.imshow("gray_blurred", gray_blurred) 
        cv2.waitKey(0) 