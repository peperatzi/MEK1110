
n = 20;
[x,y,u,v] = velfield(n);
plt = figure;
quiver(x,y,u,v);
saveas(plt, sprintf('Problem4b_%d.png', n));
pause();




