



import cv2 as cv
import numpy as np

# read image
img = cv.imread("contours1.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# image binary
res, img_bin = cv.threshold(
    img,
    150,
    255,
    cv.THRESH_BINARY
)

# 查找轮廓
















