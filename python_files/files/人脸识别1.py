# -*- coding: utf-8 -*-
import face_recognition
import cv2
import os
# import sys
# import win32api
# import win32con
import time  # 获取拍照的时间
import smtplib  # 用来发送邮件
# import email  # 用来构造邮件内容的库
from email.mime.image import MIMEImage  # 用来构造邮件内容的库
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# image = face_recognition.load_image_file("./人脸识别源文件/陈杰.jpg")
# face_locations = face_recognition.face_locations(image)
#
# known_image = face_recognition.load_image_file("./人脸识别源文件/陈杰.jpg")
# unknown_image = face_recognition.load_image_file("./待人脸识别/test.jpg")
#
# chenjie_encoding = face_recognition.face_encodings(known_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#
# results = face_recognition.compare_faces([chenjie_encoding],unknown_encoding)

host = "smtp.163.com"
port = 25
sender = 'cj1415926535898@163.com'  # 消息发送方
pwd = 'LPHKUIXWDTPDAOZJ'  # 授权码
receiver = '1430292970@qq.com'  # 消息接收方
path = 'D:/test_pictures'


def GetPicture():
    """
    拍照
    :return:
    """

    cv2.namedWindow('camera', 1)
    # 开启ip摄像头
    # video = "http://admin:admin@192.168.1.107/video"  # 同一网络中,@后的ipv4 地址需要修改为自己的地址
    # cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0,
                           cv2.CAP_DSHOW)  # global D:\a\opencv-python\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (438),添加cv2.CAP_DSHOW不出现警告
    ret, frame = cap.read()
    cv2.imwrite(path + '/stranger.jpg', frame)
    cap.release()


def SetMsg():
    """
    邮件格式设置
    :return:
    """
    msg = MIMEMultipart('mixed')
    # 标题
    msg['Subject'] = '陌生人图片'
    msg['From'] = sender
    msg['To'] = receiver

    # 邮件正文内容
    text = '陌生人图片到了，请接收'
    MIMEText(text, 'plain', 'utf-8')  # 正文转码
    text_plain = MIMEText(text, 'plain', 'utf-8')  # 正文转码
    msg.attach(text_plain)

    # 图片
    SendImageFile = open(path + '/stranger.jpg', 'rb').read()
    image = MIMEImage(SendImageFile)

    # 将收件人看见的附件照片名称改为people.png
    image['Content-Disposition'] = 'attachment; filename = "stranger.png"'
    msg.attach(image)
    return msg.as_string()


def SendEmail(msg):
    """
    发送邮件
    :param msg:
    :return:
    """
    smtp = smtplib.SMTP()
    smtp.connect(host, port)
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg)
    time.sleep(2)
    smtp.quit()
    # smtp邮件发送协议


def face_recognitions():
    my_image = face_recognition.load_image_file("./人脸识别源文件/陈杰.jpg")
    my_image_encodings = face_recognition.face_encodings(my_image, model="cnn")[0]
    # my_face_locations = face_recognition.face_locations(my_image, model="cnn")

    unknown_image = face_recognition.load_image_file(path + '/stranger.jpg')
    unknown_image_encodings = face_recognition.face_encodings(unknown_image, model="cnn")[0]
    results = face_recognition.compare_faces([my_image_encodings], unknown_image_encodings)
    #
    return results[0]


if __name__ == "__main__":
    GetPicture()
    judgment = face_recognitions()
    try:
        if judgment:
            print("It's a picture of me!")
            os.remove(path + '/stranger.jpg')
        else:
            msg = SetMsg()
            # 3.发送邮件
            SendEmail(msg)
    finally:
        try:
            msg = SetMsg()
            # 3.发送邮件
            SendEmail(msg)
        except:
            pass
