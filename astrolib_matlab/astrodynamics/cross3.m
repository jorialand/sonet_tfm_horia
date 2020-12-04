function [ rxv ] = cross3 ( r, v )
%CROSS3 Cross product
%   Returns the cross product between two 3D vectors

rxv = [ r(2)*v(3) - r(3)*v(2), ...
        r(3)*v(1) - r(1)*v(3), ...
        r(1)*v(2) - r(2)*v(1) ];

end

