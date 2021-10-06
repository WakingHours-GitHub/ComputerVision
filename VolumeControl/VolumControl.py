import cv2
import time
import math
import numpy as np
import pyautogui
import mediapipe as mp

# import HandTrackingModule as htm  # 导入一个HandTrack..的类

# 导入音频相关的库: pip install pico
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#################################

isDraw = True

#################################


# 相机参数
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)  # 设置摄像头高度
cap.set(4, hCam)  # 设置这项头高度
#################################
# 显示FPS
cTime = 0
pTime = 0

##################################
# mediapipe模块初始化
mode = False
maxHands = 2
detectionCon=0.5
trackCon=0.5
mpHands = mp.solutions.hands
hands = mpHands.Hands(mode, maxHands, detectionCon, trackCon)
mpDraw = mp.solutions.drawing_utils
################################

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
#################################

# 获取当前音量范围(range)和最大最小音量
volumeRange = volume.GetVolumeRange()  # 获取当前主音量范围
minVol = volumeRange[0]
maxVol = volumeRange[1]

vol = 0
volBar = 400
volPer = 0




























if __name__ == '__main__':

    while True:
        success, img = cap.read()  # 读入一帧图像
        #########################################################################
        # findHands模块
        result = hands.process(img) #
        if result.multi_hand_landmarks:
            for oneHand in result.multi_hand_landmarks:
                if isDraw:
                    mpDraw.draw_landmarks(img, oneHand, mpHands.HAND_CONNECTIONS)
        ##########################################################################
        # getMarkList模块
        markList = []
        if result.multi_hand_landmarks:
            oneHand = result.multi_hand_landmarks[0] # 只检测一个手
            for num, local in enumerate(oneHand.landmark):
                h,w,c = img.shape
                local_x, local_y = int(local.x * w), int(local.y * h)
                markList.append([num, local_x, local_y])
        #########################################################################
        # 音量控制模块
        if len(markList) != 0:  # 如果检测出点了
            # print(lmList[4], lmList[8d10, (122, 255, 0), cv2.FILLED)
            thumb_x, thumb_y = markList[4][1], markList[4][2]
            index_x, index_y = markList[8][1], markList[8][2]
            little_x, little_y = markList[20][1], markList[20][2]
            cx, cy = (thumb_x + index_x) // 2, (thumb_y + index_y) // 2 # 找到拇指和食指的中心

            # 高亮点
            cv2.circle(img, (thumb_x, thumb_y), 10, (122, 255, 0), cv2.FILLED)
            cv2.circle(img, (index_x, index_y), 10, (122, 255, 0), cv2.FILLED)
            cv2.circle(img, (little_x, little_y), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (cx, cy), 6, (122, 255, 0), cv2.FILLED)

            # 然后我们来在我们想标记的中间画根线
            cv2.line(img, (thumb_x, thumb_y), (little_x, little_y), (0, 255, 255), 2)
            cv2.line(img, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 255), 3)  # 参数分别是: 要显示到的图像, 坐标1, 坐标2, BGR, 厚度

            # 那么我们如何获取长度呢, 很简答嘛, 空间中的欧几里得范数:sqrt(x*x+y*y), math.hypot()就可以直接计算出
            thumb_index_distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
            little_thumb_distance = math.hypot(little_x - thumb_x, little_y - thumb_y)
            # print(thumb_index_distance)  # 打印长度, 看两根手指最大和最小的范围

            # 接下来我们就要改变系统音量了: pycaw在github中可以找到
            # 手指的长度范围: Hand range: 20~200
            # 声音的范围: Volume Range: -65~0 ( 0为最大音量)
            # 我们需要一个映射, 这里就用到了numpy.interp()
            vol = np.interp(thumb_index_distance, [20, 160], [minVol, maxVol]) # 音量的转换
            volBar = np.interp(thumb_index_distance, [20, 160], [400, 150])  # 音量条的转换
            volPer = np.interp(thumb_index_distance, [20, 160], [0, 100])  # 转换百分比

            # print(int(thumb_index_distance), vol)

            # 此时我们就可以控制我们的音量了
            volume.SetMasterVolumeLevel(vol, None)  # 设置主音量

            # 我们最后一件事情能够做的就是显示音量:
            # cv2.putText(img,f"volume: {vol}",(0,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255))

            cv2.rectangle(img, (30, 150), (60, 400), (255, 255, 20), 3)  # 画一个矩形
            cv2.rectangle(img, (30, int(volBar)), (60, 400), (255, 255, 20), cv2.FILLED)  # 填充矩形

            cv2.putText(img, f"{str(int(volPer))}%", (20, 430), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                        (255, 255, 20), 2)  # BGR颜色, 线的宽度

            # 根据你的检测精度和距离, 合适的设定你的阈值
            if thumb_index_distance <= 25:  # 当长度<=25, 我认为食指和拇指一块了
                cv2.circle(img, (cx, cy), 10, (0, 50, 255), cv2.FILLED)  # 当检测到合在一起了, 就改变颜色
                pyautogui.hotkey('ctrl', 'alt', 'right') # 网易云热键热键：切歌
                # time.sleep(1) # 等待, 不要重复切换热键
                cv2.waitKey(200)


            if little_thumb_distance <= 25: # 过小时， 就在暂停图像，等待回复
                cv2.waitKey(0)

        #######################################################
        # 显示FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f"FPS: {str(int(fps))}", (0, 30), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                    (10, 255, 0), 2)  # BGR颜色, 线的宽度
        #########################################################
        # 打印图像
        cv2.imshow("VolumeControl", img)
        cv2.waitKey(1)
        #########################################################
