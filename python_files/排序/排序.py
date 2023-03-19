import time, datetime

s1 = s2 = 0


def compare(l_s):
    # l_s = input('输入待比较的数:').split(',')
    l = []  # 接受替换后的值
    start = datetime.datetime.now()
    for k in l_s:
        if type(eval(k)) == type(1.0):  # 值的等价替换
            l.append(float(k))
        elif type(eval(k)) == type(1):
            l.append(int(k))
        elif type(eval(k)) == type((1 + 0j)):
            l.append(complex(k))
        else:
            print('输入错误。')
    l1 = l.copy()

    for i in range(1, len(l)):  # 排序开始
        for j in range(i):
            if l[j] <= l[i]:  # 里面的元素与外面进行比较
                pass
            else:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    # l1 = l.copy()  # 用于升序输出
    # l1.reverse()  # 倒置
    # print(f'升序输出:{l},降序输出:{l1}',sep='\n')  # 输出结果
    # print(l)
    end = datetime.datetime.now()
    # print(end - start)

    # l_s = input('输入:').split(',')
    # l = []
    l = l1
    start_ = datetime.datetime.now()
    # for k in l_s:
    #     if type(eval(k)) == float:
    #         l.append(float(k))
    #     elif type(eval(k)) == int:
    #         l.append(int(k))

    if len(l) % 2 != 0:
        for i in range(1, int((len(l) - 1) / 2)):
            for j in range(i):
                if l[j] <= l[i]:  # 里面的元素与外面进行比较
                    pass
                else:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
        for i in range(int((len(l) + 1) / 2)-1, len(l)):
            for j in range(i):
                if l[j] <= l[i]:  # 里面的元素与外面进行比较
                    pass
                else:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
    else:
        for i in range(1, int(len(l) / 2)):
            for j in range(i):
                if l[j] <= l[i]:  # 里面的元素与外面进行比较
                    pass
                else:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
        for i in range(int(len(l) / 2), len(l)):
            for j in range(i):
                if l[j] <= l[i]:  # 里面的元素与外面进行比较
                    pass
                else:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
    # print(l)
    end_ = datetime.datetime.now()
    # print(end_ - start_)
    global s1, s2
    if (end - start) >= (end_ - start_):
        s2 += 1
    else:
        s1 += 1
    return l


if __name__ == '__main__':
    n = int(input('输入次数:'))
    l_s = input('输入待比较的数:').split(',')
    for i in range(n):
        compare(l_s)
    print(compare(l_s))
    if s1>s2:
        print(f'总的来说，在{n}次实验中方法1相对来方法2平均快{abs((s1-s2)/n)}秒.')
    elif s1==s2:
        print(f'总的来说，{n}次实验中,方法1等同于方法2,时间为{s1}秒.')
    else:
        print(f'总的来说，在{n}次实验中方法2相对来方法1平均快{abs((s1-s2)/n)}秒.')

# import datetime
#
#
# def way1(l):
#     global start,end
#     start = datetime.datetime.now()
#     for i in range(1, len(l)):  # 排序开始
#         for j in range(i):
#             if l[j] <= l[i]:  # 里面的元素与外面进行比较
#                 pass
#             else:
#                 temp = l[i]
#                 l[i] = l[j]
#                 l[j] = temp
#     end = datetime.datetime.now()
#
#
# def way2(l):
#     global start_,end_
#     start_ = datetime.datetime.now()
#     if len(l) % 2 != 0:
#         for i in range(1, int((len(l) - 1) / 2)):
#             for j in range(i):
#                 if l[j] <= l[i]:  # 里面的元素与外面进行比较
#                     pass
#                 else:
#                     temp = l[i]
#                     l[i] = l[j]
#                     l[j] = temp
#         for i in range(int((len(l) + 1) / 2)-1, len(l)):
#             for j in range(i):
#                 if l[j] <= l[i]:  # 里面的元素与外面进行比较
#                     pass
#                 else:
#                     temp = l[i]
#                     l[i] = l[j]
#                     l[j] = temp
#     else:
#         for i in range(1, int(len(l) / 2)):
#             for j in range(i):
#                 if l[j] <= l[i]:  # 里面的元素与外面进行比较
#                     pass
#                 else:
#                     temp = l[i]
#                     l[i] = l[j]
#                     l[j] = temp
#         for i in range(int(len(l) / 2), len(l)):
#             for j in range(i):
#                 if l[j] <= l[i]:  # 里面的元素与外面进行比较
#                     pass
#                 else:
#                     temp = l[i]
#                     l[i] = l[j]
#                     l[j] = temp
#     end_ = datetime.datetime.now()
#     print(l)
#
#
# if __name__ == '__main__':
#     n = int(input('输入次数:'))
#     s = input('输入:').split(',')
#     l = []
#     for k in s:
#         l.append(eval(k))
#     l1 = l.copy()
#     start = end = s1 = 0
#     start_ = end_ = s2 = 0
#     for i in range(n):
#         way1(l)
#         way2(l1)
#         if (end-start)>(end_-start_):
#             s2 = s2+1
#         elif (end-start)==(end_-start_):
#             pass
#         else:
#             s1 = s1+1
#     if s2>s1:
#         print(f'方法1在{n}次实验中更好。')
#     elif s1==s2:
#         print(f'在{n}次实验中方法1实验速度等于方法二。')
#     else:
#         print(f'方法1在{n}次实验中更好。')