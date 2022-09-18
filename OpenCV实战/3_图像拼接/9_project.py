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


def get_homography(img1, img2):
    """
    获取但应矩阵.
    步骤是:
        1. 创建特征转换对象: 例如SIFT, SURF, ORB
        2. 通过特征转换对象, 获得特征点和描述子.
        3. 创建特征匹配器. 一种是BF(暴力), 另一种是FALNN
        4. 进行特征匹配.
        5. 过滤一些不好的特征点. 这样计算单应性矩阵才是最好的. 后续拼接图像效果才好.

    :param img1:
    :param img2:
    :return:
    """

    # 创建SIFT对象.
    sift = cv.SIFT_create()

    # 特征点和描述点计算:
    kp1, des1 = sift.detectAndCompute(img1, None)  # img, mask
    kp2, des2 = sift.detectAndCompute(img2, None)

    # 创建特征匹配器: 使用BF匹配
    bf = cv.BFMatcher()
    # 使用knn匹配
    matches = bf.knnMatch(  # 返回匹配点.
        des1,
        des2,
        k=2,  # 最接近的几个匹配点, 也就是我们只是选择最接近的几个点.
    )

    # 检测过滤的点:
    verify_ratio = 0.8  # 就是筛选的阈值. 一般取0.7, 0.8左右
    verify_matches = list()
    # 就是判断, 距离的阈值, 越小则匹配精准度越高
    for m1, m2 in matches:
        if m1.distance < verify_ratio * m2.distance:
            verify_matches.append(m1)

    # 拿到验证之后的特征点, 然后我们就可以计算单应矩阵了, 不过我们还需要进行判断.
    # 因为单应矩阵是进行透视变换的矩阵, 如果使用透视变换, 则需要四个点以上.
    if len(verify_matches) >= 8:  # 设置最小的匹配点数目, 这样效果可能会更好.
        img1_pts = list()
        img2_pts = list()
        # 得到过滤后的, img的匹配点. 我们不是要全部的了.
        for m in verify_matches:  # 遍历验证后的坐标.
            # m.queryIdx对应的索引.
            img1_pts.append(kp1[m.queryIdx].pt)  # 这个是查询idx
            img2_pts.append(kp2[m.trainIdx].pt)  # 这个是训练idx
            # .pt的数据格式: [(x1, y2), ...]
            # 而img_pts需要的是: [[], [], ...] # 这种格式.

        img1_pts = np.array(img1_pts, np.float32).reshape(-1, 1, 2)  # 这样就符合findHomography()所需要的数据格式了.
        img2_pts = np.array(img2_pts, np.float32).reshape(-1, 1, 2)

        H, mask = cv.findHomography(img1_pts, img2_pts, cv.RANSAC, 5.0)  # 计算单应矩阵.
        # H是单应矩阵, mask是掩码.

        return H




    else:
        print("无法计算单应矩阵")


