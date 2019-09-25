% Declaring variables for number of points, dimensions, and workers
np=1e7; nd=10; nl = 8;

% number of workers
hp = gcp('nocreate');
% create a pool if it is empty to the specific number of worker
if isempty(hp), hp=parpool(nl); end
%start the timer 
tic;
% MATLAB executes the code within the SPMD body denoted by STATEMENTS on
% several MATLAB workers simultaneously
spmd
    npp1 = floor(np/nl); % # pts per lab
    np1o = np-nl*npp1; % #pts left over 
    if (labindex==1)
        npt1 = npp1+np1o; % #pts for this Lab
    else 
        npt1 = npp1;
    end 
        
    % Declare variables to all the workers
    A = randn(np/nl, nd); B = randn(np/nl,nd);
    d = zeros(np/nl,1);
    % Run the for loop of the algorithm
    for i = 1:np/8
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