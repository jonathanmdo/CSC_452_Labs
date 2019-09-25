% Returns a single value
function [t] = Lab1B(np,nd,nw)
if (nargin < 1); np = 1e7; nd = 2; nw=4; end
% number of workers
hp = gcp('nocreate');
% create a pool if it is empty to the specific number of worker
if isempty(hp), hp=parpool(nw); end
A = randn(np,nd); B = randn(np,nd);
d = zeros(np,1);
tic;
% taking a something from the job manager. see a parallel tasks to split
% up, distribute the task to the number of machines in the pool, and return
% the result to the job manager 
parfor i = 1:np
    for j = 1:nd
        d(i) = d(i) + (B(i,j)-A(i,j)).^2;
    end
    d(i) = sqrt(d(i));
end
t = toc;
delete(hp);