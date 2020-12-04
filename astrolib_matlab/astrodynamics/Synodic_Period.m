function [ Ts ] = Synodic_Period ( sma1, sma2, mu )
%SYNODIC_PERIOD Synodic period
%   Returns the synodic period between two celestial bodies
%
% Inputs:
%   sma1: semi-major axis of first body [km]
%   sma2: semi-major axis of second body [km]
%   mu: standard gravitational parameter of central body [km3/s2]
%
% Outputs:
%   Ts: synodic period [s]
%
% Example:
%   [ Ts ] = Synodic_Period ( 1, 2, 1 );
%   [ Ts ] = Synodic_Period ( 'Earth', 'Mars' ); % Earth -> Mars
%   [ Ts ] = Synodic_Period ( 'Earth', 'Venus' ); % Venus -> Earth
%
%David de la Torre Sangra
%June 2017

% Get mu of Sun as default
if nargin < 3 || isempty(mu)
    mu = GetBodyProps('Sun');
end

% Get bodies sma if string inputs
if ischar(sma1) && ischar(sma2)
    sma1 = GetBodyKEP(sma1,0);
    sma2 = GetBodyKEP(sma2,0);
end

% Compute period of bodies
T1 = Orbital_Period ( sma1, mu );
T2 = Orbital_Period ( sma2, mu );

% Compute synodic period between bodies
Ts = 1.0 / abs( 1.0/T1 - 1.0/T2 );

end

