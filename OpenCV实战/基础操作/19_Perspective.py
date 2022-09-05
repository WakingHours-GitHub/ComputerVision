import cv2 as cv
import numpy as np

# read image
img = cv.imread("perspective_test.jpg")

# get M
src = np.float32([
    # 这些具体坐标可以通过画图工具, 里面可以查看像素位置, 不过工具是从1开始, 因此我们还需要-1
    [443 - 1, 385 - 1],  # 左上
    [1320 - 1, 374 - 1],  # 右上
    [454 - 1, 893 - 1],  # 左下
    [1338 - 1, 860 - 1]  # 右下
])
dst = np.float32([
    [0, 0],
    [1706, 0],
    [0, 1280],
    [1706, 1280],
])
M = cv.getPerspectiveTransform(src, dst)
# perspective transform
new_img = cv.warpPerspective(img, M, dsize=(None, None) )

# show image
cv.imshow("img", img)
cv.imshow("new_img", new_img)

cv.waitKey(0)

cv.destroyAllWindows()



