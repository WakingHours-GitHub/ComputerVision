import cv2 as cv
import numpy as np

# image read
img_search = cv.imread("opencv_search.png")
img_origin = cv.imread("opencv_origin.png")

# 创建sift对象
sift = cv.SIFT_create()

# 进行检测, 两张图都要检测:
kp_search, des_search = sift.detectAndCompute(img_search, None)
kp_origin, des_origin = sift.detectAndCompute(img_origin, None)

# 创建匹配器:
bf = cv.BFMatcher(
    cv.NORM_L1,  # 关键点检测算法使用的是SIFT, 对应, 这里就要使用NORM_L2
    crossCheck=False # 不进行交叉验证.
)

match = bf.match(des_search, des_origin) # 返回一个匹配结果.

# 画出图像:
img_matches = cv.drawMatches(
    img_search,
    kp_search,
    img_origin,
    kp_origin,
    matches1to2=match,
    outImg=None # 输出图像
)

# show result
cv.imshow("img", img_matches)

cv.waitKey(0)

cv.destroyAllWindows()








