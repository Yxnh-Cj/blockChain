clear;clc;
A = input('����ϵ������:');
b = input('����ϵ����');
B = [A,b];
if rank(A)=rank(B)
    x = A\b
    x = inv(A)*b
end