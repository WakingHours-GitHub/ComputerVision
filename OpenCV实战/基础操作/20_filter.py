"""
卷积

"""
import cv2 as cv
import  numpy as np


def filter2D():
    img = cv.imread("test.jpg")

    # create kernel
    kernel = np.ones( # 全1卷积核. 平滑.
        shape=(5, 5),
        dtype=np.float32 # 类型仍然是float32
    ) / 25

    # 卷积:
    dst = cv.filter2D(
        src=img, # 原始图像
        ddepth=-1, # -1表示和原图一样深度
        kernel=kernel # 卷积核.
    )

    # show image
    cv.imshow("img", img)
    cv.imshow("dst", dst)

    # window operation
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    filter2D()

