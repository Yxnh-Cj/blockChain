clear;clc;
syms x;  % ������ű���
x0 = input('x0=');  % �����ֵ��
y0 = input('y0=');  % �����ֵ�㺯��ֵ
n = length(x0);  % ��ֵ�����
X =zeros(n);
X(:,1)=y0;
for i=1:n
    for j=i+1:n
        X(i,j)=(X(i+1,j-1)-X(i,j-1))/(x0(j)-x0(j-i+1));
    end        
end
X