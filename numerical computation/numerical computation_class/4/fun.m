function [x1 x2 x3 x4 x5] = fun(t,n)
a=t(1:n);b=t(n+1:2*n);c=t(2*n+1:3*n-1);d=t(3*n:4*n-1);
q(1)=b(1);
for i=2:n
    p(i)=a(i)/q(i-1);
    q(i)=b(i)-p(i)*c(i-1);
end
y(1)=d(1);
for j=2:n
    y(j)=d(j)-p(j)*y(j-1);
end
x(n)=y(n)/q(n);
for k=n-1:-1:1
    x(k)=(y(k)-c(k)*x(k+1))/q(k);
end
x

end

