clear;clc;
x0 = input('x0 = ');
er = input('er = ');
x = x0-fun(x0)/dfun(x0);
while abs(x-x0)>=er
    x0 = x;
    x = x0-fun(x0)/dfun(x0);
end
x