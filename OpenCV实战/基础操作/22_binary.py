import cv2 as cv
import numpy as np

def image_binary():
    # init window
    cv.namedWindow("img", cv.WINDOW_NORMAL)
    cv.resizeWindow("img", 480, 640)
    # read image
    img = cv.imread("test.jpg")

    # 一般图像学操作都是针对灰度图像, 因此我们这里将图像转换为灰度图像.
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 转换为灰度

    # binary to image
    res, dst = cv.threshold( # 返回两个值, 一个是状态, 一个是处理后的图像
        src=img_gray,  # source image
        thresh=50, # 阈值 -> thresh
        maxval=255, # 如果超过阈值, 则替换的是数值
        type=cv.THRESH_BINARY, # 阈值类型.
    )

    # 查看图像:
    # print(dst.shape) #  (1080, 1620, 3)

    # show image:
    cv.imshow("img", np.hstack((img_gray, dst)))
    cv.imshow("souce_img", img)

    cv.waitKey(0)

    cv.destroyAllWindows()




if __name__ == '__main__':
    image_binary()














