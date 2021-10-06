# 实现手部追踪模块
import mediapipe as mp  # 直接导入一个对象
import cv2
import time
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class HandTracking:

    # self, mode = False, maxHand = 2, 检测置信度, 追踪置信度
    def __init__(self, mode=False, maxHands=2, dedectionCon=0.5, trackCon=0.5):
        # 声音模块
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # 赋值初始化
        self.mode = mode # 方式
        self.maxHands = maxHands
        self.dedectionCon = dedectionCon
        self.trackCon = trackCon
        # 导入手部解决方案
        self.mpHands = mp.solutions.hands  # 导入mp.solutions.hands(追踪手的方案)
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.dedectionCon, self.trackCon)  # 使用参数初始化mp.hand
        self.mpDraw = mp.solutions.drawing_utils  # 画图单元
        self.results = None  # 对当前图像进行加工
        # 显示FPS
        self.pTime = 0
        self.cTime = 0

    # 用来追踪发现并且追踪手部
    def findHands(self, img, draw=True):  # 对传入的图像, 是否draw
        self.results = self.hands.process(img) # 对每帧图像进行加工
        if self.results.multi_hand_landmarks:  # 检测到手, 并且返回标号
            for oneHand in self.results.multi_hand_landmarks: # 遍历所有手(maxHand)
                if draw: # 是否标记出
                    self.mpDraw.draw_landmarks(img, oneHand, self.mpHands.HAND_CONNECTIONS)
        return img  # 返回加工好的图像

    # 返回所有的landmark(标号), 以便
    def getLmList(self, img):
        markList = []  # 保存所有的id, x, y
        self.results = self.hands.process(img) # 加工
        if self.results.multi_hand_landmarks: # 列表不为空, 说明找到手
            myHand = self.results.multi_hand_landmarks[0]  # 仅仅找一个手
            for num, lm in enumerate(myHand.landmark): # 返回索引序列
                h, w, c = img.shape # 获取当前img画幅
                cx, cy = int(lm.x * w), int(lm.y * h) # 比例
                markList.append([num, cx, cy]) # 添加到列表
        return markList

    # 实现音量控制的模块
    def VolumeControl(self, img):

        markList = HandTracking.getLmList(self, img)  # 返回各个标号及其x，y坐标: [[],[], ...]
        if len(markList) != 0:  # 检测到手
            # pass
            thumbx, thumby = markList[4][1], markList[4][2]  # 大拇指
            indexx, indexy = markList[8][1], markList[8][2]  # 食指



            cv2.circle(img, (thumbx, thumby), 8, (122, 255, 0), cv2.FILLED)
            cv2.circle(img, (indexx, indexy), 8, (122, 255, 0), cv2.FILLED)

            cv2.line(img, (thumbx, thumby),(indexx, indexy), (0,255,255),2)
        else:
            print("检测不到手")

    def dispFPS(self, img):
        self.cTime = time.time()
        fps = 1 / (self.cTime - self.pTime)
        self.pTime = self.cTime
        cv2.putText(img, str(int(fps)), (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (10, 255, 0), 2)
