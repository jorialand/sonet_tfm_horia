function [ r, v ] = ICF2Arc ( r1, v1, r2, v2, mu, n )
%ICF2ARC Get body's orbit range
%   Returns the position and velocity of a body throughout a partial orbit
%
% Inputs:
%   r_ijk: position vector [km]
%   v_ijk: velocity vector [km/s]
%   mu: standard gravitational parameter of the central body [km^3 s^-2]
%   n: number of points to return. Default 100
%
% Outputs:
%   r: position in ICF [km]
%   v: velocity in ICF [km/s]
%
% Example:
%   [ r, v ] = ICF2Arc ( [1,0,0], [0,1,0], [0,1,0], [-1,0,0], 1, 100 );
%
% References:
%   ICF2KEP, KEP2Orbit
%
%David de la Torre Sangra
%January 2015

% Default inputs
if nargin < 6 || isempty(n), n = 100; end

% Get orbital elements
[ sma, ecc, inc, nu1, argp, raan ] = ICF2KEP_O ( r1, v1, mu );
[ ~, ~, ~, nu2, ~, ~ ] = ICF2KEP_O ( r2, v2, mu );

% Get true anomaly range
if nu2 < nu1, nu2 = nu2 + 2*pi; end % Enforce forward orbit
nu = linspace(nu1,nu2,n); % True anomaly range

% Get position and velocity on a complete orbit
[ r, v ] = KEP2Arc ( sma, ecc, inc, nu, argp, raan, mu );

end

