clear;clc;
x = linspace(0,1500)';
n = length(x);
% model a polynomial, y = ax2 + mx +b
a = 1.0;%quadratic - make nonzeros for larger errors
m = 1.0;%slope
b = 1.0;%intercept
sigma = 0.1; %standard deviation of the noise
y0 = a*x.^2 + m*x + b;
y = y0 + sigma*randn(n,1);
% 线性回归
a = [x ones(n,1)];
c = pinv(a)*y;
yR = c(1)*x+ c(2); %the fitted line
%线性回归作图

h = figure;
h.Name = 'Linear_Regression';
plot(x,y);hold on;
plot(x,yR,'linewidth',2);
grid on;
xlabel('x');

ylabel('y');
title('Linear Regression');
legend('Data','Fit')

figure('Name','Regression Error')
plot(x,yR-y0);
grid on;
xlabel('x');
ylabel('\Delta y');
title('Error between Model and Regression')