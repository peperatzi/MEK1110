

function[x, y] = Problem1c(a, b, theta)
    x = linspace(a, b, 100);
    y = (x - x.^2)*tan(theta);
end

% Plot 1:
[x, y] = Problem1c(0, 1, pi/6);
plot(x, y, '-r');

hold on

% Plot 2:
[x, y] = Problem1c(0, 1, pi/4);
plot(x, y, '-m');

hold on

% Plot 3:
[x, y] = Problem1c(0, 1, pi/3);
plt = plot(x, y, '-b');

% Setup plot window:
legend('\pi/6','\pi/4','\pi/2');
xlabel('x');
ylabel('y');

axis([0 1, 0, 0.5]);

saveas(plt, 'oppgave_1c.png');


pause()

