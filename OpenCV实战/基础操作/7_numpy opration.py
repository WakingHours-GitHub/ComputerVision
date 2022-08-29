import numpy as np
import cv2 as cv

a = np.array([1, 2, 3])

print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)

# 定义zeros矩阵
c = np.zeros(shape=(8, 8, 3), dtype=np.uint8)
print(c)

# 定义ones矩阵
d = np.ones(shape=(8, 8, 3), dtype=np.uint8)
print(d) #

# 创建full数组
e = np.full(shape=(8, 8), fill_value=10, dtype=np.uint8)
print(e) # 创建全10数组.


# 单位矩阵
f = np.identity(3)
print(f)
# 打印3的单位矩阵

# eye, 可以不是方阵
g = np.eye(6, 4, k=2)
print(g)



# 索引:
def index():
    img = np.zeros((480, 640, 3), np.uint8)

    print(img[100, 100])  # [0 0 0]
    # 可见, 是三个值.

    # 向矩阵中某个元素赋值.
    count = 0
    while count < 200:
        # channel is BRG order
        # img[count, 100, 0] = 255 # 等价于下面的代码.
        img[count, 100] = [0, 0, 255]  # 同时赋值
        count += 1
    # 可见, 画了一根竖线.

    # 如果没有窗口, 那么imshow会自动创建一个窗口
    cv.imshow("img", img)
    cv.waitKey(0)

    cv.destroyAllWindows()



def ROI():
    img = np.zeros((480, 640, 3), np.uint8)

    roi = img[100: 200, 100:200]
    roi[:] = 255 # 这就表示图像中所有元素的像素点.



    cv.imshow("img", img)
    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    # index()
    ROI()

