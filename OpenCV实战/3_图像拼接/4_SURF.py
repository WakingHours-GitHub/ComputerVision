import cv2 as cv
import numpy as np



# image read
img = cv.imread("chess.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# create SURF object
surf = cv.SURF_create()