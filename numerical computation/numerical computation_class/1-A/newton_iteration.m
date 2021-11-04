clear;clc;  % 清除工作区数据和清屏
x0 = input('x0 = ');  % 输入初始值
er = input('er = ');  % 输入精度
x1 = x0-newton_iteration_fun(x0)/newton_iteration_fun_dfun(x0);  % 进行一次迭代
tic  % 计时开始
while abs(x1-x0)>=er  % 当低于需要精度时继续循环
    x0 = x1;  % 将x1的值赋给x0
    x1 = x0-newton_iteration_fun(x0)/newton_iteration_fun(x0);  % 进行牛顿迭代法迭代
end  % 循环结束
toc  % 计时结束
fprintf('满足%f的近似值为%f\n',er,x1)  % 输出x1的值