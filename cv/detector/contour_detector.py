import cv2
import numpy as np
import logging
from .image_manager import ImageManager
from .contants import *

class ContourDetector:
    def __init__(self) -> None:
        self.img_manager = ImageManager()

    def detectContour(self):
        processed_image = self.img_manager.grayImg().blurImg((20, 20)).cropImg(STD_IMG_SIZE).getImg()
        ret, binary = cv2.threshold(processed_image, 100, 255, cv2.THRESH_OTSU)
        inverted_binary = ~ binary
        cv2.waitKey(0) 