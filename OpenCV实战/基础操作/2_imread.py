import cv2 as cv

cv.namedWindow('img', cv.WINDOW_NORMAL)
img = cv.imread("./test.jpg")  # 返回Mat数据类型的数据

# 展示, 实际上就是指定哪个图片在哪个窗口中显示
cv.imshow('img', img)
key = cv.waitKey(0)
if key == 'q':
    exit()
cv.destroyAllWindows()  # destroy all windows
