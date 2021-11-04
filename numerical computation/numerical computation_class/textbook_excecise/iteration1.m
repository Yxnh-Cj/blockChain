clear;clc;
x0 = input('x0 = ');
er = input('er = ');
x1 = fun1(x0);
tic
while abs(x1-x0)>=er
    x0 = x1;
    x1 = fun1(x0);
end
toc
fprintf('计算结果：%f\n计算时间：%f\n',x1,toc)