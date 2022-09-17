import cv2 as cv
import numpy as np
"""

图像拼接步骤:
1. 读取文件, 将图片设置成一样大小的: 640*480. 或者其他常用大小例如1280p, 960p等等
2. 对读取的图片找到特征点, 描述子, 计算单应性矩阵. 
3. 根据单应性矩阵对图像进行变换, 然后平移.
4. 拼接, 并输出结果. 



image stitch step:
1. read image file, and set image to same size: 640*480, all of is same size comml
2. 
"""

def main() -> None:
    # 读取
    img1 = cv.imread("img_stitch1.png")
    img2 = cv.imread("img_stitch2.png")

    # 尺寸的设置, 设置成为同样的大小:
    img1 = cv.resize(img1, (640, 480))
    img2 = cv.resize(img2, (640, 480))
    # 看一下:
    # cv.imshow("np.hstack([img1, img2])", np.hstack([img1, img2]))







    cv.waitKey(0)

    cv.destroyAllWindows()






















































if __name__ == '__main__':
    main()