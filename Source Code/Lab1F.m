%function [d,t] = Lab1f(np,nd)
%if (nargin < 1); np = 1e3; nd = 2; end

% declare the number of points and dimensions
np = 1e7; nd = 2;

%Create a pool if it is empty to the specific number of workers.
hp = gcp('nocreate');
if isempty(hp), hp=parpool(4); end


% start the timer 
tic;

% Taking something from the job manager. See a parallel tasks to split up,
% distribute the task to the number of machines in the pool, and return the result to
% the job manager.
spmd
    % A bunch of if conditions and each if conditions returns a value and
    % sent to the next lab index and being received from the past condition.
    if (labindex==1)
            A = randn(np,nd); B = randn(np,nd);
            C = A-B;
            labSend(C,2);
    elseif (labindex==2)
        C = labReceive(1);
        D = C.^2;
        labSend(D,3);
    elseif (labindex==3)
        D = labReceive(2);
        E = sum(D,2);
        labSend(E,4);
        
    elseif (labindex==4)
        E = labReceive(3);
        F = sqrt(E);
    end              


end

% stop the timer 
t = toc;

% Gets the result from the worker by calling their index and storing it in
% to a variable
D = F{4};

