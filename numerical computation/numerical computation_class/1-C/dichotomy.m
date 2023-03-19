close;clear;clc;
a = input('a = ');
b = input('b = ');
er = input('er = ');
while abs(b-a)>=er
    x = (a+b)/2;
    if fun(a)*fun(x)<0
        b = x;
    else
        a = x;
    end
end
x