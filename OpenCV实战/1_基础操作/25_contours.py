"""
图像轮廓.
    图像轮廓就是具有相同颜色或者强度的连续点的曲线。

"""
import cv2 as cv

# read image
img = cv.imread("contours_test.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# image binary
ret, img_bin = cv.threshold(
    img_gray,
    150,
    255,
    cv.THRESH_BINARY
)

# find contours

contours, hierarchy = cv.findContours(
    image=img_bin,
    # mode=cv.RETR_EXTERNAL,  # 表示按照什么模式进行查找。
    # EXTERNAL是只是找到最外层轮廓
    mode=cv.RETR_TREE,
    # 一般是按照tree进行查找, 这样方便知道什么轮廓是那个图案的.
    # 轮廓查找是, 从右到左, 从大到小去查找的.
    method=cv.CHAIN_APPROX_SIMPLE  # 就是逼近算法. 也就是返回的轮廓点集. 是什么模式的
    # NONE: 保存所有轮廓上的点.
    # SIMPLE只存储角点.
)  # 返回两个值. 一个是轮廓. 一个是轮廓的层级. 也就是检测出来的轮廓是否有层级关系.

# 通过findContours我们可以得到轮廓对应的坐标点, 以及对应的深度关系
print(contours)  #
# (array([[[  0,   0]],
#
#        [[  0, 535]],
#
#        [[470, 535]],
#
#        [[470,   0]]], dtype=int32),)
# 只是存储角点. 因此数据量就得到简化了.

# 绘制轮廓
cv.drawContours( # 绘制轮廓。
    image=img,  # 在那个图像上绘制图像, 这里使用原图, 在原图上绘制轮廓.
    contours=contours,  # 就是刚刚通过findContours查找到的轮廓点集.
    contourIdx=-1,  # 表示索引, 这个索引的顺序, 就是我们使用mode的方法查找的顺序. -1表示绘制所有轮廓.
    color=(0, 0, 255),  # 颜色
    thickness=1
)  # 直接就在img中画图, 不返回任何值

# show image
cv.imshow("img", img)

cv.waitKey(0)

cv.destroyAllWindows()
