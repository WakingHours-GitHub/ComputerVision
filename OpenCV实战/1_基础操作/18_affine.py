import cv2 as cv
import numpy as np


def img_translation():
    img = cv.imread("./test.jpg")

    M = np.float32([[1, 0, 100], [0, 1, 50]])  # 为了精度, 需要转换成float32.
    # 100和50分别是x, y轴的偏移量.

    img_translation = cv.warpAffine(img, M, dsize=img.shape[-2::-1])
    # 注意这里img.shape -> 返回的是(h, w, c) 而dsize的参数是(x, y)因此需要逆序一下.

    cv.imshow("img_translation", img_translation)
    # 此时图像就是向下平移50, 同时向右平移100.

    cv.waitKey(0)

    cv.destroyAllWindows()

def img_rotation():
    img = cv.imread("./test.jpg")

    # 通过旋转角度, 来确定仿射矩阵
    M = cv.getRotationMatrix2D(
        tuple(map(lambda x: int(x / 2), list(img.shape[-2::-1]))), # center, 中心点为(x, y)
        angle=15, # angle 角度, 这里旋转的角度为逆时针.
        scale=0.7 # scale, 缩放因子.
    )
    print(M)
    # [[ 6.76148078e-01  1.81173332e-01  1.64486457e+02]
    #  [-1.81173332e-01  6.76148078e-01  3.21630436e+02]]

    src = np.float32([[400, 300], [800, 300], [400, 1000]])
    # 这里的点. 坐标是(x, y), 这些点一定要是在图像当中
    dst = np.float32([[200, 400], [600, 500], [150, 1100]])
    # src和dst一定是一一对应的. 根据自己的要求, 选择对应点的对应关系.
    # 使用src和dst进行对应, 返回放射矩阵.
    M2 = cv.getAffineTransform(src, dst) #
    # 如果想改变新图像的尺寸, 则需要传入dsize参数.
    new_img = cv.warpAffine(img, M2, dsize=img.shape[-2::-1]) # 进行仿射变换.

    cv.imshow("img", img)
    cv.imshow("new_img", new_img)

    cv.waitKey(0)


    cv.destroyAllWindows()



if __name__ == '__main__':
    # img_translation()
    img_rotation()


