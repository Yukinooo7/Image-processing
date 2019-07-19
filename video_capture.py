import numpy as np
import cv2
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import threading

def capture_image(frame):
    img_name = "{}.jpg".format(time.strftime("%m%d%H%M",time.localtime()))
    cv2.imwrite(img_name,frame)
    cv2.imshow(img_name,frame)
    print("{}.jpg".format(time.strftime("%m%d%H%M",time.localtime()))+"has been saved")

def capture_video():
## VideCapture里面的序号
# 0 : 默认为笔记本上的摄像头(如果有的话) / USB摄像头 webcam
# 1 : USB摄像头2
# 2 ：USB摄像头3 以此类推
# -1：代表最新插入的USB设备 

    #创建一个实例
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

    print("if the camera is opened? {}".format(cap.isOpened()))

    ## 设置画面的尺寸

    # 画面宽度设为640
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    # 画面长度设为320
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)
    # 设置一个名为images的窗口，窗口大小为画面大小
    cv2.namedWindow('images',cv2.WINDOW_AUTOSIZE)
    # 操作提醒
    helpInfo = '''
    提示-按键前需要选中当前画面显示的窗口

    按键Q： 退出程序
    按键C： Capture 拍照
    '''
    print(helpInfo)
    # 逐帧获取摄像头画面
    while(True):
        #ret 为摄像头是否获取成功，如成功，则为True
        ret, frame = cap.read()
        # 若获取失败，则退出程序
        if not ret:
            print("Failed to get scream")
            break

        cv2.imshow('images',frame)

        key = cv2.waitKey(1)

        # 按q退出程序
        if key == ord('q'):
            print("Bye")
            break

        # 按c截图保存并显示最后一张截图
        elif key == ord('c'):
            capture_image(frame)
            # img_name = "{}.jpg".format(time.strftime("%m%d%H%M",time.localtime()))
            # cv2.imwrite(img_name,frame)
            # cv2.imshow(img_name,frame)
            # print("{}.jpg".format(time.strftime("%m%d%H%M",time.localtime()))+"has been saved")



    cap.release()
    cv2.destroyAllWindows()


capture_video()




