import cv2 as cv
import numpy as np

def image_binary():
    """
    image binary
    when operate image to binary, input image as gray image,
    because only one channel image, binary effect batter

    :return:
    """
    # init window
    cv.namedWindow("img", cv.WINDOW_NORMAL)
    cv.resizeWindow("img", 480, 640)
    # read image
    img = cv.imread("test.jpg")

    # 一般图像学操作都是针对灰度图像, 因此我们这里将图像转换为灰度图像.
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 转换为灰度
    # transition to gray image # 转换为灰色图像。

    # binary to image
    res, dst = cv .threshold( # 返回两个值, 一个是状态, 一个是处理后的图像
        src=img_gray,  # source image
        thresh=50, # 阈值 -> thresh
        maxval=255, # 如 果超过阈值, 则替换的是数值
        type=cv.THRESH_BINARY, # 阈值类型.
    )

    # 查看图像:
    # print(dst.shape) #  (1080, 1620, 3)

    # show image:
    cv.imshow("img", np.hstack((img_gray, dst)))
    cv.imshow("souce_img", img)

    cv.waitKey(0)

    cv.destroyAllWindows()


def adaptive_image_binary():
    """
    adaptive image binary, that is adaptive threshold.
    使用自适应二值化, 全局二值化在一些带有阴影的图片效果不是很好, 因此我们使用局部二值化.
    对每一个block进行二值化, 然后根据阈值查找算法自动计算该block阈值.


    :return:
    """

    # read image
    img = cv.imread("test.jpg")
    # transition image:
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # image binary
    img_binary = cv.adaptiveThreshold( # 返回处理后的二值化图像
        src=img_gray, # 注意, 这里图像要使用灰色图像.
        maxValue=255, # 与threshold一样, 高于阈值就会被替换为该值, 255就是灰度最大值, 就是白色.
        adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, # 我们一般都会使用高斯窗口加权, 更科学
        thresholdType=cv.THRESH_BINARY_INV, # 二值化相反, 原来白色的地方会换成黑色, 黑色的地方会换成白色
        blockSize=11, # 就是局部区域大小
        C=0, # 计算得到的阈值加上C就是本次阈值, 用来全局调参数.
    )

    # show iamge:
    cv.imshow("img", img)
    cv.imshow("img_binary", img_binary)

    cv.waitKey(0)

    cv.destroyAllWindows()

    #

if __name__ == '__main__':
    # image_binary()
    adaptive_image_binary()













