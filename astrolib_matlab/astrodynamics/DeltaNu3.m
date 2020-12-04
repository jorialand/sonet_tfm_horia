function [ dnu ] = DeltaNu3 ( r1, r2, prograde )
%DeltaNu3 True anomaly difference
%   Computes the angle between two 3D vectors.
%
% Inputs:
%   r1: first vector [r1x,r1y,r1z]
%   r2: second vector [r2x,r2y,r2z]
%   prograde: prograde motion (1), retrograde motion (0). Default 1
%
% Outputs:
%   dnu: angle between vectors [rad]
%
% Example:
%   [ dnu ] = DeltaNu3 ( [1 0 1], [-1 -1 1], 1 );
%
% References:
%   [1] Curtis D25
%
%David de la Torre Sangra
%August 2014

% Define default motion (prograde)
if nargin < 3 || isempty(prograde), prograde = true; end

% Compute cosine (dot product)
A = acos(dot(r1,r2) / (norm(r1) * norm(r2)));

% Compute sine (cross product)
B = cross(r1,r2);
Bz = B(3); % Get z-component

% Check motion case
if prograde % Prograde motion
    if Bz >= 0, dnu = A;
    else, dnu = 2*pi - A;
    end
else % Retrograde motion
    if Bz < 0, dnu = A;
    else, dnu = 2*pi - A;
    end
end

end

