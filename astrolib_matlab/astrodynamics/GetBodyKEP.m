function [ sma, ecc, inc, nu, argp, raan ] = GetBodyKEP ( body, jd2k, DB )
%GETBODYKEP Get body's orbital elements
%   Returns the classical orbital elements for the given body.
%   Auto-assigns the appropiate orbital elements databases if required.
%
%   WRAPPER FUNCTION
%
% Inputs:
%   body: name of the target planet [string]
%   JD2K: days from J2000 (1 Jan 2000 T12.0) [days]
%   DB: orbital elements database [function handle]
%
% Outputs:
%   sma: semi-major axis [km]
%   ecc: eccentricity (0=circular, <1=elliptic, 1=parabolic, >1=hyperbolic)
%   inc: inclination to the ecliptic [rad]
%   nu: true anomaly [rad]
%   argp: argument of periapsis [rad]
%   raan: right ascension of the ascending node [rad]
%
% Example:
%   [ sma, ecc, inc, nu, argp, raan ] = GetBodyKEP ( 'Mars', 7300 );
%
% References:
%   n/a
%
% See also:
%   GetBodyKEP_SSDG, GetBodyKEP_Izzo, GetBodyKEP_Schlyter
%
%David de la Torre Sangra
%May 2016

% Auto-assign batabase as function of the input body
if nargin < 3 || isempty(DB)
    
    % Planetary bodies
    PL = cell(11,1);
    PL{1} = 'Sun';
    PL{2} = ['Mercury,Venus,Earth,Mars,',...
        'Jupiter,Saturn,Uranus,Neptune,Pluto'];
    PL{3} = 'Pluto,Ceres,Makemake,Haumea,Eris';
    PL{4} = 'Moon';
    PL{5} = 'Phobos,Deimos';
    PL{6} = ['Ganymede,Callisto,Io,Europa,',...
        'Amalthea,Thebe,Adrastea,Metis'];
    PL{7} = ['Mimas,Enceladus,Tethys,Dione,Rhea,',...
        'Titan,Hyperion,Iapetus,Phoebe'];
    PL{8} = '';
    PL{9} = '';
    PL{10} = 'Charon,Styx,Nix,Kerberos,Hydra';
    PL{11} = ['Ryugu,1989 ML,Nereus,Didymos,',...
        '2011 UW158,Anteros,1992 TC'];
    PL{12} = ['Didymos',''];
    
    % Find body among list
    idx = find(contains(PL,body));
    
    % If no match found, error
    if isempty(idx)
        error('Body "%s" not found in any of the default databases',body);
    end
    
    % Select only first database if multiple objects found
    idx = idx(1);
    
    % Select database
    switch idx
        case 01, DB = @GetBodyKEP_Sun;
        case 02, DB = @GetBodyKEP_SSDG;
        case 03, DB = @GetBodyKEP_Dwarf_Planets;
        case 04, DB = @GetBodyKEP_Moons_Earth;
        case 05, DB = @GetBodyKEP_Moons_Mars;
        case 06, DB = @GetBodyKEP_Moons_Jupiter;
        case 07, DB = @GetBodyKEP_Moons_Saturn;
        case 08, DB = @GetBodyKEP_Moons_Uranus;
        case 09, DB = @GetBodyKEP_Moons_Neptune;
        case 10, DB = @GetBodyKEP_Moons_Pluto;
        case 11, DB = @GetBodyKEP_Asteroids_Mining;
        case 12, DB = @GetBodyKEP_SBD;
        otherwise, error('Database %d not implemented',idx);
    end

end

% Query database and return orbital elements propagated up to time JD2K
[ sma, ecc, inc, nu, argp, raan ] = DB ( body, jd2k );

end

