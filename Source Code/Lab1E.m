%function [t] = Lab1e(np,nd)
%if (nargin < 1); np = 1e6; nd = 2; nw=4; end

% Declare variables
np = 1e6; nd = 2;
% number of workers
hp = gcp('nocreate');
% create a pool if it is empty to the specific number of worker
if isempty(hp), hp=parpool(8); end
% assign a random number between number of points and number of dimensions
aA = randn(np,nd); aB = randn(np,nd);
% combined memory of multiple to store the elements of an array 
dA = distributed(aA); dB = distributed(aB);
% Matrix of zeros of numbers of pool by 1
d = zeros(np,1);
tic;
% Do the algorithm
dc = sqrt(sum((dA-dB).^2,2));
% Returns an array in the local workspace
c = gather(dc);
% stop the timer
t = toc;

%delete(hp);