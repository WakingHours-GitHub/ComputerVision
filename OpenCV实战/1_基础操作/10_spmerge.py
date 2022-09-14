import cv2 as cv

# read figure
img = cv.imread("test.jpg")

# 分割:
b, g, r = cv.split(img)
# 分离出来的b,g,r每一个都是一个单个矩阵.

b[100: 200, 100: 200] = 255
g[100: 200, 100: 200] = 255

img_merge = cv.merge((b, g, r)) # opencv的读取通道数为bgr, 因此合并的时候也需要使用这个顺序


cv.imshow("img", img)
cv.imshow('b', b) # 因为是单个通道所以也就没有颜色了.
cv.imshow('g', g)
cv.imshow('img_merge', img_merge)
# 可以看见, 因为将b和g通道设置为255, 组合在一起就是青色.
cv.waitKey(0)

cv.destroyAllWindows()



