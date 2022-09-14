import cv2 as cv
import numpy as np


def sift() -> None:
    img = cv.imread("chess.png")

    # gray
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 创建sift对象
    sift = cv.SIFT_create() # 已经授权过了。因此直接使用SIFT_create创建对象




if __name__ == '__main__':
    sift()
