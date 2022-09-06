"""
卷积

"""
import cv2 as cv
import numpy as np


def filter2D() -> None:
    img = cv.imread("test.jpg")

    # create kernel
    kernel = np.ones(  # 全1卷积核. 平滑.
        shape=(5, 5),
        dtype=np.float32  # 类型仍然是float32
    ) / 25

    # 卷积:
    dst = cv.filter2D(
        src=img,  # 原始图像
        ddepth=-1,  # -1表示和原图一样深度
        kernel=kernel  # 卷积核.
    )

    # show image
    cv.imshow("img", img)
    cv.imshow("dst", dst)

    # window operation
    cv.waitKey(0)
    cv.destroyAllWindows()


def boxFilter() -> None:
    img = cv.imread("test.jpg")

    # 方盒卷积
    dst1 = cv.boxFilter(
        src=img,
        ddepth=-1,  # -1表示位深和原图相同.
        ksize=(3, 3),  # 注意, 这里ksize使用的是tuple类型, 也就是需要传入长宽才可以
        normalize=True,  # a = 1/h*w, 退化成均值滤波
    )
    dst2 = cv.boxFilter(
        img,
        -1,
        (3, 3),  #
        normalize=False  # a=1, 这样就变成了真正的放box Filter了
    )

    # show image
    cv.imshow("img", img)
    cv.imshow("dst1", dst1)
    cv.imshow("dst2", dst2)

    cv.waitKey(0)  #

    cv.destroyAllWindows()


def blur_filter() -> None:
    img = cv.imread("test.jpg")

    # use blur filter
    dst = cv.blur(
        src=img,  # src img
        ksize=(3, 3),
        anchor=(-1, -1) # 表示自动设置锚点
    )

    # show image
    cv.imshow("img", img)

    cv.imshow("dst", dst)

    cv.waitKey(0)

    cv.destroyAllWindows()


def gaussian_filter() -> None:
    """use gaussian filter to deal figure"""

    # read image
    img = cv.imread("test.jpg")

    # use gauss filter
    dst = cv.GaussianBlur(
        src=img,
        ksize=(3, 3),
        sigmaX=1,
        sigmaY=1,

    )

    # show image
    cv.imshow("img", img)

    cv.imshow("dst", dst)

    cv.waitKey(0)

    cv.destroyAllWindows()






if __name__ == '__main__':
    # filter2D() # 卷积
    # boxFilter() # 方盒滤波
    # blur_filter() # 均值滤波
    gaussian_filter() # 高斯滤波