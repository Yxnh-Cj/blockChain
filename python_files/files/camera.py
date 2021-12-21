# 环境:Anaconda3-5.2.0   内置python3.6
# 编辑器：pycharm专业版

# 工具
import os
import sys
import win32api
import win32con
import time  # 获取拍照的时间
import smtplib  # 用来发送邮件
import email  # 用来构造邮件内容的库
from email.mime.image import MIMEImage  # 用来构造邮件内容的库
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cv2  # pip install opencv-python

# 二.思路
# 1.用opencv调用摄像头拍照保存图像文件
# 2.检测香炉是否正常，未连接图像保存本地
# 3.用email库构造邮件内容，保存图片以附件形式插入邮件内容中
# 4.用smtplib库发送邮件给指定邮箱

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
    cap = cv2.VideoCapture(0)
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


if __name__ == '__main__':
    # 1.先拍照保存
    GetPicture()
    # 2.设置邮件格式
    msg = SetMsg()
    # 3.发送邮件
    SendEmail(msg)
