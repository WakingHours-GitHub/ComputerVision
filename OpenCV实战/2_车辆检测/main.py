import gc
import cv2 as cv
import numpy as np

MIN_W = 50
MIN_H = 50
# 窗口shape: (360, 640, 3)
START_POINT = 20
LINE_HIGH = 280 # 检测线的高度, 从左上角开始.
LINE_WIDTH = 600
LINE_RANGE = 3 # 线的范围, 只要在这个范围内. 就被判定为过线了.

# 存放有效车辆 容器
cars: list[tuple] = list()


car_num = 0 # 记数.


def calculate_center(x, y, w, h) -> tuple:
    return x + w//2, y + h // 2

def main() -> None:

    global car_num

    # 使用视频加载的构造方法, 创建Capture对象
    cap = cv.VideoCapture("./video3.mp4")  # 返回一个cap对象
    # cv.namedWindow("img", cv.WINDOW_NORMAL)
    cv.namedWindow("frame", cv.WINDOW_NORMAL)

    # 创建视频去除对象.
    bgsubmog = cv.createBackgroundSubtractorMOG2()  # 返回对象
    # 可以看到, 其实车的影子也是跟着在动的, 因此没有被去除.
    # 树叶也在动, 不过较小, 我们可以通过滤波去除.

    # 视频是由很多frame(帧)组成的.
    """
    使用opencv读取rtsp视频流预览的时候，发现运行越久越卡的情况。
    分析是内存没有释放的缘故，在循环里每帧结束后把该帧用del()删除即可。 修改代码如下：
    cap = cv2.VideoCapture(rtsp_address)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('preview', frame)
            del(ret)
            del(frame)
    """

    # 获取kernel
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

    while True:
        ret, frame = cap.read()  # 读取每一帧. 返回两个值
        # 返回是否成功, 以及frame
        if ret:  # 需要判断是否读取成功

            # print(frame.shape)
            # 灰度化:
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # 降噪 # 我们一般是在去背景之前进行降噪, 这样得到的效果比较好.
            frame_blur = cv.GaussianBlur(frame_gray, (5, 5), 5) # opencv中去背景的API。
            # 去背景 -> image binary
            mask = bgsubmog.apply(frame_blur)  # 处理后得到的一个掩码


            # 腐蚀:
            frame_erode = cv.erode(mask, kernel)
            # 经过腐蚀之后, 将一些小的噪点(斑块)去除掉.
            # 还原: 进行膨胀
            frame_dilate = cv.dilate(frame_erode, kernel, iterations=2) # 多次膨胀.
            # 然后使用形态学闭操作: 对一些小的噪点进行去除,
            # 然后我们还需要填充, 去除物体内部中的小块

            # 闭操作, 填充物体内部的方块
            frame_close = cv.morphologyEx(frame_dilate, cv.MORPH_CLOSE, kernel)
            frame_close = cv.morphologyEx(frame_close, cv.MORPH_CLOSE, kernel)

            # 查找轮廓:
            contours, h = cv.findContours(frame_close, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

            # 画线:
            cv.line(frame, (START_POINT, LINE_HIGH), (START_POINT+LINE_WIDTH, LINE_HIGH), (0, 0, 255), 2)

            for index, contour in enumerate(contours):
                # 外接矩阵:
                x, y, w, h = cv.boundingRect(contour) # 返回retc, 自动解包得到(x, y, w, h)

                # 这里识别是所有轮廓, 也就是所有在mask去背景后的物体都会被识别出来. 因此因此我们还需要进行进一步的处理.
                # 然后我们应该遍历所有轮廓的同时, 进行判断, 车辆识别轮廓的体积, 如果体积满足一个条件, 那么我们判断这是车辆, 而其他不是车辆.
                # 对车辆的宽高进行判断.
                if not (w >= MIN_W and h >= MIN_H): # 不是有效的车
                    continue

                # 只有判断成为有效的车, 才继续
                # 只有是有效的车, 才可以画出矩形
                # 然后在原图上画出矩形
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.rectangle(frame_gray, (x, y), (x + w, y + h), (255, 255, 255), 2)


                # 有效的车. 将中心点存储起来, 添加到一个列表当中去. 然后判断是否经过一个范围
                # 只有经过了这个范围, 然后计数.

                # 计算中心点, 并添加到列表中去.
                center_points = calculate_center(x, y, w, h)
                cars.append(center_points)
                # 画出每辆车的中心点:
                cv.circle(frame, center_points, 5, (0, 0, 255), thickness=-1) # -1表示填充

                # 然后对有效车进行判读, 如果过线了则数字+1
                for x, y in cars:
                    # 要有一条线, 但是这并不是单纯意义上的线, 因为要有范围. 这样才能判断的更加精确.
                    # 进行判读:
                    if ((y > LINE_HIGH - LINE_RANGE) and (y < LINE_HIGH + LINE_RANGE)): # 只有这样就落入到这个区域.
                        # 落入这个区域了.
                        car_num += 1
                        cars.remove((x, y)) # 去除掉
                        print(car_num)







            # 显示信息
            cv.putText(frame, "Cars count: "+str(car_num), (10, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
            cv.imshow("img", np.hstack([frame_close, frame_gray, mask]))
            cv.imshow("frame", frame)
            # cv.imshow("img", frame_close)  # 展示.

            # 降噪

            # if cv.waitKey(25) & 0xFF == ord('q'):
            if cv.waitKey(25) & 0xFF == 27:  # 27就是esc键
                break
        else:
            print("frame not read in Python")

        del ret
        del frame
        gc.collect()

    # release source.
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
