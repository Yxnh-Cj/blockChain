clear;clc;
syms x;
x0 = input('x=');
y0 = input('y=');
n = length(x0);
L=0;
for i=1:n
    t = x0;
    t(i)=[];
    l(i) = prod((x-t)./(x0(i)-t));
    L=L+l(i)*y0(i);
end
%simplify(L)
vpa(L)
expand(L)
vpa(subs(L,x,2.5),5)