function [x, y, u, v] = velfield(n)

if nargin < 1;
    n=15;
end

x=linspace(-0.5*pi, 0.5*pi, n);
[x,y] = meshgrid(x,x);
u=cos(x).*sin(y);
v=-sin(x).*cos(y)



