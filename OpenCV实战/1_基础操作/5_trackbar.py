import cv2 as cv
import numpy as np


def callback():
    pass

winname = "trackbar"
cv.namedWindow(winname, cv.WINDOW_NORMAL)
cv.resizeWindow(winname, 640, 480)



# 创建trackbar控件
# argument:
# trackbarname, winname, value, count, callback, userdata
cv.createTrackbar('R', winname, 0, 255, callback)
cv.createTrackbar('G', winname, 0, 255, callback)
cv.createTrackbar('B', winname, 0, 255, callback)

# 创建初始图像
img = np.zeros(shape=(640, 480, 3), dtype=np.uint8)

# 显示图像：
while True:
    # 读取控件值:
    r = cv.getTrackbarPos('R', winname)
    g = cv.getTrackbarPos('G', winname)
    b = cv.getTrackbarPos('B', winname)

    # 然后赋值给这个图像中去
    img[:] = [b, g, r]
    # 这里的两个细节.
    # 首先是img[:]表示, img全部图像, 赋值给全部.
    # 然后就是b,g,r这个通道数, 在opencv中, rgb通道数是反过来的

    # 显示图像
    cv.imshow(winname, img)

    # 等待键盘
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()







