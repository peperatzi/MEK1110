x = linspace(-5, 5, 10);
y = linspace(-5, 5, 10);

[x, y] = meshgrid(x,y);

u = x.*y;
v = y;

plt = figure;

quiver(x, y, u, v, 0.7);
hold on;

c = y - log(abs(x));

contour(x, y, c);

saveas(plt, 'Problem2b.png');

pause();
