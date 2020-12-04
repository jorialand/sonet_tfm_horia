function [ c3d, c3a, dvd, dva, dvt, theta ] = ...
    InterplanetaryTransfer_Lambert ( ...
    departure_planet, arrival_planet, departure_date, tof, mr, lp )
%PCP_GRID Pork-chop plot
%   Returns the results from a Pork-chop Plot via Lambert arcs
%
% Inputs:
%   departure_planet: Departure planet [string]
%   arrival_planet: Arrival planet [string]
%   departure_date: Departure Julian day (J2000 reference) [days]
%   tof: Time of flight [days]
%
% Outputs:
%   c3d: C3 at departure [km2/s2]
%   c3a: C3 at arrival [km2/s2]
%   dvd: DeltaV at depature [km/s]
%   dva: DeltaV at arrival [km/s]
%   dvt: Total DeltaV of the mission [km/s]
%   theta: Transfer angle [rad]
%
% Example:
%   [c3d,c3a,dvd,dva,dvt,trj,theta] = PCP_Grid(...
%       'Earth','Mars',7300,600);
%
% References:
%	[-]
%
% See also:
%   PCP_Simulation, PCP_Grid, PCP_Grid_BPM, PCP_Grid_BPM2D
%
%David de la Torre Sangra
%UPC-ETSEIAT 2016

% Constants
mu = GetBodyProps('Sun'); % Standard gravitational parameter [km3/s2]
days2secs = 24*60*60; % Days to seconds

% Arrival date [JD2K days]
arrival_date = departure_date + tof;

% State vector of departure/arrival planets [km] [km/s]
[r1,v1] = GetBodyICF(departure_planet,departure_date);
[r2,v2] = GetBodyICF(arrival_planet,arrival_date);

% Transfer angle betweer P1 and P2 (counter-clockwise)
theta = DeltaNu3(r1,r2,1);

% Select long-way transfer (Type II) if required
if theta > pi, lw = 1; else, lw = 0; end

% Solve Lambert problem between P1 and P2
[vsd,vsa] = Lambert(r1,r2,tof*days2secs,mu,lw,mr,lp);

% Calculate DeltaV [km/s]
dvd = vsd - v1; % DeltaV at departure (vector)
dva = vsa - v2; % DeltaV at arrival (vector)
dvt = norm(dvd) + norm(dva); % Total DeltaV (norm)

% Calculate C3 ( C3 = Vinf^2 ~ |Vsc-Vp|^2 ) [km/s]
% Keplerian 2BP point-mass model: Vinf ~ DeltaV_heliocentric
c3d = norm(dvd)^2; % C3 departure
c3a = norm(dva)^2; % C3 arrival

end

