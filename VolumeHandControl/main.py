import cv2
import HandTracking
import gc

if __name__ == '__main__':
    track = HandTracking.HandTracking(
        mode=False,
        maxHands=2,  # 所检测的最大手的数量
        dedectionCon=0.5,  # 检测置信度, 有多大可能确定
        trackCon=0.5  # 追踪置信度
    )  # 初始化对象

    videoCapture = cv2.VideoCapture(0)  # 打开摄像头
    videoCapture.set(3, 420)  # 设置摄像头高度
    videoCapture.set(4, 320)  # 设置这项头高度

    while True:
        isOpen, img = videoCapture.read()
        if isOpen:
            img = track.findHands(img=img)  #

            track.VolumeControl(img=img)

            track.dispFPS(img=img) # 显示FPS


            cv2.imshow("image", img)
            cv2.waitKey(1)

        else:
            print("打开摄像头失败")
            isOpen, img = videoCapture.read()

        gc.collect()

