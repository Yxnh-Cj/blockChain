clear;clc;
x0 = input('x0 = ');
x1 = input('x1 = ');
er = input('er = ');
x2 = x1 - fun1(x1)*(x1-x0)/(fun1(x1)-fun1(x0));
while abs(x2-x1)>=er
    x0 = x1;
    x1 = x2;
    x2 = x1 - fun1(x1)*(x1-x0)/(fun1(x1)-fun1(x0));
end
x2