"""
本章节主要介绍一些常用的算子.
Blue let me clame!


"""
import cv2 as cv
import numpy as np



def sobel_operator() -> None:
    """use sobel operator"""
    # read image:
    img = cv.imread("edge_test.png")  # read check edge image

    # use sobel operator to deal image
    d_x = cv.Sobel(
        src=img,
        ddepth=-1, # 位深和原图一样
        dx=1,
        dy=0, # one only deal a turn
        ksize=3, # 指定核大小为3
    )
    d_y = cv.Sobel(img, -1, 0, 1, ksize=3)

    # d_x add with d_y
    result_img = cv.add(d_x, d_y)
    # can use addWeight also
    result_img = cv.addWeighted(d_x, 0.5, d_y, 0.5, gamma=0)


    # show image
    cv.imshow("img", img)
    cv.imshow("result", np.hstack([d_x, d_y, result_img])) #  can use np.hstack to 横向拼接矩阵
    # 这样就可以同时显示了.

    cv.waitKey(0)

    cv.destroyAllWindows()


def scharr_operator():
    """use scharr operator to deal edge of image"""
    # read image
    img = cv.imread("edge_test.png")

    # use scharr operator
    d_x = cv.Scharr(
        src=img,
        ddepth=-1,
        dx=1,
        dy=0, # 同样, 也是只能分开计算x, y的导数.
        scale=None, # 缩放因子,
        # ksize 不需要指定ksize, 因为scharr核的大小只能为3
    )
    d_y = cv.Scharr(img, -1, 0, 1)

    # addWeight
    result = cv.add(d_x, d_y)

    # show image
    # cv.imshow("img", )

def camera_test():
    """
    使用canny边缘检测算法对每帧图像进行操作。
    :return:
    """
    cap = cv.VideoCapture(0)
    while True:
        isopened, frame = cap.read()

        if isopened:
            # deal img
            dst = cv.Canny( # canny边缘检测算法。
                image=frame,
                threshold1=100,
                threshold2=150
            )
            result = np.zeros(shape=frame.shape)
            result[:, :, 0] = dst
            result[:, :, 1] = dst
            result[:, :, 2] = dst

            result = np.uint8(result)


            # cv.imshow("test", frame)
            cv.imshow("img", np.hstack((frame, result)))
            """
            我们在使用imshow或者imwrite时，往往会错误的全白的纯色图像。
            这是因为，imshow函数在处理时是分情况的，当Mat.type为浮点数时，默认区间为【0，1】,当浮点数大于1时就是白色；当Mat.type为整数时，默认区间为【0，255】。
            """
        else:
            print('not opened')


        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()



if __name__ == '__main__':
    # sobel_operator()

    camera_test()