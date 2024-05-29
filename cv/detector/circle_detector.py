import cv2
import numpy as np
import logging

class CircleDetector:
    def __init__(self) -> None:
        self.img = None
        self.gray = None

    def readImg(self, path):
        try:
           self.img = cv2.imread(path, cv2.IMREAD_COLOR)
        except Exception as e:
            logging.error(e) 
        
        self.self2Gray()

    def self2Gray(self):
        try:
            self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            logging.error(e)

    def cvt2Gray(self, image):
        try:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            logging.error(e)
    
    def showGrayImg(self):
        pass
                  
    def detectCircle(self):
        gray_blurred = cv2.blur(self.gray, (5, 5)) 
  
        detected_circles = cv2.HoughCircles(gray_blurred,  
                        cv2.HOUGH_GRADIENT, 1, 300, 20, param1 = 75, 
                    param2 = 40, minRadius = 100, maxRadius = 200) 
        '''
        cv2.imshow("Detected Circle", gray_blurred) 
        cv2.waitKey(0) 
        '''

        if detected_circles is not None: 
            detected_circles = np.uint16(np.around(detected_circles)) 

            for pt in detected_circles[0, :]: 
                a, b, r = pt[0], pt[1], pt[2] 
        
                cv2.circle(self.img, (a, b), r, (0, 255, 0), 2) 
        
                cv2.circle(self.img, (a, b), 1, (0, 0, 255), 3) 
                cv2.imshow("Detected Circle", self.img) 
                cv2.waitKey(0) 

if __name__== "__main__":
    circle_detector = CircleDetector()