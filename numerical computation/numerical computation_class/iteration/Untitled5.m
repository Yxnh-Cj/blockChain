switch(lower(action))
    case 'defaults'
        m=Defaults;
    case 'initialize'
        if (nargin<2)
            d=Defaults;
        else
            d = x;
        end
        p = Initialize(d);
    case 'update'
        if (nargout==1)
            m = Update(p,x);
        else
            Update(p,x);
        end
end
