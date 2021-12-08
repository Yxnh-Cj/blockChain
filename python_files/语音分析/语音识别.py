from aip import AipSpeech
APP_ID="xxx"
API_KEY="xxxxx"
SECRET_KEY="xxxxxxxxxxxxxxx"
#初始化语音识别客户端
client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
#客户端合成文本生成结果，vol-指定语速
result=client.synthesis(text='我是如此的优秀，人工智能技术.',options={'vol':5})
#生成为语音格式文件
if not isinstance(result,dict):
    with open('1.mp3','wb') as f:
        f.write(result)
else:
    print(result)