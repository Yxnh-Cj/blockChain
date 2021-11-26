clear;clc;
a=input('a=');
b=input('b=');
c=input('c=');
d=input('d=');
n=length(b);
q(1)=b(1);
for i=2:n
    p(i)=a(i)/q(i-1);
    q(i)=b(i)-p(i)*c(i-1);
end
%»Ø´ú
y(1)=d(1);
for j=2:n
    y(j)=d(j)-p(j)*y(j-1);
end
x(n)=y(n)/q(n);
for k=n-1:-1:1
    x(k)=(y(k)-c(k)*x(k+1))/q(k);
end
x