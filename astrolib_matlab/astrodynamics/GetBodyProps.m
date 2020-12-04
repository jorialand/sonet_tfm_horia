function [ mu, vmr, rsoi, sper, j2, mass, ash ] = GetBodyProps ( body )
%GETBODYPROPS Get body properties
%   Returns several properties of many Solar System's bodies
%
% Inputs:
%   body: name of the target object [string]
%
% Outputs:
%   mu: Standard gravitational parameter of the body [km^3 s^-2]
%   vmr: Body's volumetric mean radius [km]
%   rsoi: Sphere of influence radius (Tisserand) using sma [km]
%   sper: Sidereal Period [seconds]
%   j2: Zonal Harmonic Coefficients 
%   mass: Body's mass [kg]
%   ash: Atmosphere scale height [km]. H=0 if no atmosphere
%
% Example:
%   [ mu, vmr, rsoi, sp, j2, mass, ash ] = GetBodyProps ( 'Makemake' );
%
% References:
%	[1] https://nssdc.gsfc.nasa.gov/planetary/planetfact.html
%   [2] https://nssdc.gsfc.nasa.gov/planetary/factsheet/galileanfact_table.html
%   [3] https://nssdc.gsfc.nasa.gov/planetary/factsheet/asteroidfact.html
%
%David de la Torre Sangra
%August 2014

%% Default (Unknown) Planet
mu = NaN;
vmr = 0;
rsoi = 0;
sper = 0;
j2 = 0;
mass = 0;
ash = 0;

%% Sun
if strcmpi(body,'Sun')
    mu = 1.32712440018E11;
    mass = 1.988544E30;
    vmr = 6.96342E5;
    rsoi = 1.1967829656E11;
    return;
end

%% Planets

if strcmpi(body,'Mercury')
    mu = 0.022032E6;
    mass = 0.33011E24;
    vmr = 2.4397E3;
    rsoi = 1.1218802638128363E5;
    j2 = 50.3E-6;
    sper = 1407.6 * 3600;
    return;
end

if strcmpi(body,'Venus')
    mu = 3.24859E5;
    mass = 4.867E24;
    vmr = 6.0518E3;
    rsoi = 6.1623991733995883E5;
    ash = 15.9;
    j2 = 0.000027;
    return;
end

if strcmpi(body,'Earth')
    mu = 3.986004418E5;
    mass = 5.97219E24;
    vmr = 6.3781366E3;
    rsoi = 9.2462559147537535E5;
    ash = 8.5;
    j2 = 0.0010826269;
    sper = 23.9345 * 24*3600;
    return;
end

if strcmpi(body,'Moon')
    mu = 4.9028E3;
    mass = 0.07346E24;
    vmr = 1737.4;
    rsoi = 6.6189540975262644E4;
    j2 = 0.0002027;
    sper = 655.728 * 3600;
    return;
end

if strcmpi(body,'Mars')
    mu = 4.2828E4;
    mass = 6.39E23;
    vmr = 3.3895E3;
    rsoi = 5.7624224061266356E5;
    ash = 11.1;
    j2 = 0.001964;
    return;
end

if strcmpi(body,'Jupiter')
    mu = 1.26686534E8;
    mass = 1.89813E27;
    vmr = 6.9911E4;
    rsoi = 4.821711777624438E7;
    ash = 27;
    j2 = 0.01475;
    return;
end

if strcmpi(body,'Saturn')
    mu = 3.7931187E7;
    mass = 5.683E26;
    vmr = 5.8232E4;
    rsoi = 5.4802369749626689E7;
    ash = 59.5;
    j2 = 0.01645;
    return;
end

if strcmpi(body,'Uranus')
    mu = 5.793939E6;
    mass = 8.681E25;
    vmr = 2.5362E4;
    rsoi = 5.1760361762205213E7;
    ash = 27.7;
    j2 = 0.012;
    return;
end

if strcmpi(body,'Neptune')
    mu = 6.836529E6;
    mass = 1.024E26;
    vmr = 2.4622E4;
    rsoi = 8.6651829830722004E7;
    ash = 20;
    j2 = 0.004;
    return;
end

%% Dwarf Planets

if strcmpi(body,'Ceres')
    mu = 6.29161113E1;
    mass = 9.43E20;
    vmr = 4.762E2;
    rsoi = 7.714299823636092E4;
    return;
end

if strcmpi(body,'Pluto')
    mu = 8.71E2;
    mass = 1.305E22;
    vmr = 1.184E3;
    rsoi = 3.1315839956073486E6;
    return;
end

if strcmpi(body,'Haumea')
    mu = 2.672767146E2;
    mass = 4.006E21;
    vmr = 6.50E2;
    rsoi = 2.144841996213831E6;
    return;
end

if strcmpi(body,'Makemake')
    mu = 0.283556175;
    mass = 4.25E18;
    vmr = 7.15E2;
    rsoi = 1.471116376188730E5;
    return;
end

if strcmpi(body,'Eris')
    mu = 1.108E3;
    mass = 1.67E22;
    vmr = 1.163E3;
    rsoi = 5.9816722296488713E6;
    return;
end

if strcmpi(body,'Sedna')
    vmr = 9.95E2;
    return;
end

%% Jupiter Moons

if strcmpi(body,'Io')
    mu = 5.9592832929E3;
    mass = 8.9319E22;
    vmr = 3.66E3;
    return;
end

if strcmpi(body,'Europa')
    mu = 3.2025168E3;
    mass = 4.8E22;
    vmr = 3.121E3;
    return;
end

if strcmpi(body,'Ganymede')
    mu = 9.887103429E3;
    mass = 1.4819E23;
    vmr = 5.262E3;
    return;
end

if strcmpi(body,'Callisto')
    mu = 7.178307969E3;
    mass = 1.0759E23;
    vmr = 4.82E3;
    return;
end

%% Saturn Moons

if strcmpi(body,'Mimas')
    mu = 2.668764;
    mass = 4.0E19;
    vmr = 3.96E2;
    return;
end

if strcmpi(body,'Enceladus')
    mu = 7.339101;
    mass = 1.1E20;
    vmr = 5.04E2;
    return;
end

if strcmpi(body,'Tethys')
    mu = 4.1365842E1;
    mass = 6.2E20;
    vmr = 1.062E3;
    return;
end

if strcmpi(body,'Dione')
    mu = 7.339101E1;
    mass = 1.1E21;
    vmr = 1.123E3;
    return;
end

if strcmpi(body,'Rhea')
    mu = 1.5345393E2;
    mass = 2.3E21;
    vmr = 1.527E3;
    return;
end

if strcmpi(body,'Titan')
    mu = 9.0070785E3;
    mass = 1.35E23;
    vmr = 5.15E3;
    return;
end

if strcmpi(body,'Iapetus')
    mu = 1.2009438E2;
    mass = 1.8E21;
    vmr = 1.47E3;
    return;
end

%% Neptune Moons

if strcmpi(body,'Triton')
    mu = 1427.6;
    mass = 2.14E22;
    vmr = 1353.4;
    return;
end

end

