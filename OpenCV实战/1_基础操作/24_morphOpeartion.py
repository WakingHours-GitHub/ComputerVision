"""
形态学操作:
    开运算: 先腐蚀后膨胀, 用于消除图片外面的噪点. 
    闭运算: 先膨胀后腐蚀, 用于消除中间区域内部的噪点.
    形态学梯度: 原图-腐蚀, 得到的就是边缘部分, 不过卷积核的选择是非常重要的.
    顶帽:
    黑帽



"""

import cv2 as cv
import numpy as np


def open_operation():
    """
    开运算: 先腐蚀后膨胀
    :return:
    """
    # read image:
    img = cv.imread("dot_i.png")  # read carry dot image
    img_gray = cv.cvtColor(
        img,
        cv.COLOR_BGR2GRAY
    )
    # image binary
    ret, img_bin = cv.threshold(
        img_gray,
        180,
        255,
        cv.THRESH_BINARY
    )

    # get kernel
    kernel = cv.getStructuringElement(cv.MORPH_RECT, ksize=(7, 7))

    # morphology exchange: Open operation
    img_open = cv.morphologyEx(
        src=img_bin,  # 使用经过二值化之后的图片,
        op=cv.MORPH_OPEN,  # 要执行的操作, opencv定义了几个标识符. 用来表示不同的操作.
        kernel=kernel,  # kernel可以自己创建, 也可以直接使用opencv提供过的api

    )

    # show image
    cv.imshow("img", np.hstack([img_gray, img_bin, img_open]))
    # 可见, 最左边是带有噪点的原图, 可以见到比较模糊. 然后经过二值化后, 图像变得清晰起来, 这是因为我们使用
    # threshold进行二值化了.  然后经过开运算后, 去除图像外部的噪点.
    # 如果噪点比较大可以选择比较大的kernel, 不过这可能导致原图腐蚀过大, 导致原图无法膨胀恢复,
    # 不过我们设置iterations, 进行多次开运算.

    cv.waitKey(0)

    cv.destroyAllWindows()


def close_operation():
    """
    闭运算: 先膨胀后腐蚀, 用于去除图像内部的噪点.
    :return:
    """

    # read image
    img_gray = cv.imread("dot_in_i.png", cv.IMREAD_GRAYSCALE)  # 直接读取灰度图

    # image binary
    ret, img_bin = cv.threshold(img_gray, 130, 255, cv.THRESH_BINARY)

    # get kernel
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (11, 11))  # 这里ksize是可以调整的, 取决于闭运算效果
    # 开运算:
    img_close = cv.morphologyEx(img_bin, cv.MORPH_CLOSE, kernel)

    # show image
    cv.imshow("img", np.hstack([img_bin, img_close]))
    # 可见, 从左到右依次是二值化图, 以及经过闭运算后的图形.
    # 可见, 闭运算是去除黑底白色物体中, 白色物体的黑色噪点

    cv.waitKey(0)

    cv.destroyAllWindows()


def morphology_gradient():
    """
    形态学梯度: 原图 - 腐蚀过后的图片, 得到的就是形态学梯度,
    也是一种求边缘的方法.
    :return:
    """
    # read image
    img_gray = cv.imread("i.png", cv.IMREAD_GRAYSCALE)

    # image binary
    ret, img_bin = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

    # get kernel
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

    # morphology gradient:
    img_grad = cv.morphologyEx(img_bin, cv.MORPH_GRADIENT, kernel)

    # show image
    cv.imshow("img", np.hstack([img_bin, img_grad]))

    cv.waitKey(0)

    cv.destroyAllWindows()

    # 使用越小的核, 腐蚀的就越小, 当原图-腐蚀图时, 得到的边缘也就越细


def morphology_tophat():
    """
    顶帽运算: 原图 - 开运算.
    开运算: 去除图像外边的噪点（斑块）
    tophat: 原图 - 开运算。得到的就是图像外面的斑块（噪点）
    # 如果顶帽运算后没有得到理想的小斑块, 说明开运算先腐蚀的时候, 没有腐蚀掉小的斑块, 因此我们需要增大kernel的大小.
    这样才能腐蚀到更大的斑块, 这样经过原图减去后, 才可以得到斑块
    :return:
    """
    img = cv.imread("tophat.png")

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 二值化:
    ret, img_bin = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (19, 19))
    # 顶帽运算:
    img_tophat = cv.morphologyEx(img_bin, cv.MORPH_TOPHAT, kernel)

    cv.imshow("img", np.hstack([img_bin, img_tophat]))

    cv.waitKey(0)

    cv.destroyAllWindows()



def morphology_blackhat():
    """
    黑帽运算就是: 原图 - 闭运算
    闭运算: 就是先膨胀后腐蚀, 去除白色目标中黑色的噪点.
    然后经过原图减去后, 得到的就是, 仅剩下白色目标的黑色噪点(不过原图减去之后, 呈现白色). 这就是黑帽运算.
    :return:
    """
    img = cv.imread("dot_in_i.png")
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img_bin = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    # 黑帽运算:
    img_blackhat = cv.morphologyEx(img_bin, cv.MORPH_BLACKHAT, kernel)

    # show image
    cv.imshow("img", np.hstack([img_bin, img_blackhat]))

    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    # open_operation()
    close_operation()
    # morphology_gradient()
    # morphology_tophat()
    # morphology_blackhat()