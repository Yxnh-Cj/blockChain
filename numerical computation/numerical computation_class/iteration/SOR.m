clear;clc;
A = input('A=');
b = input('b=');
x0 = input('x0=');%x0为初始近似解
x = input('x=');%x为为精确�?
er = input('er=');
n = length(A);
%取出L
L = zeros(n,n);U=L;
for i=2:n
    for j=1:i-1
        L(i,j)=A(i,j);
    end
end
%取出U
for s=1:n
    for t=s+1:n
        U(s,t)=A(s,t);
    end
end
D = A-L-U;
%SOR迭代
w = 1.9;k=0;
x1=inv(D+w*L)*(((1-w)*D-w*U)*x0+w*b);%x1为x在G-S方法�?��的近似解
while sqrt((x1-x)'*(x1-x))>=er
    x0 = x1;
    x1 = inv(D+w*L)*(((1-w)*D-w*U)*x0+w*b);
    k=k+1;
end
x1
k+1