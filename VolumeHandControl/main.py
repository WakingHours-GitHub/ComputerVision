import cv2
import HandTrackingModule

if __name__ == '__main__':

    videoCap = cv2.VideoCapture(0)
    dete = HandTrackingModule.HandTrackingModule()

    while True:
        isOpen, img = videoCap.read()
        if isOpen:
            img = dete.findHands(img)
            # lmList = dete.getLmList(img)
            # if len(lmList) != 0:  # 检测到手
            #     pass
            # else:
            #     print("没有检测到手")
            dete.VolumeControl(img)


            dete.dispFPS(img)

            cv2.imshow("image", img)
            cv2.waitKey(1)
        else:
            print("打开摄像头失败")
            videoCap = cv2.VideoCapture(0)
