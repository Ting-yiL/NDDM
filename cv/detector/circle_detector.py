import cv2
import numpy as np
import logging

STD_IMG_SIZE = ()

class CircleDetector:
    def __init__(self) -> None:
        self.img = None

    def readImg(self, path):
        try:
           self.img = cv2.imread(path, cv2.IMREAD_COLOR)
        except Exception as e:
            logging.error(e) 
        self.img = self.cvt2Gray(self.img)

    def cvt2Gray(self, image):
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            return gray
        except Exception as e:
            logging.error(e)

    def image_masking(self, image, a, b, r):
        mask1 = np.zeros_like(image)
        mask1 = cv2.circle(mask1, (a, b), r, (255,255,255), -1)

        result = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        result[:, :, 3] = image[:,:,0]

        return cv2.bitwise_and(mask1, image)
    
    def contourDetection():
        pass
                  
    def inspectSingleCircle(self, image):
        r_image = cv2.resize(image, (550, 550))

        gray_blurred = cv2.blur(r_image, (6, 6)) 
  
        detected_circles = cv2.HoughCircles(gray_blurred,  
                        cv2.HOUGH_GRADIENT, 1, 300, 45, param1 = 75, 
                    param2 = 40, minRadius = 100, maxRadius = 200) 

        if detected_circles is not None and len(detected_circles) != 0: 
            detected_circles = np.uint16(np.around(detected_circles)) 
            print(detected_circles)
            pt = detected_circles[0][0]
            
            a, b, r = pt[0], pt[1], pt[2] 
    
            cv2.circle(self.img, (a, b), r, (0, 255, 0), 2) 
            cv2.circle(self.img, (a, b), 1, (0, 0, 255), 3) 

            cv2.imshow("Detected Circle", self.img) 
            cv2.imshow("Cropped Circle", self.image_masking(self.img, a, b, r)) 

            cv2.waitKey(0) 


if __name__== "__main__":
    circle_detector = CircleDetector()