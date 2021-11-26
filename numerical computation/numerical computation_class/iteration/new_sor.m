clear;clc;
A=input('A=');
b=input('b=');
x0=input('x0=');
x = input('x=');
er=input('er=');
d = diag(diag(A));
l = tril(A)-d;
u = triu(A)-d;
w = 1.3;
x1=vpa(inv(d+w*l)*(((1-w)*d-w*u)*x0+w*b),8);
while norm(x1-x,2)>=er
    x0 = x1;
    x1=vpa(inv(d+w*l)*(((1-w)*d-w*u)*x0+w*b),8);
end
x1