% Returns a single value 
function [t] = Lab1A(np,nd)
if (nargin < 1), np = 1e5; nd = 2; end

% do things in matlab in fairly easy

%list of variables
A = randn(np,nd); 
B = randn(np,nd);
d = zeros(np,1);

% start of the timing
tic;
% number of points 
for i = 1:np
    % number of demensions
    for j = 1:nd
        % Euclidean Distance
        d(i) = d(i) + (B(i,j)-A(i,j)).^2;
    end
    % index of variable of i, and sqrt of the final sum
    d(i) = sqrt(d(i));
end
% end of the timing
toc;
