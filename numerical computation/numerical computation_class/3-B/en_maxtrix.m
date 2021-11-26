clear;clc;
a = input(' ‰»Î‘ˆπ„æÿ’Û£∫');
n = size(a,1);
for k=1:n-1
    for i=(k+1):n
        m(i,k)=-a(i,k)/a(k,k);
        a(i,k)=0;
        for j=(k+1):(n+1)
            a(i,j)=a(i,j)+m(i,k)*a(k,j);
        end
    end
end
x(n)=a(n,n+1)/a(n,n);
for k=(n-1):-1:1
    s = 0;
    for j=(k+1):n
        s = s+a(k,j)*x(j);
    end
    x(k)=(a(k,n+1)-s)/a(k,k);
end
x