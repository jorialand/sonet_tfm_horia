function [ n ] = norm3( r )
%NORM3 Vector norm
%   Returns the norm of a 3D vector

n = sqrt(r(1)*r(1) + r(2)*r(2) + r(3)*r(3));

end

