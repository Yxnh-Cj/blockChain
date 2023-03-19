clear;clc;  % 清除工作区数据和清屏
x0 = input('x0 = ');  % 输入初始值
er = input('er = ');  % 输入精度
x1 = simple_iteration(x0);  % 迭代一次
tic  % 计时开始
while abs(x0-x1)>=er  % 当低于误差精度时继续循环
    x0 = x1;  % 将x1的值赋值给x0继续循环
    x1 = simple_iteration(x0);  % 再次进行迭代
end  % 循环结束
toc  % 计时结束
fprintf('不超过%f的近似值为：%f\n',er,x1)  % 输出满足精度的近似值