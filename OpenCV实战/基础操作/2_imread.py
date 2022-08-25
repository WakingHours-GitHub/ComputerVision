import cv2
import cv2 as cv

cv.namedWindow('img', cv.WINDOW_NORMAL)
img = cv.imread("./test.jpg")  # 返回Mat数据类型的数据
# 这里需要注意, linux和windows中

# 展示, 实际上就是指定哪个图片在哪个窗口中显示
cv.imshow('img', img)

# waitKey接收到任何键后都会往后执行, 因此我们应该加个循环
while True:
    key = cv.waitKey(0)
    # 通过查看源码,可知这个key是16位的

    print(key) # 113
    print('q') # q
    print(ord('q')) # 113
    # ord就是将字符转换成对应的ASCII码

    if key & 0xFF == ord('q'): # 这样的逻辑, 才是完整的.
        print("1")
        # exit()

        break
    elif key & 0xFF == ord('s'):
        # 保存图片
        cv2.imwrite("./test_copy.png", img)
# 退出循环, 则销毁所有窗口
cv.destroyAllWindows()  # destroy all windows


