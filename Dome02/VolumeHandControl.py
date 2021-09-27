import cv2
import time
import math
import numpy as np
import pyautogui
import HandTrackingModule as htm  # 导入一个HandTrack..的类
# 导入音频相关的库: pip install pico
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#################################
# 相机参数
wCam, hCam = 640, 480
#################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # 设置摄像头高度
cap.set(4, hCam)  # 设置这项头高度

cTime = 0
pTime = 0

detector = htm.handDetector()  # 你也可以修改检测手的置信度

# 音量初始化
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute() # 静音
# volume.GetMasterVolumeLevel() # 主音量等级
# volume.GetVolumeRange() # 主音量范围
# volume.SetMasterVolumeLevel(-20.0, None) # 设置主音量

# print(volume.GetVolumeRange()) #  (-63.5, 0.0, 0.5)
volumeRange = volume.GetVolumeRange()  # 获取当前主音量范围
minVol = volumeRange[0]
maxVol = volumeRange[1]

vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()  # 读入一帧图像

    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)  # 获取当前id和坐标
    if len(lmList) != 0:  # 如果检测出点了
        # print(lmList[4], lmList[8d10, (122, 255, 0), cv2.FILLED)
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[20][1], lmList[20][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (122, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (122, 255, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (122, 255, 0), cv2.FILLED)

        cv2.circle(img, (x3, y3), 10, (0, 255, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x3, y3), (0, 255, 255), 2)

        # 然后我们来在我们想标记的中间画根线
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)  # 参数分别是: 要显示到的图像, 坐标1, 坐标2, BGR, 厚度

        # 那么我们如何获取长度呢, 很简答嘛, 空间中的欧几里得范数:sqrt(x*x+y*y), math.hypot()就可以直接计算出
        length = math.hypot(x2 - x1, y2 - y1)
        print(length)  # 打印长度, 看最大和最小值的情况

        # 接下来我们就要改变系统音量了: pycaw在github中可以找到
        # 手指的长度范围: Hand range: 20~200
        # 声音的范围: Volume Range: -65~0 ( 0为最大音量)
        # 我们需要一个映射, 这里就用到了numpy.interp()
        vol = np.interp(length, [20, 160], [minVol, maxVol])  # 在这里控制的有点不太平滑, 我们可以在考虑考虑算法
        volBar = np.interp(length, [20, 160], [400, 150]) # 在来一个音量调的转换
        volPer = np.interp(length,[20,160], [0,100]) # 转换百分比

        print(int(length), vol)
        # 此时我们就可以控制我们的音量了
        volume.SetMasterVolumeLevel(vol, None)  # 设置主音量

        # 我们最后一件事情能够做的就是显示音量:
        # cv2.putText(img,f"volume: {vol}",(0,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255))

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)  # 画一个矩形
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)  # 填充它
        cv2.putText(img, f"{str(int(volPer))}%", (40, 450), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                    (10, 255, 0), 2)  # BGR颜色, 线的宽度

        # 根据你的检测精度和距离, 合适的设定你的阈值
        if length <= 25:  # 当长度<=25, 我认为食指和拇指一块了
            cv2.circle(img, (cx, cy), 10, (0, 0, 200), cv2.FILLED)  # 当检测到合在一起了, 就改变颜色
            pyautogui.hotkey('ctrl', 'alt', 'right')
            time.sleep(1)
        length2 = math.hypot(x3 - x1, y3 - y1)

        if length2 <= 25:
            cv2.waitKey(0)

    #######################################################
    # 显示FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {str(int(fps))}", (0, 30), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                (10, 255, 0), 2)  # BGR颜色, 线的宽度
    #########################################################

    cv2.imshow("VolumeControl", img)
    cv2.waitKey(1)
