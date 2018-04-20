
% 
[x,y] = meshgrid(0:0.25:3.0, 0:0.25:3.0);
u = cos(x).*sin(y);
v = -sin(x).*cos(y);
plt = quiver(x,y,u,v);

axis([0,3,0,3]);

saveas(plt, 'problem_3b_streamlines.png');

pause();
