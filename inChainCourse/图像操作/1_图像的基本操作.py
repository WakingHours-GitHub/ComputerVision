# pip install opencv
# 课程中是使用notebook进行开发的

# 下面简单介绍一些opencv中的东西
import cv2 # OpenCv默认读取的格式是BGR， 蓝绿红。
import matplotlib.pyplot as plt
import numpy as np

# 数据读取 -- 图片

img = cv2.imread('910709.jpg')
# 读取图像可选两种参数：
# IMREAD_COLOR # 彩色图像
# IMREAD_GRAYSCALE # 灰度图像

# print(type(img)) # numpy.ndarray对象


# 图像的显示， 也可以创建多个窗口
cv2.imshow('image', img) # 参数分别是显示的名字和要显示的内容
# 等待时间，毫秒级，0表水任意键终止, 就是在参数时间后窗口消失
cv2.waitKey(0)
cv2.destroyAllWindows() # 关闭所有窗口

print(img.shape) # (1080, 1920, 3),这三个参数分别是 h,w,c
# 这三个参数分别表示 高, 宽, 和色彩通道(彩色是RGB(Opencv是BGR)所以为3, 灰白是一个通道,所以c为1

img = cv2.imread('910709.jpg', cv2.IMREAD_GRAYSCALE)
print(img.shape) # (1080, 1920)

# 保存:
# 第一个参数是保存到文件的名字, 第二个参数是要保存的img
# cv2.imwrite('1.pnj',img)

print(type(img)) # <class 'numpy.ndarray'>
print(img.size) # 查看img的像素点的个数
print(img.dtype) # 查看数据的类型


# 数据读取--视频
'''
图像是一帧一帧的图片所组成的
那么我们首先要读入进来一段图像, 然后在读取一帧一帧的图片
然后我们在操作
'''
# videoCap = cv2.VideoWriter('test.mp4') # 路径名称
# # 检查是否正确打开
# if videoCap.isOpened(): # 检测视频是否正确打开
#     isopen, frame = videoCap.read() # read()读取当前视频信息, 返回两个参数
#     # 第一个参数是返回bool类型, frame返回的是当前帧的图像信息(就是矩阵)
# else:
#     isopen = False
#
# while isopen:
#     ret, frame = videoCap.read()
#     if frame is None: # 没有图像了
#         break
#     if ret == True: # 返回值为True时, 说明还有
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # cvtColor 是从一种颜色空间转换成另一种颜色空间
#         # COLoR_BGR2GRAY: 就是从BGR格式转到GRAY格式（灰度）
#         cv2.imshow('result', gray)
#         if cv2.waitKey(10) & 0xFF == 27: # 间隔10ms， 并且判断有无特殊输入符
#             break
# videoCap.release() # 释放
# cv2.destroyAllWindows() # 关闭所有打开窗口

# 截取部分图像的数据
# ROI操作： 你感兴趣的区域
img = cv2.imread('910709.jpg')
img = img[0:200, 0:200]
cv2.imshow('image', img)
