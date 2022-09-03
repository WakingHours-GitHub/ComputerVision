import cv2 as cv
import numpy as np

pic1 = cv.imread("./test.jpg")

print(pic1.shape) # (1080, 1620, 3)
# 显示原始图片
cv.imshow("origin", pic1)

# 创建相同大小的全1 矩阵。
pic2 = np.ones_like(pic1, dtype=np.uint8) * 100 #  默认是对每个元素进行运算

result_add = cv.add(pic1, pic2)
result_sub = cv.subtract(pic1, pic2)

cv.imshow("result_add", result_add)
cv.imshow("result_sub", result_sub)


cv.waitKey(0)

cv.destroyAllWindows()
# 可见, 在每个元素值加起来, 会有一些曝光的感觉, 即每个像素点的灰度值都增加了.
# 图像的减法运算, 就是将图片中对应位置的元素, 减去一个灰度值, 所以图片变得暗淡了







