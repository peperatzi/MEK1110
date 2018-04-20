
% Load data. 
A = load("data.mat");

size(A.x)
%size(A.y)
%size(A.u)
%size(A.v)
%size(A.xit)
%size(A.yit)

for i=1:201
    for j = 1:191
        curr = A.x(i,j);
        next = A.x(i,j+1);
        if (next-curr) != 0.5
            disp("Glitch in the matrix!")
        end
    end
end

%[X,Y] = meshgrid(A.xit,A.yit)

%contour(A.x,A.y,A.u,A.v)

%quiver(A.x(1,10,end),A.y(1,10,end),A.u,A.v)
%plot(A.x(1,2,end),A.y(1,2,end))

%pause()

