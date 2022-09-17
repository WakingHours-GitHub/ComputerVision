import cv2 as cv
import numpy as np


img_search = cv.imread("opencv_search.png")
img_origin = cv.imread("opencv_origin.png")

# 灰度化：
img_search_gray = cv.cvtColor(img_search, cv.COLOR_BGR2GRAY)
img_origin_gray = cv.cvtColor(img_origin, cv.COLOR_BGR2GRAY)




