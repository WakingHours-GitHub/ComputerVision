import cv2 as cv
import numpy as np

cv.namedWindow("result", cv.WINDOW_NORMAL)
cv.resizeWindow("result", 640, 480)

back = cv.imread("cloud1.jpg")
img = cv.imread("./cloud2.jpg")

# 图像融合, 前提是两张图片形状相同
result = cv.addWeighted(back, 0.7, img, 0.3, 0 )

cv.imshow("result", result)

cv.waitKey(0)

cv.destroyAllWindows()

# 可见, 两张图片进行了不同程度的融合.





