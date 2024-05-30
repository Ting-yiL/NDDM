import cv2
import logging

class ImageManager():
    def __init__(self) -> None:
        self.img = None
        self.og_img = None

    def setImg(self, image):
        '''
        Sets current image.

        Parameters:
            image (numpy.ndarray): The image

        Returns:
            None
        '''
        self.img = image
        self.og_img = image
    
    def getImg(self):
        return self.img

    def readImg(self, path):
        '''
        Reads the image from the given path.

        Parameters:
            path (str): The path of the image.

        Returns:
            None
        '''
        try:
            self.setImg(cv2.imread(path, cv2.IMREAD_COLOR))
        except Exception as e:
            logging.error(e) 

    def resizeImg(self, scale):
        self.img =  cv2.resize(self.img, scale)
    
    def cropImg(self, dim):
        self.img =  self.img[0:dim[0], 0:dim[1]]

    def grayImg(self):
        '''
        Converts the image to a grayscale image.

        Parameters:
            None

        Returns:
            The grayscale image.
        '''
        try:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            logging.error(e)
    
    def blurImg(self, scale):
        self.img = cv2.blur(self.img, (6, 6)) 

    def resetImg(self):
        self.img = self.og_img

if __name__== "__main__":
    image_manager = ImageManager()