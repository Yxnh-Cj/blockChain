clear;clc;
syms x;  % ������ű���
x0 = input('x0=');  % �����ֵ��
y0 = input('y0=');  % �����ֵ�㺯��ֵ
n = length(x0);  % ��ֵ�����
X =zeros(n);
X(:,1)=y0;
y=X(1,1);
lx=1;
for j=2:n
    for i=j:n
        X(i,j)=(X(i,j-1)-X(i-1,j-1))/(x0(i)-x0(i-j+1));
    end
    lx = lx*(x-x0(j-1));
    y = y+X(i,j)*lx;
end
X
y
p = expand(y)
vpa(subs(p,x,2),5)