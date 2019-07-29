import numpy as np
import cv2
import time
from apscheduler.schedulers.blocking import BlockingScheduler


# 保存格式以及保存位置，默认设为存在此py文件的同目录下，名称为当地时间月日时分秒
def capture_image(frame):
    img_name = "{}.jpg".format(time.strftime("%m%d%H%M%S",time.localtime()))
    cv2.imwrite(img_name,frame)
    # cv2.imshow(img_name,frame)
    print("{}.jpg".format(time.strftime("%m%d%H%M%S",time.localtime()))+" has been saved")

def capture_video():
## VideCapture里面的序号
# 0 : 默认为笔记本上的摄像头(如果有的话) / USB摄像头 webcam
# 1 : USB摄像头2
# 2 ：USB摄像头3 以此类推
# -1：代表最新插入的USB设备 

    #创建一个实例
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    c = 1
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

    # 视频帧计算间隔频率
    time = 60
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
            print("Video capture halts")
            break
        
        # 按a进入自动截图模式，每秒拍摄速率为30帧，截图时间设为60帧，也就是两秒一截图
        elif key == ord('a'):
            print("Automatic capture starts")
            while ret:
                ret, frame = cap.read()
                cv2.imshow('images',frame)
                if(c%time == 0):
                    capture_image(frame)
                c = c+1
                key_in = cv2.waitKey(1)

                # 按q退出程序
                if key_in == ord('q'):
                    print("Automatic capture halts")
                    break

        # 按c截图保存并显示最后一张截图
        elif key == ord('c'):
            capture_image(frame)
            # img_name = "{}.jpg".format(time.strftime("%m%d%H%M",time.localtime()))
            # cv2.imwrite(img_name,frame)
            # cv2.imshow(img_name,frame)
            # print("{}.jpg".format(time.strftime("%m%d%H%M",time.localtime()))+"has been saved")

        c = c + 1

    print("Have a nice day")
    cap.release()
    cv2.destroyAllWindows()


capture_video()




