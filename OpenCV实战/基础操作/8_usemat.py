import cv2 as cv
import numpy
import numpy as np


img = cv.imread("./test.jpg")
print(type(img)) # <class 'numpy.ndarray'>
# 可见, 在python中, 从cv读进来的图片, 直接就转换成numpy中的ndarray数组.

# 浅拷贝
img2 = img # 默认均是浅拷贝

# 深拷贝
img3 = img.copy() # 显示的使用深拷贝.
# 将data区域拷贝一份

# 修改img原始图片
img[200: 300, 200: 300, :] = [0, 0, 255]

# 显示图片
cv.imshow("img", img)
cv.imshow("img2", img2)
cv.imshow("img3", img3)
# 可见, 当使用浅拷贝时, 共享数据区域.

cv.waitKey(0)

cv.destroyAllWindows()


