import cv2 as cv
import numpy as np

img = cv.imread('test.jpg')

# shape: 查看图片形状
# 返回值为元组, 分别是高度, 长度(宽)和通道数.
print(img.shape)

# size: 图像占用多大空间
# 高 * 宽 * 通道
print(img.size)

# 图像中每个元素(像素)的数据类型, 其实也就是位深.
print(img.dtype) # uint8










