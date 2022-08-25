import cv2
import cv2 as cv


# 创建VideoWrite
fourcc = cv.VideoWriter_fourcc(*'MJPG')
# fourcc = cv.VideoWriter_fourcc(*'MP4V')
# fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')



vw = cv.VideoWriter('./out.mp4v', fourcc, 25, (1280, 720))  # 设置成分辨率
# 注意, 这里设置分辨率需要与你摄像头或者读取的文件的分辨率保持一致, 否则不会写入数据

# 创建窗口
cv.namedWindow('video', cv.WINDOW_NORMAL) # 跟内容是有关的,
cv.resizeWindow('video', 640, 480)



# 获取视频设备
cap = cv.VideoCapture(index=0)
# 读取视频文件
# cap = cv.VideoCapture("./video1.mp4") # 读取视频文件.

if cap.isOpened(): # 判断摄像头是否打开.


    while True:
        # 从摄像头读取视频帧.
        ret, frame = cap.read()
        # 第一个参数是状态值:bool, 第二个参数是frame:Mat

        # 对视频帧进行判断:
        if ret == True:

            # 将视频帧在窗口中显示
            cv2.imshow('video', frame)
            # 需要重新设置一下窗口的大小 不过现在的版本不需要使用了这个方法
            # cv.resizeWindow('video', 640, 480)

            # 写数据到多媒体文件
            vw.write(frame)  #

            # 等待. 这里不能为0, 一直等待输入
            # 这里给定一个数字, 单位为ms, 这样视频就可以动起来了.
            key = cv.waitKey(1)
            # 读取视频帧较快.
            # 在实时采集的过程中, 1ms是没问题的.
            # 但是在播放视频文件时, 大致是1000 / 24~30 = 40ms

            if key & 0xFF == ord('q'):
                break
        else:
            # frame也有帧的意思
            print("video frame is not readed")
            break # 退出
else:
    print("carma is not opened")
# 释放资源
vw.release()
cap.release()
cv.destroyAllWindows()
