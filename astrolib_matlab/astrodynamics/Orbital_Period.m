function [ T ] = Orbital_Period ( sma, mu )
%ORBITAL_PERIOD Orbital period
%   Returns the orbital period of a body
%
% Inputs:
%   sma: semi-major axis of body [km]
%   mu: standard gravitational parameter of central body [km3/s2]
%
% Outputs:
%   T: orbital period [s]
%
% Example:
%   [ T ] = Orbital_Period ( 1, 1 );
%
%David de la Torre Sangra
%UPC/ESEIAAT 2017

% Compute period
T = 2*pi * sqrt(sma^3 / mu);

end

