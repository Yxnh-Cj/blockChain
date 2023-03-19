# -*- coding: utf-8 -*-  # 原因：Python默认是以ASCII作为编码方式的，如果在自己的Python源码中包含了中文（或者其他的语言，比如小日本的日语……），
# 此时即使你把自己编写的Python源文件以UTF-8格式保存了；但实际上，这依然是不行的。
import requests
from bs4 import BeautifulSoup  # 通过BeautifulSoup库能很好地解析Requests库请求的网页，

# 并把网页源代码解析成Soup文档，以便过滤提取数据（Soup文档按标准的缩进格式的结构输出为结构化的数据，为数据的过滤提取做好准备）
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4636.4 Safari/537.36'}
# s = 'y'
# while s=='y':
#     url = input('请输入网址:')
#     res = requests.get('{}'.format(url),headers=headers)
#     # res = res.text  # 将网页反映码以网页源码输出
#     # print(res)
#     try:
#         soup = BeautifulSoup(res.text,'html.parser')  # 支持的python标准库中的HTML解析器（lxml HTML、Lxml XML、html5lib）
#         print(soup.prettify())
#     except ConnectionError:
#         print('拒绝连接。')
#     s = input('是否继续(y/n):')

# l = input('输入:').split(',')
# l1 = []
# for i in l:
#     l1.append(int(i))
#
# sum_ = sum(l1)/10

# ABC分类线性规划权重规划
# if __name__ == '__main__':
#     try:
#         while True:  # 一直执行
#             s = input('输入:').split(',')  # 将输入数据用逗号隔开，分割成列表，每个元素是字符串类型（将输入字符串用逗号分割成每个字符串元素组合成列表）
#             l = []  # 用于保存字符串转换成数值格式的数值集
#             for k in s:  # for循环取遍s列表中的值
#                 l.append(eval(k))  # 添加转换后的值，eval函数中针对字符串
#             sum_ = max(l)/(sum(l)*10)  # 线性规划转换成代码
#             sum1 = 0  # 用于累加值
#             for i in l:  # 用for循环取遍列表数值
#                 sum1 += i*sum_  # 累加
#             print(sum1)  # 输出计算权重结果
#     except Exception as e:
#         print(e)
#     else:
#         print('没有异常')
#     finally:
#         pass

'''二项式系数'''


# 特殊情形：杨辉三角
try:  # 异常处理
    n = eval(input('输入行数:'))  # 接受用户输入行数值


    def Factorial(n):  # 定义一个计算阶乘的函数
        m = 1  # 阶乘初始值
        if n == 0:  # 0的阶乘等于1
            return 1  # 返回0的阶乘值1
        else:  # 非零整数阶乘值计算
            for i in range(1, n + 1):  # for循环遍历从1到n的整数值
                m = m * i  # 累乘求得阶乘值
            return m  # 返回阶乘值


    for i in range(0, n):  # 行数
        for j in range(0, i + 1):  # 组合数上限
            print(int(Factorial(i) / (Factorial(j) * Factorial(i - j))), end=' ')  # 组合数计算
        print()  # 每输出一行就换行
except Exception as e:  # 万能异常排除
    print(e)  # 输出异常原因
finally:  # 无论是否异常都输出的值
    pass  # pass作为占位code

# 一般情形:（非正整数阶乘）
