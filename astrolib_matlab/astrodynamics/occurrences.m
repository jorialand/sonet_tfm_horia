function [count] = occurrences(vec)
% Input: A vector or matrix.
% Output: Number of ones.
% ocurrences: Counts and returns the number of ones (occurrences) in a vector or
% matrix.

count = sum(vec(:)>0);
end

