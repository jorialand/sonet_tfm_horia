function [ nr1, nr2, ntof, nmu, xr, xt, xmu ] = NorMag_Lambert ( ...
    r1, r2, tof, mu )
%NorMag_Lambert Normalize Lambert magnitudes
%   Normalizes magnitudes - Specific for Lambert algorithms
%
%   Note: input magnitudes units must be consistent.
%
% Inputs:
%   r1: position vector of departure point [km]
%   r2: position vector of arrival point [km]
%   tof: time of flight [s]
%   mu: standard gravitational parameter of the central body [km3/s2]
%
% Outputs:
%   r1: position vector of departure point [normalized]
%   r2: position vector of arrival point [normalized]
%   tof: time of flight [normalized]
%   mu: standard gravitational parameter of the central body [normalized]
%   xr: normalization factor [length]
%   xt: normalization factor [time]
%   xmu: normalization factor [mu]
%
% Example:
%   AU = 149.597870E6; % AU [km]
%   r1 = [1.0*AU,0,0];
%   r2 = [1.2*AU,3*AU,0];
%   tof = 182*86400; % 182 days
%   mu = 1.32712440018E11; % Gravitational parameter of Sun [km3/s2]
%   [ nr1, nr2, ntof, nmu ] = NormalizeUnits_Lambert( r1, r2, tof, mu );
%
% References:
%	[1] Bate, Roger R., D.D. Mueller, and J.E. White
%       Fundamentals of Astrodynamics, Section 5.3
%       New Dover Publications, New York, 1971
%
%David de la Torre Sangra
%September 2015

% Normalization factors [1] (Eq. 1.11)
xr = norm(r1); % Normalising factor for R [km]
xt = xr / sqrt(mu / xr); % Normalising factor for time [s]
xmu = xr^3 / xt^2; % Normalising factor for mu [km^3 s^-2]

% Normalised magnitudes
nr1 = r1 / xr;
nr2 = r2 / xr;
ntof = tof / xt;
nmu = mu / xmu;

end

