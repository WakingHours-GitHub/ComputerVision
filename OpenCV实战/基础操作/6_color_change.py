import cv2 as cv

winname = "color"
trackbarname = "colorspace"
cv.namedWindow(winname, flags=cv.WINDOW_NORMAL)
cv.resizeWindow(winname, 640, 480)

color_space_list = [cv.COLOR_BGR2RGB, cv.COLOR_BGR2BGRA, cv.COLOR_BGR2GRAY, cv.COLOR_BGR2HSV,
                    cv.COLOR_BGR2YUV] # 格式转换队列
def callback():
    pass

# 创建Trackbar
cv.createTrackbar(trackbarname, winname, 0, len(color_space_list)-1, callback) # 注意, 这里len要-1. 否则列表越界

# 读取图片
img = cv.imread("test.jpg")

# 显示图像
while True:
    color_space_index = cv.getTrackbarPos(trackbarname, winname)

    # 颜色空间转换 -> cvtColor(src, colorSpace)颜色转换API
    cvt_img = cv.cvtColor(img, color_space_list[color_space_index])

    cv.imshow(winname, cvt_img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()




