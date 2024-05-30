from detector.circle_detector import CircleDetector
from detector.contour_detector import ContourDetector

'''
cd2 = CircleDetector()
cd2.readImg(r"./resources/images/N45/NG/NG_group1.jpg")
cd2.readImg(r"./resources/images/N45/NG/NG1.jpg")
cd2.inspectSingleCircle()
'''

'''
cd1 = CircleDetector()
cd1.readImg(r"./resources/images/N45/NG/NG_group1.jpg")
cd2 = ContourDetector()
cd2.detectContour(cd1.img)

'''
cd2 = ContourDetector()
cd2.img_manager.readImg(r"./resources/images/N45/OK/OK1.jpg")
cd2.detectContour()