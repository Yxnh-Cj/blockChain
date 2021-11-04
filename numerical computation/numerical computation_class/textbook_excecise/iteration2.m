clear;clc;
x0 = input('x0 = ');
er = input('er = ');
x1 = fun2(x0);
tic
while abs(x1-x0)>=er
    x0 = x1;
    x1 = fun2(x0);
end
toc
fprintf('计算结果：%f,计算时间：%f',x1,toc)