import math

import cv2 as cv
import numpy as np




class DrawShape(object):
    @staticmethod
    def init_info() -> None:
        pass


    def __init__(self):
        # init value.
        self.winname = "draw graph"
        self.trackbarname = "color"
        self.img = np.zeros(shape=(480, 640), dtype=np.uint8)
        self.graph_code = 0
        self.graph_start = (0, 0)
        self.graph_color: tuple = (0, 0, 0)

    @staticmethod
    def __trackbar_callback():
        pass

    def init_track_bar_color_control(self):
        cv.createTrackbar('b', self.winname, 255, 255, self.__trackbar_callback)
        cv.createTrackbar('g', self.winname, 255, 255, self.__trackbar_callback)
        cv.createTrackbar('r', self.winname, 255, 255, self.__trackbar_callback)

    def get_track_bar_color(self):
        b, g, r = cv.getTrackbarPos('b', self.winname), cv.getTrackbarPos('g', self.winname), cv.getTrackbarPos('r', self.winname)

        return (b, g, r)
    # @staticmethod
    def __on_mouse(self, event, x, y, flags, userdata):
        print(event, x, y, flags, userdata)
        self.graph_color = self.get_track_bar_color()
        print(self.graph_color)
        # 计算event
        # if event & cv.EVENT_LBUTTONDOWN == cv.EVENT_LBUTTONDOWN: # don't know why that is write
        #     self.graph_start = (x, y)
        # elif event & cv.EVENT_LBUTTONUP == cv.EVENT_LBUTTONUP: # left button up
        #
        #     if self.graph_code == 1:
        #         cv.line(self.img, self.graph_start, (x, y), color=self.graph_color, thickness=2)
        if event == cv.EVENT_LBUTTONDOWN:
            self.graph_start = (x, y)
        elif event == cv.EVENT_LBUTTONUP:
            if self.graph_code == 1:
                cv.line(self.img, self.graph_start, (x, y), color=self.graph_color, thickness=2)
            elif self.graph_code == 2:
                cv.rectangle(self.img, self.graph_start, (x, y), color=self.graph_color, thickness=2)
            elif self.graph_code == 3:
                # calculate radius
                radius = round(math.sqrt((self.graph_start[0] - x) ** 2 + (self.graph_start[1] - y) ** 2))
                cv.circle(self.img, self.graph_start,radius, self.graph_color, thickness=2)




    def main(self) -> None:
        # 创建窗口
        cv.namedWindow(self.winname)
        # set trackbar to control color
        self.init_track_bar_color_control()
        # 设置鼠标回调函数
        cv.setMouseCallback(self.winname, self.__on_mouse, 'date_test')
        while True:
            cv.imshow(self.winname, self.img)
            key = cv.waitKey(10) & 0xFF
            if key == ord('q'):
                break # exit
            elif key == ord('l'): # line
                print("line")
                self.graph_code = 1
            elif key == ord('r'): # r
                print("rectangle")
                self.graph_code = 2
            elif key == ord('c'):
                self.graph_code = 3
            elif key == ord('a'):
                self.img = np.zeros(shape=(480, 640), dtype=np.uint8)

        cv.destroyAllWindows()







def main() -> None:
    DrawShape().main()

if __name__ == '__main__':
    main()