def stitch_image(img1, img2, H):
    # 获得每个图片四个角点. 然后对整张图片进行变换, 这样最后才能进行拼接.
    # 对图片进行变换: 首先通过单应矩阵, 进行透视变换, 然后将图片进行平移.
    # 创建一张大的幕布. 然后将两张图拼接在一起.
    # 将结果输出.
    # [[], [], ...]

    # 角点: 按照逆时针进行, 这个顺序也是在图像领域中约定俗称的领域
    # 获得原始图像的高, 宽
    h1, w1, _ = img1.shape
    h2, w2, _ = img2.shape

    # 然后我们就可以定义角点了.
    # 后续计算我们都是使用float32进行计算, 然后拓展为三维. 后续计算
    img1_dims = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)

    # 然后进行变换.
    # 对图像1进行变换:
    img1_transform = cv.perspectiveTransform(  # 经过变换之后的坐标
        src=img1_dims,  # 对图像1进行变换
        m=H,  # 矩阵.
    )
    # print(img1_dims)
    # print(img1_transform)  # 有负值, 因此是超越了画布了的.

    # 然后准备大的画幕
    # 我们如何计算变换后的宽高呢。 实际上就是x, y轴方向上的最大值-最小值, 得到的就是和高.
    # 因此我们需要知道最大值和最小值.
    result_dims = np.concatenate([img2_dims, img1_transform], axis=0)  # 获取集合 # 进行横向拼接
    print(result_dims)  # 就是将两张图的角点进行拼接.
    [x_min, y_min] = np.int32(result_dims.min(axis=0).ravel() - 0.5)  # 按照x轴, 进行找最小, 返回float, 并且是二维. 因此我们使用revel进行平坦.
    [x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
    # 并且害怕数组越界, 取最小值时,应该舍去. 因此是-0.5
    # 取最大值时, 应该是进位, 因此是+0.5
    # print( [x_min, y_min])  # [[-772.9236  -179.28111]]

    # 因为img1是一部分在外面, 因此我们需要平移.
    # 然后进行平移. 平移的距离其实就是x,y的最小值, 因为都是负数, 直接移过来就好了
    transform_dist = [-x_min, -y_min]

    transform_matrix = np.array([
        [1, 0, transform_dist[0]],
        [0, 1, transform_dist[1]],
        [0, 0, 1]
    ])
    # 投影变换:
    # cv.warpPerspective()
    result_img = cv.warpPerspective(
        img1,
        np.dot(transform_matrix, H),
        (x_max - x_min, y_max - y_min)  # 目标图像的大小, 就是宽高
    )
    # print(result_img) # 效果就是
    # 效果就是目前是一个大的画幕, 不过变换的角度已经是与第二张图片是一致的了
    # 下一步我们就是将图像平移过来, 平移距离就是x,y的min

    # 矩阵平移, 其实就是乘以一个齐次坐标. 就可以平移过来了.
    # [1, 0, dx]
    # [0, 1, dy]
    # [0, 0, 1] # 这就是平移矩阵.
    # transform_matrix = np.array([
    #     [1, 0, transform_dist[0]],
    #     [0, 1, transform_dist[1]],
    #     [ 0, 0, 1]
    # ])
    # 不过矩阵的平移我们合于上一步:

    # 然后就是进行拼接了. 将图片二拼接到图片1.
    result_img[
    transform_dist[1]:transform_dist[1] + h2,  # y轴
    transform_dist[0]:transform_dist[0] + w2  # x轴.
    ] = img2  # 复制进去

    # 剩下的就是对图片进行最后的优化了, 对接缝处进行优化, 然后进行裁剪.
    # 接缝处就是: transform_dist
    # 所以我们应该做的就是平均
    result_img[
        transform_dist[1]:transform_dist[1] + h2,
        transform_dist[0]+1
    ] = cv.addWeighted(
        result_img[
        transform_dist[1]:transform_dist[1] + h2,
        transform_dist[0] + 2
        ], 0.5,
        result_img[
        transform_dist[1]:transform_dist[1] + h2,
        transform_dist[0] - 2], 0.5,
        -5
    )

    return result_img  #


def main() -> None:
    # 读取
    img1 = cv.imread("img_stitch1.png")
    img2 = cv.imread("img_stitch2.png")

    # 尺寸的设置, 设置成为同样的大小: 具体的大小, 根据素材来选择.
    img1 = cv.resize(img1, (640, 480))
    img2 = cv.resize(img2, (640, 480))
    # 看一下:
    # cv.imshow("np.hstack([img1, img2])", np.hstack([img1, img2]))
    # 这个api的意思就是将图片横向拼接在一起, 要使用[]括起来.

    # 2. 对读取的图片找到特征点, 描述子, 计算单应性矩阵.
    H = get_homography(img1, img2)  # 计算单应性矩阵, 返回的就是单应矩阵
    print(H)

    # 3. 实现图像的拼接
    result = stitch_image(img1, img2, H)

    cv.imshow("test", result)
    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
