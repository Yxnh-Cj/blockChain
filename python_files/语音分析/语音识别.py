from aip import AipSpeech
#
APP_ID = "25246219"
API_KEY = "6pVKqPrB9vPwF5Du6yqC3lBU"
SECRET_KEY = "9S42EomFjKMTHFh5aByLp6zAwRF1mbXv"
#
# # 初始化语音识别客户端
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# # 文件读取成文本
# text_audio = open('D:/学习/new project/python_files/语音分析/testAudio.txt', encoding='utf-8')
# # 客户端合成文本生成结果，vol-指定语速
# result = client.synthesis(text=text_audio, options={'vol': 5})
# # 生成为语音格式文件
# if not isinstance(result, dict):
#     with open('D:/学习/new project/python_files/语音分析/testAudio.mp3', 'wb') as f:
#         f.write(result)
# else:
#     print(result)

# -*- coding: utf-8 -*-

import requests
import re
import os
import time
# from aip import AipSpeech
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import speech_recognition as sr


# 参数    类型    描述    是否必须
# tex    String    合成的文本，使用UTF-8编码，
# 请注意文本长度必须小于1024字节    是
# cuid    String    用户唯一标识，用来区分用户，
# 填写机器 MAC 地址或 IMEI 码，长度为60以内    否
# spd    String    语速，取值0-9，默认为5中语速    否
# pit    String    音调，取值0-9，默认为5中语调    否
# vol    String    音量，取值0-15，默认为5中音量    否
# per    String    发音人选择, 0为女声，1为男声，
# 3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女    否


def wordToFileB():
    print('开始转文件')
    data = word_e.get('1.0', 'end')
    per = var_per.get()
    filepath = var_path.get()
    num = len(word_e.get('1.0', 'end'))
    var_ws.set('已输入' + str(num) + '字')
    # print(data)
    # print(per)
    # print(filepath)
    if num > 500:
        tkinter.messagebox.showwarning('警告', '请输入不超过500字')
    else:
        wordToFile(data, per, filepath)
        flag = tkinter.messagebox.askokcancel('提示', '转语音成功,文件地址' + filepath + '是否播放')
        if flag:
            playFile(filepath)


def playFileB():
    print('开始播放')
    playFile(var_path.get())


def playFile(filepath):
    os.system(filepath)


def wordToFile(data, per, filepath, spd=5, pit=5, vol=5):
    result = client.synthesis(data, 'zh', 1, {
        'vol': vol,
        'spd': spd,
        'pit': pit,
        'per': per
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(filepath, 'wb') as f:
            f.write(result)


tk = Tk()
tk.title('文字转语音')
tk.geometry('600x400')

frame = Frame(tk)
Label(tk, text='请输入文字：(最多输入500字)', width=200, anchor=W, justify=LEFT).place(x=200, y=10)
var_ws = Variable()
wordsize = Label(tk, width=300, textvariable=var_ws, anchor=W, justify=LEFT)
var_ws.set('已输入0字')
wordsize.place(x=365, y=10)
# 输入文字
# var_word = Variable()
word_e = Text(tk, height=14)
word_e.place(x=20, y=40)

Label(tk, text='选择发音(0女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫)').place(x=10, y=240)
var_per = Variable()
e = Entry(tk, textvariable=var_per, width=20)
var_per.set(3)
e.place(x=400, y=240)
Label(tk, text='输入文件路径：').place(x=10, y=270)
var_path = Variable()
e = Entry(tk, textvariable=var_path, width=50)
var_path.set('test.mp3')
e.place(x=100, y=270)
Label(tk, text='输入语速0-9：').place(x=10, y=300)
var_spd = Variable()
e = Entry(tk, textvariable=var_spd)
var_spd.set(5)
e.place(x=100, y=300)
Label(tk, text='输入音调0-9：').place(x=180, y=300)
var_pit = Variable()
e = Entry(tk, textvariable=var_pit)
var_pit.set(5)
e.place(x=260, y=300)
Label(tk, text='输入音量0-15：').place(x=310, y=300)
var_vol = Variable()
e = Entry(tk, textvariable=var_vol)
var_vol.set(5)
e.place(x=400, y=300)
Button(tk, text="转语音", command=wordToFileB).place(x=200, y=330)
Button(tk, text="播语音", command=playFileB).place(x=260, y=330)
tk.mainloop()

# wav_path = input('请输入文件路径:')
# # wavio.write(wav_path)
# r = sr.Recognizer()
# r = sr.Recognizer()
# with sr.AudioFile(wav_path) as source:
#     audio = r.record(source)  # read the entire audio file
#
# res = r.recognize_sphinx(audio)
# res1 = res.split(" ")
# # for each in res1:
# print(" ".join(res1))
