clear;clc;
A=input('A=');
b=input('b=');
x0=input('x0=');
er=input('er=');
d = diag(diag(A));
l = tril(A)-d;
u = triu(A)-d;
x1=inv(d+l)*(b-u*x0);
G = [x0';x1'];
while norm(x1-x0,inf)>=er
    x0 = x1;
    x1=inv(d+l)*(b-u*x0);
    G=[G;x1'];
end
G
x1