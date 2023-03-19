function y = Jocbi_fun(A,b,x0,er)
d = diag(diag(A));
l = triu(A)-d;
u = tril(A)-d;
x1 = inv(d)*(b-(l+u)*x0);
while norm(x1-x0,inf)>=er
    x0 = x1;
    x1 = inv(d)*(b-(l+u)*x0);
end
x1


end

