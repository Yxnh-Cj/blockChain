# # 画函数图
# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(1,11)  # 默认为1行，从np.arange(m,n)从m按步长为1加到n
# # print(x)  # [ 1  2  3  4  5  6  7  8  9 10]
# y = np.exp(x)
# # print(y)  # [2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01
# #  1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03
# #  8.10308393e+03 2.20264658e+04]
# plt.title("Matplotlib Demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x,  y)
# plt.show()

# 求矩阵的逆及线性方程组的解
import numpy as np
from matplotlib import pyplot as plt


a = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
b = np.array([[6], [-4], [27]])
ni = np.linalg.inv(a)
print(ni)  # 输出逆矩阵
print(np.linalg.solve(a, b))  # 输出方程组的解
# x = np.arange(-5,5)
# l1 = a[0]*x
# l2 = a[1]*x
# l3 = a[2]*x
# plt.plot(l1,l2,l3)
# plt.show()
