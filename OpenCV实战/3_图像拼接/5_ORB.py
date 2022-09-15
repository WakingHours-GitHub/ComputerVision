import cv2 as cv
import numpy as np


img = cv.imread('chess.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 创建orb对象
orb = cv.ORB_create()

# 通过orb对象进行检测
kp, des = orb.detectAndCompute(
    img_gray, # 灰度图,
    None, # mask=None表示全部区域.
)

# 绘制key points
cv.drawKeypoints(
    image=img_gray, # 在那个图像中绘画
    keypoints=kp, # 特征点集
    outImage=img

)
cv.imshow("img", img)
cv.waitKey(0)

cv.destroyAllWindows()