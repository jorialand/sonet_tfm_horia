function [ r, v ] = GetBodyOrbit ( body, jd2k, mu, n, planar )
%GETBODYORBIT Get body orbit
%   Returns the position and velocity of a body throughout a full orbit
%
% Inputs:
%   body: body name [string]. Must exist in database
%   epoch: days from J2000 (1 Jan 2000 T12.0) [days]
%   mu: standard gravitational parameter [km2/s2]. Default Sun
%   n: number of points to return. Default 100
%
% Outputs:
%   r: position in ICF [km]
%   v: velocity in ICF [km/s]
%
% Example:
%   [ r, v ] = GetBodyOrbit ( 'Earth', 7300 );
%
% References:
%   [-]
%
% See also:
%	GetBodyKEP, KEP2Orbit
%
%David de la Torre Sangra
%January 2015

% Standard gravitational parameter of Sun [km^3 s^-2]
if nargin < 3 || isempty(mu), mu = GetBodyProps('Sun'); end

% Orbit resolution [steps]
if nargin < 4 || isempty(n), n = 100; end

% Planar orbit [-]
if nargin < 5 || isempty(planar), planar = 0; end

% Get Orbital elements of body at epoch
[ sma, ecc, inc, nu, argp, raan ] = GetBodyKEP ( body, jd2k );

% Fix planar orbit
if planar, inc = 0; end

% Get position and velocity on a complete orbit
[ r, v ] = KEP2Orbit ( sma, ecc, inc, nu, argp, raan, mu, n );

end

