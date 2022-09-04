import cv2 as cv
import numpy as np


img = cv.imread("test.jpg")
img_clockwish90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
img_clockwish180 = cv.rotate(img, cv.ROTATE_180)
img_clockwish270 = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

cv.imshow("img", img)
cv.imshow("img_clockwish90", img_clockwish90 )
cv.imshow("img_clockwish180",  img_clockwish180)
cv.imshow("img_clockwish270", img_clockwish270)
cv.waitKey(0)

cv.destroyAllWindows()



