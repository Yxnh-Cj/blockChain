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
fprintf('��������%f,����ʱ�䣺%f',x1,toc)