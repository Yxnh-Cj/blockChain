clear;clc;  % 清除工作区数据和清屏
a = input('请输入左端点值a = ');  % 输入左端点值
b = input('请输入右端点值b = ');  % 输入右端点值
er = input('请输入误差值er = ');  % 输入误差值
tic  % 计时开始
while abs(a-b)>=er  % 当区间长度超过误差值继续循环
    x = (a+b)/2;  % 取中点
    if dichotomy_fun(a)*dichotomy_fun(x)<0  % 零点存在性定理（根存在性定理）保证收敛方向
        b = x;  % 将右端点值赋值给b
    else
        a = x;  % 将左端点值赋值给a
    end
end
toc  % 计时结束
fprintf('结果：%f\n',x)  % 输出结果