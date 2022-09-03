import cv2 as cv
import numpy as np


def bit_not_operation():
    # 创建一张图片
    img = np.zeros(shape=(480, 640), dtype=np.uint8)
    # 画一个矩形:
    img[50: 150, 50: 150] = 255
    print(img)

    cv.imshow("img", img)

    # 按照位取反:
    img_not = cv.bitwise_not(img)
    print(img_not)

    cv.imshow("img_not", img_not)

    cv.waitKey(0)

    cv.destroyAllWindows()


def bit_and_operation():
    '''按位与操作.'''
    img1 = np.zeros((480, 640), dtype=np.uint8)
    img2 = np.zeros(shape=(480, 640), dtype=np.uint8)
    img1[20: 130, 20: 130] = 128
    img2[50: 150, 50:150] = 255

    # 显示图片:
    cv.imshow("img1", img1)
    cv.imshow("img2", img2)

    # 图像与运算, 只有同为1的才为1, 因此, 只有重叠部分能够保留下来
    bit_and_img = cv.bitwise_and(img1, img2)
    cv.imshow("bit_and_img", bit_and_img)
    # 如果值不是255, 那么则.


    cv.waitKey(0)

    cv.destroyAllWindows()



def bit_or_operation():
    img1 = np.zeros((480, 640), dtype=np.uint8)
    img2 = np.zeros(shape=(480, 640), dtype=np.uint8)
    img1[20: 130, 20: 130] = 128
    img2[50: 150, 50:150] = 255

    # 显示图片:
    cv.imshow("img1", img1)
    cv.imshow("img2", img2)

    # 图像与运算, 只有同为1的才为1, 因此, 只有重叠部分能够保留下来
    bit_and_img = cv.bitwise_or(img1, img2)
    cv.imshow("bit_and_img", bit_and_img)
    # 如果值不是255, 那么则.

    cv.waitKey(0)

    cv.destroyAllWindows()


def bit_xor_operation():
    img1 = np.zeros((480, 640), dtype=np.uint8)
    img2 = np.zeros(shape=(480, 640), dtype=np.uint8)
    img1[20: 130, 20: 130] = 255
    img2[50: 150, 50:150] = 255

    # 显示图片:
    cv.imshow("img1", img1)
    cv.imshow("img2", img2)

    # 图像与运算, 只有同为1的才为1, 因此, 只有重叠部分能够保留下来
    bit_and_img = cv.bitwise_xor(img1, img2)
    cv.imshow("bit_and_img", bit_and_img)
    # 如果值不是255, 那么则.

    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    # bit_not_operation()
    # bit_and_operation()

    # bit_or_operation()
    bit_xor_operation()

