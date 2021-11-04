close;clear;clc;
x0 = input('x0 = ');
er = input('er = ');
x = fun1(x0);
while abs(x0-x)>=er
    x0 = x;
    x = fun1(x0);
end
x