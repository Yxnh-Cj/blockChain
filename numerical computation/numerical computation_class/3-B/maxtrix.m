clear;clc;
a = input('输入系数矩阵：');
b = input('输入系数：');
n = length(b);
for k=1:(n-1)
    for i=(k+1):n
        m(i,k)=-a(i,k)/a(k,k);
        a(i,k)=0;
        for j=(k+1):n
            a(i,j)=a(i,j)+m(i,k)*a(k,j);
        end
        b(i)=b(i)+m(i,k)*b(k);
    end
end
x(n)=b(n)/a(n,n);
for k=n-1:-1:1
    s=0;
    for j=(k+1):n
        s=s+a(k,j)*x(j);
    end
    x(k)=(b(k)-s)/a(k,k);
end                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
x