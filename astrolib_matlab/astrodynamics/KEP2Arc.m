function [ r, v ] = KEP2Arc ( sma, ecc, inc, nu, argp, raan, mu )
%KEP2Arc Get body's orbital arc
%   Returns the position and velocity of a body throughout an orbital arc
%
% Inputs:
%   sma: semi-major axis [km]
%   ecc: eccentricity [#]
%   inc: inclination [rad]
%   nu: true anomaly range (min,max) [rad]. Default full orbit
%   argp: argument of periapsis [rad]
%   raan: right ascension of ascending node [rad]
%   mu: standard gravitational parameter of the central body [km^3 s^-2]
%   n: number of points to return. Default 100
%
% Outputs:
%   r(:,3): position in ICF [km]
%   v(:,3): velocity in ICF [km/s]
%
% Example:
%   [ r, v ] = KEP2Arc ( 1, 0, 0, linspace(0,pi/2,100), 0, 1, 100 );
%
% References:
%   [-]
%
% See also:
%	GetBodyKEP, KEP2ICF
%
%David de la Torre Sangra
%January 2015

% Preallocate orbital position/velocity array
n = length(nu);
r = zeros(n,3);
v = zeros(n,3);

% Propagate orbit
for k=1:n
    
    % Orbital elements to position and velocity
    [r(k,:), v(k,:)] = KEP2ICF_O ( sma, ecc, inc, nu(k), argp, raan, mu );
    
end

end

