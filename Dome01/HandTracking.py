# 实现手部追踪模块
import mediapipe as mp #  直接导入一个对象
import cv2
import time



class HandTracking:

    # self, mode = False, maxHand = 2, 检测置信度, 追踪置信度
    def __init__(self, mode=False, maxHands = 2, dedectionCon = 0.5, trackCon = 0.5):
        # 赋值初始化
        self.mode = mode
        self.maxHands = maxHands
        self.dedectionCon = dedectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands # 导入mp.solutions.hands(追踪手的方案)
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.dedectionCon,self.trackCon ) # 使用参数初始化mp.hand
        self.mpDraw = mp.solutions.drawing_utils # 画图单元

    def findHands(self, img, draw=True):  # 传入的图像,和是否draw
        self.result = self.hands.process(img) # 对当前图像进行加工





