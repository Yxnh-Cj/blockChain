# -- *-coding=utf-8-* --
import os
import time
import subprocess
import copy

wifi_network = 'CMCC-CMCC'


def close():
    while True:
        process = subprocess.Popen(
            'netsh wlan connect {0}'.format(wifi_network),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()


if __name__ == '__main__':
    t = float(input('输入间隔时间(秒):'))
    time_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    time_start_time = time.mktime(time.strptime(time_start,'%Y-%m-%d %H:%M:%S'))
    close()
    # time_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # time_start_time = time.mktime(time.strptime(time_start,'%Y-%m-%d %H:%M:%S'))
    # time_old = copy.deepcopy(time_start_time)
    # print('现在时间是:{}'.format(time_start))

    # time_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # time_end_time = time.mktime(time.strptime(time_end,'%Y-%m-%d %H:%M:%S'))
    # while True:
    #     close()
    #     time_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    #     time_end_time = time.mktime(time.strptime(time_end,'%Y-%m-%d %H:%M:%S'))
    #     if time_end_time
    # print(time_end_time-time_start_time)
    # print(time.mktime(time.strptime(time_start,'%Y-%m-%d %H:%M:%S')))
    # time.sleep(t)
    # print(time.mktime(time.strptime(time_end,'%Y-%m-%d %H:%M:%S')))

# import os
# import time
#
# class App():
#
#     def __init__(self,count):
#         self.count = count
#
#     # 开启wifi的方法
#     def openWifi(self):
#         cmd = 'adb shell svc wifi enable'
#         os.popen(cmd)
#         time.sleep(2)
#
#     # 关闭wifi的方法
#     def closeWifi(self):
#         cmd = 'adb shell svc wifi disable'
#         time.sleep(2)
#
#     #控制wifi循环的方法
#     def controlWifi(self):
#         i = 1
#         while (self.count >0):
#             print("第 %d 次执行开关Wi-Fi操作" % i)
#             self.closeWifi()
#             self.openWifi()
#             i = i +1
#             self.count = self.count - 1
#
#
# if __name__ == '__main__':
#     #控制Wi-Fi开关执行100次
#     app = App(100)
#     app.controlWifi()