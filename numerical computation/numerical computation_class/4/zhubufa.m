%消元过程
clear;clc;
a = input('输入矩阵：');
U(1,1)=a(1,1);
n = length(a);
for i=2:n
    L(i-1,i-1)=1;
    U(i-1,i)=a(i-1,i);
    L(i,i-1)=a(i,i-1)/U(i-1,i-1);
    L(i,i)=1;
    U(i,i)=a(i,i)-L(i,i-1);
end

%回代过程
d = input('输入系数：');
y(1)=d(1);
for k=2:n
    y(k)=d(k)-L(k,k-1)*y(k-1);
end
x(n)=y(n)/U(n,n);
for l=n-1:-1:1
    x(l)=(y(l)-a(l,l+1)*x(l+1))/U(l,l);
end
x