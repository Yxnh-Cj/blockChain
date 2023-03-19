clear;clc;
x0 = input('x0 = ');
x1 = input('x1 = ');
er = input('er = ');
x2 = x1-(newton_iteration_fun(x1)/(newton_iteration_fun(x1)-newton_iteration_fun(x0)))*(x1-x0);
while abs(x2-x1)>=er
    x2 = x1-newton_iteration_fun(x1)*(x1-x0)/(newton_iteration_fun(x1)-newton_iteration_fun(x0));
    x0 = x1;
    x1 = x2;
end
x2