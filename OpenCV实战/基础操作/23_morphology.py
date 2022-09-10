import cv2 as cv
import numpy as np


def morph_erode():
    """
    图形学操作: 腐蚀. 对白色区域, 进行腐蚀操作.
    卷积核可以是矩形, 椭圆, 以及十字交叉.
    卷积核越大, 腐蚀效果越强.

    :return:
    """

    # read image
    img = cv.imread("i.png")
    # before binary, need image transition to gray image
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # image binary
    ret, img_bin = cv.threshold(img_gray, 180, 255, cv.THRESH_BINARY)

    # create kernel by hand made
    # kernel = np.ones(shape=(5, 5), dtype=np.uint8)

    # use API offered by OpenCV
    kernel = cv.getStructuringElement(
        shape=cv.MORPH_RECT, # 使用矩形的卷积核
        # cv.MORPH_ELLIPSE # 椭圆卷积核
        # cv.MORPH_CROSS # 十字卷积核
        ksize=(5, 5),
    )
    print(kernel)


    # erode
    img_erode = cv.erode( # 返回结果
        src=img_bin,
        kernel=kernel,
        iterations=1, # 操作次数。
    )


    # show image
    cv.imshow("img", np.hstack([img_gray, img_erode]))

    cv.waitKey(0)

    cv.destroyAllWindows()

def morph_dilate():
    """
    图形学操作: 膨胀操作. 对白色区域进行膨胀操作.


    :return:
    """
    # read image
    img = cv.imread("i.png", flags=cv.IMREAD_GRAYSCALE) # 直接读成灰度图

    # image binary
    ret, img_bin = cv.threshold( # 注意, threshold return two value, one is status, one is img
        img,
        180,
        255,
        cv.THRESH_BINARY
    )
    print(img_bin)


    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(7, 7))

    # dilate operate
    img_dil = cv.dilate(
        src=img_bin,
        kernel=kernel,
        iterations=1,
    )

    # show image:
    cv.imshow("img", np.hstack([img_bin, img_dil]))



    cv.waitKey(0)


    cv.destroyAllWindows()












if __name__ == '__main__':
    # morph_erode()
    morph_dilate()