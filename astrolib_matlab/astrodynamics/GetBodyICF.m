function [ r_icf, v_icf ] = GetBodyICF ( body, jd2k, mu, planar )
%GETBODYICF Get body ICF state vector
%   Returns the position and velocity of a celestial body at a given
%   Calendar/J2000 date
%
% Inputs:
%   body: body full name [string]
%   jd2k: days from J2000
%   mu: standard gravitational parameter of parent [km^3 s^-2]. Default Sun
%
% Outputs:
%   r_icf: position in ICF [km]
%   v_icf: velocity in ICF [km/s]
%
% Example:
%   [ r_icf, v_icf ] = GetBodyICF ( 'Earth', 7300 );
%
% References:
%	  n/a
%
% See also:
%   GetBodyKEP, KEP2ICF
%
%David de la Torre Sangra
%September 2014

% Default: Standard gravitational parameter (Sun) [km^3 s^-2]
if nargin < 3 || isempty(mu), mu = GetBodyProps('Sun'); end

% Default: 3D scenario
if nargin < 4 || isempty(planar), planar = 0; end

% Get orbital elements for Body @ Date
[ sma, ecc, inc, nu, argp, raan ] = GetBodyKEP ( body, jd2k );

% Force planar scenario
if planar, inc = 0; end

% Convert orbital elements to ICF state vector
[ r_icf, v_icf ] = KEP2ICF_O ( sma, ecc, inc, nu, argp, raan , mu );

end

