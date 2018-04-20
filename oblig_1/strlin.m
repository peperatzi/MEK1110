
for n=[5 30]
    [x, y, psi] = streamfun(n);
    plt = figure;
    contour(x, y, psi);
    title(sprintf('n = %d', n));
    saveas(plt, sprintf('Problem4a_%d.png', n));
end


pause();


