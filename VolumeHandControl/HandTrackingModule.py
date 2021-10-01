# 实现手部追踪模块
import math

import mediapipe as mp  # 直接导入一个对象
import cv2 # 导入cv2： 用于对图像进行处理
import time # 计算Fps
import numpy as np # 导入科学计算模块
# 音量控制模块
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class HandTrackingModule:
    # 初始化声音模块
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # self, mode = False, maxHand = 2, 检测置信度, 追踪置信度
    def __init__(self, mode=False, maxHands=2, dedectionCon=0.5, trackCon=0.5):
        # 初始化
        self.mode = mode
        self.maxHands = maxHands
        self.dedectionCon = dedectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands  # 导入mp.solutions.hands(追踪手的解决方案)
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.dedectionCon, self.trackCon)  # 导入手部的模块
        self.mpDraw = mp.solutions.drawing_utils  # 画图单元

        self.results = None  # 对当前图像进行加工返回的结果
        self.pTime = 0
        self.cTime = 0

    # 检测手部
    def findHands(self, img, draw=True):  # 传入的图像,和是否draw
        self.results = self.hands.process(img) # 对每帧图像进行加工
        if self.results.multi_hand_landmarks:  # 检测到手, 返回标号
            for oneHand in self.results.multi_hand_landmarks: # 遍历所有手
                if draw: # 是否画图
                    self.mpDraw.draw_landmarks(img, oneHand, self.mpHands.HAND_CONNECTIONS)
        return img  # 返回图像

    def getLmList(self, img): # 获取手部标号
        lmList = []  # 保存所有的id, x, y
        self.results = self.hands.process(img)
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]  # 仅仅找一个手
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
        return lmList

    def VolumeControl(self, img):
        dete = HandTrackingModule()
        lmList = dete.getLmList(img)  # 返回各个列表
        if len(lmList) != 0:  # 检测到手
            # pass
            thumbx, thumby = lmList[4][1], lmList[4][2]  # 大拇指
            indexx, indexy = lmList[8][1], lmList[8][2]  # 食指
            # cx, cy =

            # 标记大拇指和食指
            cv2.circle(img,(thumbx,thumby),8,(122,255,0),cv2.FILLED)
            cv2.circle(img,(indexx,indexy),8,(122,255,0),cv2.FILLED)

            # 然后在中间画根线
            cv2.line(img, (thumbx,thumby), (indexx, indexy), (255, 0, 255), 3)

            # 计算长度
            thumb_index_length = math.hypot(thumbx - indexx, thumby - indexy) # 计算欧氏距离

            # 映射到音量
            # vol = np.interp(thumb_index_length, )


        else:
            print("检测不到手")

    def dispFPS(self, img):
        self.cTime = time.time()
        fps = 1 / (self.cTime - self.pTime)
        self.pTime = self.cTime
        cv2.putText(img, str(int(fps)), (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (10, 255, 0), 2)


