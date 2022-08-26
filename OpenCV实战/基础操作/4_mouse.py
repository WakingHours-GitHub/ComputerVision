import cv2 as cv
import numpy as np


# 定义鼠标回调函数.
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


WINDOW_NAME = "mouse"
# 创建桌面
cv.namedWindow(WINDOW_NAME, cv.WINDOW_NORMAL)
cv.resizeWindow(WINDOW_NAME, 640, 480)

# 设置鼠标回调, 绑定窗口
cv.setMouseCallback(WINDOW_NAME, mouse_callback, "123")

# 获取图像
img = np.zeros((480, 640, 3), np.uint8)  # 生成全黑图像
# 注意, 第一个参数是行, 也就是高, 第二个参数是列, 也就是宽

# 显示图像
while True:
    cv.imshow(WINDOW_NAME, img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
