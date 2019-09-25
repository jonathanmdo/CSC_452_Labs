% Declaring variables for number of points, dimensions, and workers
np=1e5; nd=10; nl = 4;

% number of workers
hp = gcp('nocreate');
% create a pool if it is empty to the specific number of worker
if isempty(hp), hp=parpool(nl); end
%start the timer 
tic;
% MATLAB executes the code within the SPMD body denoted by STATEMENTS on
% several MATLAB workers simultaneously
spmd
    % Declare variables to all the workers
    nppl = round(np/nl);
    A = randn(nppl,nd); B = randn((nppl),nd);
    d = zeros(nppl,1);
    % Run the for loop of the algorithm
    for i = 1:nppl
        for j = 1:nd
            d(i) = d(i) + (B(i,j) - A(i,j)).^2;
        end
        d(i) = sqrt(d(i));
    end
    % Global Concatenation 
    da = gcat(d,1,1);
end
t = toc;
% The client calls the index of the worker and getting the result
d1 = da{1};