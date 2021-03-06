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
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # 赋值初始化
        self.mode = mode
        self.maxHands = maxHands
        self.dedectionCon = dedectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands  # 导入mp.solutions.hands(追踪手的方案)
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.dedectionCon, self.trackCon)  # 使用参数初始化mp.hand
        self.mpDraw = mp.solutions.drawing_utils  # 画图单元

        self.results = None  # 对当前图像进行加工
        self.pTime = 0
        self.cTime = 0

    def findHands(self, img, draw=True):  # 传入的图像,和是否draw
        self.results = self.hands.process(img)
        if self.results.multi_hand_landmarks:  # 检测到手
            for oneHand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, oneHand, self.mpHands.HAND_CONNECTIONS)
        return img  # 返回加工好的图像

    def getLmList(self, img):
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

        lmList = HandTracking.getLmList(self, img)  # 返回各个标号及其x，y坐标: [[],[], ...]
        if len(lmList) != 0:  # 检测到手
            # pass
            thumbx, thumby = lmList[4][1], lmList[4][2]  # 大拇指
            indexx, indexy = lmList[8][1], lmList[8][2]  # 食指

            cv2.circle(img, (thumbx, thumby), 8, (122, 255, 0), cv2.FILLED)
            cv2.circle(img, (indexx, indexy), 8, (122, 255, 0), cv2.FILLED)

            # cv2.line(img, (thunm))



        else:
            print("检测不到手")

    def dispFPS(self, img):
        self.cTime = time.time()
        fps = 1 / (self.cTime - self.pTime)
        self.pTime = self.cTime
        cv2.putText(img, str(int(fps)), (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (10, 255, 0), 2)


if __name__ == '__main__':
    videoCap = cv2.VideoCapture(0)
    dete = HandTracking()

    while True:
        isOpen, img = videoCap.read()
        if isOpen:
            # 检测手部
            img = dete.findHands(img)
            # lmList = dete.getLmList(img)
            # if len(lmList) != 0:  # 检测到手
            #     pass
            # else:
            #     print("没有检测到手")

            # dete.VolumeControl(img)

            # 显示FPS
            dete.dispFPS(img)

            cv2.imshow("image", img)
            cv2.waitKey(1)
        else:
            print("打开摄像头失败")
            videoCap = cv2.VideoCapture(0)
