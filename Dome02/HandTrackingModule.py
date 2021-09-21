import cv2
import mediapipe as mp
import time


# 手部追踪模块
class handDetector():

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    # findHands返回img,
    def findHands(self, img, draw=True):  # drwa表示默认是画出图像
        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:  # 如果有手
            for handLms in self.results.multi_hand_landmarks:  # 遍历手
                # 你也可以在这里加上id,x,y等参数.这是你可选的
                if draw:  # 如果True, 就画出
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img  # 返回新的图像

    # 寻找姿势: img, handNO(id) 可以选择手的标号, 画默认都是True
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []  # 保存,id,cx,cy
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]  # 仅仅是找那个id
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])  # 添加
                if draw:  # 同样,还是判断画图
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:  # != 0 说明,检测到东西所以写入到lmList
            print(lmList[4])  # 这里面的标号

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)),  # 显示给哪个对象, 显示什么
                    (0, 30), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                    (10, 255, 0), 2)  # BGR颜色, 线的宽度

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
