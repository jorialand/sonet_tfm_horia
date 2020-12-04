function [ r, v ] = KEP2Orbit ( sma, ecc, inc, nu, argp, raan, mu, n )
%KEP2Orbit Get body's orbit
%   Returns the position and velocity of a body throughout a full orbit
%
% Inputs:
%   sma: semi-major axis [km]
%   ecc: eccentricity [#]
%   inc: inclination [rad]
%   nu: true anomaly start value for ecc<1 [rad]. Default 0.0 rad
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
%   [ r, v ] = KEP2Orbit ( 1, 0, 0, 0, 0, 1, 100 );
%
% References:
%	GetBodyKEP, KEP2ICF
%
%David de la Torre Sangra
%January 2015

% Default values
if nargin < 8 || isempty(n), n = 100; end % Default resolution

% Define true anomaly range for the orbit
if ecc < 1, nu = linspace(nu,nu+2*pi,n); % Elliptic/Circular
elseif ecc == 1, nu = linspace(-pi+eps,pi-eps,n); % Parabolic
else, nu = linspace(-acos(-1/ecc)+eps,acos(-1/ecc)-eps,n); % Hyperbolic
end

% Propagate orbit
[ r, v ] = KEP2Arc ( sma, ecc, inc, nu, argp, raan, mu );

end

