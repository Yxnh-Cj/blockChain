a = input('a=');
b = input('b=');
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
for k=(n-1):(-1):1
    sum = 0;
    for j = (k+1):n
        sum = sum+a(k,j)*x(j);
    end
    x(k)=(b(k)-sum)/a(k,k);
end
x