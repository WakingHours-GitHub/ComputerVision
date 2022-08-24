# 创建和显示窗口
import cv2 # 常见写法。
import numpy as np
# import cv2 as cv # 常见写法

# cv2.namedWindow(窗口名称, 窗口属性)
"""
WindowFlags:
    WINDOW_NORMAL : user can resize the window
    WINDOW_AUTOSIZE : user cannot resize the window, the size is constrainted by the image displayed 
    WINDOW_OPENGL : window with opengl support
    WINDOW_FULLSCREEN : change the window to fullscreen
    WINDOW_FREERATIO : the image expends as much as it can 自由比例 
    WINDOW_KEEPRATIO : 保持比例
    WINDOW_GUI_EXPANDED : status bar and tool bar
    WINDOW_GUI_NORMAL  : old fashious way
"""

# cv2.namedWindow('new', cv2.WINDOW_AUTOSIZE) # create window, not display

cv2.namedWindow('new', cv2.WINDOW_NORMAL) # can use mouse to resize window

# cv2.resizeWindow(winname: str, width: int, height: int) # 窗口名称, 一个宽度一个高度,
cv2.resizeWindow('new', 640, 640) # resize window.

# cv2.imshow(winname: str, mat: array)
cv2.imshow('new', 1) # show window



# key = cv2.waitKey(delay=None) 等待窗口的显示时长. 单位: ms
# key是接收键盘的动作.
# 并且接收鼠标和键盘的事件.
# 0为等待, 任意字符则关闭.
key = cv2.waitKey(0) # 停留
# 对接收到的键盘字符, 进行判断.
if(key == 'q'):
    exit()

cv2.destroyAllWindows() # 释放所有的窗口资源, 销毁所有资源



















