import requests
import re
import tkinter as tk
import webbrowser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
url = 'https://v.ctrlqq.com/'
response = requests.get(url, headers=headers)
html = response.text
pattern = re.compile('<option.value="(.*?)"')
url_lis = re.findall(pattern, html)

root = tk.Tk()
root.geometry('500x300')  # 设置窗口“宽x高”
root.title('vip电影播放')  # 设置窗口名称
na = tk.Label(root, text='播放接口:', font=12)  # 往窗口上放置文字，并设置字体大小
na.grid()  # 将字体放在root上

num = 0
var = tk.StringVar()
for i in range(0, len(url_lis)):  # 通过循环将每一个播放接口都放到root面板上
    # 如果某一个按钮被选中，那么url_lis的值会通过variable传给var
    name1 = tk.Radiobutton(root, text='播放接口' + str(num + 1), variable=var, value=url_lis[num])
    name1.grid(row=num, column=3)  # 将这个接口放在root面板的第num行，第column列

    num = num + 1

na2 = tk.Label(root, text='播放链接:', font=12)
na2.grid(row=num, column=0)
texts = tk.Entry(root, text='', width=50)  # 输入链接的文本框
texts.grid(row=num, column=3)
num = num + 1


def dispaly():  # 不用系统默认浏览器，我们指定浏览器来打开链接
    chromePath = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    '''
    webbrowser.open(url, new=0, autoraise=True)
    在系统的默认浏览器中访问url地址，如果new=0,url会在同一个浏览器窗口中打开；如果new=1，新的浏览器窗口会被打开;new=2新的浏览器tab会被打开。
    '''
    webbrowser.get('chrome').open(var.get() + texts.get())
    # webbrowser.open(var.get()+texts.get())


# def down_film():
#     res = requests.get(texts.get(), headers=headers)
#     res.encoding = res.apparent_encoding
#     html = res.text
#     pattern1 = '<title>(.*?)</title>'
#     name = re.search(pattern1, html).group(1)
#     print('视频{}已开始下载.......', format(name))
#     url_film = var.get() + texts.get()
#     print(url_film)
#     film = requests.get(url_film, headers=headers).content
#     print(film)
#     with open(name + '.mp4', 'wb') as f:
#         f.write(film)
#     print('视频{}下载完成!', format(name))


bf = tk.Button(root, text='播放', font=12, command=dispaly)  # 设定按钮点击后触发的事件
bf.grid(row=num, column=3)

# bf = tk.Button(root,text='下载',font=12,command=down_film)  #设定按钮点击后触发的事件
# bf.grid(row=num+5,column=3)
# down_film()
root.mainloop()

'''
下面以“大决战奥特八兄弟”这部电影为例，我们先找到他在爱奇艺/腾讯视频/优酷/芒果/土豆/乐视的播放链接
http://www.iqiyi.com/w_19rqswhlx9.html?vfm=m_103_txsp
之后放到程序文本框内就行
'''
