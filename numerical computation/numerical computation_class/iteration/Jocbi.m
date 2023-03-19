clear;clc;
A = input('A=');
b = input('b=');
x0 =input('x0=');
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
%雅克比迭代
x=inv(D)*(b-(L+U)*x0);
while max(abs(x-x0))>=er
    x0=x;
    x=inv(D)*(b-(L+U)*x0);
end
x