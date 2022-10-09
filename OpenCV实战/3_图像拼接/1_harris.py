"""
Harris角点.
哈里斯角点检测:
三种状况:
    1. 一种是平坦区域.
    2. 一种是沿边缘进行移动, 那么x轴方向进行sobel运算则不会变.
    3. 如果已经在角点上时, 那么无论角点, 往那个方向上变换, 那么像素都会发生变化.




"""

import cv2 as cv
import numpy as np


img = cv.imread("./chess.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 使用harris角点检测:
img_harris = cv.cornerHarris(
    src=img_gray,
    blockSize=5,
    ksize=5, # sobel的卷积核
    k=0.04 # 权重系数
)

# show image
cv.imshow("harris", img_harris)

cv.waitKey(0)

cv.destroyAllWindows()






