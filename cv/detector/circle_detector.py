import cv2
import numpy as np
import logging
from .image_manager import ImageManager

STD_IMG_SIZE = (550, 550)

class CircleDetector:
    def __init__(self) -> None:
        self.img_manager = ImageManager()

    def image_masking(self, image, a, b, r):
        mask1 = np.zeros_like(image)
        mask1 = cv2.circle(mask1, (a, b), r, (255,255,255), -1)

        result = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        result[:, :, 3] = image[:,:,0]

        return cv2.bitwise_and(mask1, image)
                  
    def inspectSingleCircle(self):
        self.img_manager.cropImg(STD_IMG_SIZE)
        self.img_manager.grayImg()
        self.img_manager.blurImg((6, 6))
  
        detected_circles = cv2.HoughCircles(self.img_manager.getImg(),  
                        cv2.HOUGH_GRADIENT, 1, 300, 45, param1 = 75, 
                    param2 = 40, minRadius = 100, maxRadius = 200) 
        
        self.img_manager.resetImg()

        if detected_circles is not None and isinstance(detected_circles[0][0], np.ndarray): 
            detected_circles = np.uint16(np.around(detected_circles)) 
            pt = detected_circles[0][0]

            a, b, r = pt[0], pt[1], pt[2] 
    
            cv2.circle(self.img_manager.getImg(), (a, b), r, (0, 255, 0), 2) 
            cv2.circle(self.img_manager.getImg(), (a, b), 1, (0, 0, 255), 3) 

            cv2.imshow("Detected Circle", self.img_manager.getImg()) 
            cv2.imshow("Cropped Circle", self.image_masking(self.img_manager.getImg(), a, b, r)) 

            cv2.waitKey(0) 
        else:
            logging.warning('No circle is detected...')


if __name__== "__main__":
    circle_detector = CircleDetector()