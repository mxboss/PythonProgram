"""
   __author__="dazhi"
    2021/3/20-16:49
"""
# 导入库
import cv2 as cv


def face_detect_demo():
    # 将图片转换为灰度图片
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 加载特征数据
    face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    #进行检测人脸操作(参数也可以不写)
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=50)
    #得到的daces可能是多组x,y,h,w
    print("faces 的数值：",faces)
    for x, y, w, h in faces:
        #画矩形
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
        #画圆
        cv.circle(img, center=(x + w // 2, y + h // 2),radius=w//2,color=(0,0,255),thickness=1)
    # 显示图片(这时的照片会一闪而过)
    cv.imshow('result', img)


if __name__ == '__main__':
    # 读取图片（注意路径不要有中文,否则会报错）
    img = cv.imread("yibo.png")
    face_detect_demo()
    # 设置等待键盘输入（保证上边显示的照片可以停留）
    # 传入0表示无限等待，直到有东西输入(单位是毫秒)
    cv.waitKey(0)
    # 释放内存（由于底层是c++写的，所以将底层里面的空间进行释放）
    cv.destroyAllWindows()
