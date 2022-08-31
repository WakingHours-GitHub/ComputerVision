import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

# 划线, 坐标点为(x, y), 这与之前我们索引图像时不同, 之前是(y, x)
cv.line(img,
        (10, 20), (300, 400),
        color=(0, 0, 255), # 颜色还是遵循BGR的顺序.
        thickness=5, # 线宽
        lineType=4, # 平滑度, 越大, 则约平滑
        )

cv.line(img,
        (100, 200), (400, 500),
        color=(0, 0, 255), # 颜色还是遵循BGR的顺序.
        thickness=5, # 线宽
        lineType=16, # 平滑度, 越大, 则约平滑, 取-1, 4, 8, 16这几个数值
        # 源码规定的. 默认为8,
        )

# 画矩形, 参数与上面画线的api参数相同.
cv.rectangle(
        img,
        (400, 100),
        (500, 400),
        (0, 0, 255),
        thickness=2,
        lineType=16
)

# 画圆:
cv.circle(
        img,
        center=(320, 280), # 坐标是反的. 这里表示圆心
        radius=50, # 圆形的半径
        color=(0, 255, 0),
        thickness=2,
        lineType=16
)

# 画椭圆
cv.ellipse(
        img, # 在哪个img上画图
        center=(320, 280), # 中心点
        axes=(100, 50), # 长轴和短轴的一半, (x, y)
        angle=0, # 长方形的角度
        startAngle=0, # 起始角度
        endAngle=360, # 结束的角度
        color=(0, 255, 0), # 颜色
        thickness=2, # 线宽
        lineType=16, # -1: 填充
)

# 再画一个矩形:
cv.ellipse(
        img, # 在哪个img上画图
        center=(320, 280), # 中心点
        axes=(50, 20), # 长轴和短轴的一半, (x, y)
        angle=90, # 长方形的角度, 从x轴, 顺时针旋转
        startAngle=0, # 起始角度
        endAngle=180, # 结束的角度 # 从x轴正方向开始, 顺时针.
        color=(0, 255, 0), # 颜色
        thickness=2, # 线宽
        lineType=-1, # -1: 填充
)


# 绘制多边形:
# 创建点集
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32) # 注意, 这个点集必须是int32类型的
cv.polylines(
        img,
        [pts], # 点的集合, 作为一个列表, 成为电机
        isClosed=True, # 表示是闭合True
        color=(255, 0, 0),
        thickness=2,
)
# 无法使用lineType, 直接填充多边形
# 需要使用fillpoly这个api进行填充
cv.fillPoly(
        img,
        [pts], # 注意, 这里要使用[]包裹
        color=(255, 0, 0)
)

# 绘画字符串:
cv.putText(
        img,
        text="离谱",
        org=(300, 400), # 字符串左上角点的坐标
        fontFace=cv.FONT_HERSHEY_SIMPLEX,
        fontScale=2, # 字的规模, 字号
        color=(255, 255, 0),
        thickness=2,
        lineType=16

)



# 明显可以看出, 后边的线条更加平滑.
# display figure
cv.imshow("img", img)
cv.waitKey(0)

cv.destroyAllWindows()