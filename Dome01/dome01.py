import cv2
import mediapipe as mp
import time

videoCapture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands  # 导入hands包
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils  # 画图

# 显示帧率
pTime = 0  # 过去的时间
cTime = 0  # 现在的时间


def displayFps(img):
    global pTime
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # 将fps put到img中: cv2.putText # 显示文本: 取整(因为除以得到小数),然后转成str
    cv2.putText(img, str(int(fps)),  # 显示给哪个对象, 显示什么
                (0, 30), cv2.FONT_HERSHEY_PLAIN, 2,  # 位置, 字体, 比例
                (10, 255, 0), 2)  # BGR颜色, 线的宽度


while True:  # 不断的去获取你当前捕获的图像
    success, img = videoCapture.read()  # 读取当前的img
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将img(GBR)转换成RGB

    results = hands.process(imgRGB)  # 跟踪我们的手部得到的点(结果)
    # print(results) # 打印的是检测
    # 如果我们想要知道什么时候结果发生了改变, 那么
    # print(results.multi_hand_landmarks)  # 这样当你手被识别时,就会返回坐标, 否则返回None

    if results.multi_hand_landmarks:  # 当检测到有手在img中时
        for handLms in results.multi_hand_landmarks:  # 遍历所有的results(就是可能有多个手)
            # mpDraw.draw_landmarks(img,handLms) # 在img上,显示handLms(一只手)
            for id, lm in enumerate(handLms.landmark):  # 获取id和位置信息
                # id就是每个标号(谷歌给的人手21个标号0~20), lm给出的是每个点(id)在图像中的比例
                # 给的lm是比例,那我们如何获取准确的xyz呢, 就用整体的img像素乘以比例就得到的是手的位置了
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)  # 中心的坐标等于比例乘以img的w和h

                # 那么我们如何获取特定的指尖吗, 已经获取到id了, 那么我们只需要if id等于我们想要的标号即可了
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)  # 填充
                # cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)  # 单独拿出来, 就会将所有的点(id)绘制出来
                # 所以我们可以用这些id的位置, 来做我们想要做的事

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # 将点连接起来

    displayFps(img)  # 显示帧率

    cv2.imshow("MyTestImage", img)  # 显示出来
    cv2.waitKey(5)
