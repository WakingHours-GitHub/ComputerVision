import cv2 as cv


def img_resize():
    """图像变换, 重设大小"""
    img = cv.imread("test.jpg")

    print(img.shape)  # (y, x, channel) # (1080, 1620, 3)
    # dsize -> (x, y) 绝对缩放.
    # img_transform = cv.resize(img, (600, 400)) # 然后其他都是用默认值
    img_transform = cv.resize(img, None, fx=0.3, fy=0.3, interpolation=cv.INTER_AREA)  # 使用相对缩放. 更换插值算法.
    print(img_transform.shape)  # (324, 486, 3)
    # 使用fx, fy缩放因子是相对缩放
    # 也就是1080*0.3, 和1620*0.3, 这种是乘比例缩放的.

    cv.imshow("img", img)
    cv.imshow("img_transform", img_transform)

    cv.waitKey(0)

    cv.destroyAllWindows()


def image_rollovers():
    """图像翻转, 上下翻转, 左右翻转"""

    img = cv.imread("test.jpg")
    img_up_down_reverse = cv.flip(img, 0)  # 上下翻转
    img_left_right_reverse = cv.flip(img, 1)  # flipcode > 0为左右翻转
    img_left_down_reverse = cv.flip(img, -1)  # flipCode < 0 上下左右翻转

    cv.imshow("img", img)  # 原图
    cv.imshow("img_up_down_reverse", img_up_down_reverse)  # 上下颠倒
    cv.imshow("img_left_right_reverse", img_left_right_reverse)  # 左右颠倒
    cv.imshow("img_left_down_reverse", img_left_down_reverse)  # 上下左右颠倒.

    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    # img_resize()
    image_rollovers()
