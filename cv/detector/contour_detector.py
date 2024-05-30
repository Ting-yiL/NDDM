import cv2
import numpy as np
import logging
from .image_manager import ImageManager
from .contants import *

class ContourDetector:
    def __init__(self) -> None:
        self.img_manager = ImageManager()

    def reject_outliers(self, data:np.ndarray, m=0.5): 
        return [abs(data - np.mean(data)) < m * np.std(data)]

    def detectContour(self):
        processed_image = self.img_manager.grayImg().blurImg((100, 100)).resizeImgStd().getImg()
        ret, binary = cv2.threshold(processed_image, 100, 255, cv2.THRESH_OTSU)
        inverted_binary = ~ binary
        contours, hierarchy = cv2.findContours(inverted_binary,
                                               cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
        with_contours = cv2.drawContours(processed_image, contours, -1,(255,0,255),3)

        screened_contours = self.reject_outliers(np.array(list(map(cv2.contourArea, contours))))[0]

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            if (cv2.contourArea(c)) > 10:
                cv2.rectangle(with_contours,(x,y), (x+w,y+h), (255,0,0), 5)

        cv2.imshow('Detected contours', with_contours)
        cv2.waitKey(0)