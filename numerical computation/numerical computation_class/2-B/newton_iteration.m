clear;clc;
x0 = input('x0 = ');
er = input('er = ');
x1 = x0 - fun(x0)/dfun(x0);
while abs(x1-x0)>=er
    x0 = x1;
    x1 = x0 - fun(x0)/dfun(x0);
end
x1