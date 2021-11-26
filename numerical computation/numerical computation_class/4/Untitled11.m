clear;clc;
A = input('输入系数矩阵:');
b = input('输入系数：');
B = [A,b];
if rank(A)=rank(B)
    x = A\b
    x = inv(A)*b
end