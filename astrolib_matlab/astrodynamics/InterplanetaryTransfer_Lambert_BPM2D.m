function [ c3d, c3a, c3bpm, dvd, dva, dvbpm, dvt, theta ] = ...
    InterplanetaryTransfer_Lambert_BPM2D ( ...
    departure_planet, arrival_planet, departure_date, tof, mr, lp )
%PCP_GRID Pork-chop plot
%   Returns the results from a Pork-chop Plot via Lambert arcs + 2D BPM
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
%   [c3d,c3a,dvd,dva,dvt,trj,theta] = PCP_Grid_BPM2D(...
%       'Earth','Mars',7300:50:7500,100:5:600);
%
% References:
%	[-]
%
% See also:
%   PCP_Simulation, PCP_Grid, PCP_Grid_BPM
%
%David de la Torre Sangra
%UPC-ETSEIAT 2016

% Constants
mu = GetBodyProps('Sun'); % Standard gravitational parameter [km3/s2]
days2secs = 24*60*60; % Days to seconds
alpha = 0.5; % Broken plane manoeuvre location

% Arrival date [JD2K days]
arrival_date = departure_date + tof;

% State vector of departure planet [km] [km/s]
[sma1,ecc1,inc1,nu1,argp1,raan1] = GetBodyKEP(...
    departure_planet,departure_date);
[r1,v1] = KEP2ICF_O(sma1,ecc1,inc1,nu1,argp1,raan1,mu);

% State vector of arrival planet [km] [km/s]
[sma2,ecc2,inc2,nu2,argp2,raan2] = GetBodyKEP(...
    arrival_planet,arrival_date);
[r2_2d,~] = KEP2ICF_O(sma2,ecc2,inc1,nu2,argp2,raan2,mu);
[r2_3d,v2_3d] = KEP2ICF_O(sma2,ecc2,inc2,nu2,argp2,raan2,mu);

% Transfer angle
theta = DeltaNu3(r1,r2_2d,1); % Angle between planets
if theta > pi, lw = 1; else, lw = 0; end % Long-way

% Solve Lambert problem between P1 and P2_2d
[vsd_2d,~] = Lambert(r1,r2_2d,tof*days2secs,mu,lw,0,lp);

% Get orbital elements of initial state
[sma,ecc,inc,nu_bpm1,argp,raan] = ICF2KEP_O(r1,vsd_2d,mu);

% BPM location
nu_bpm2 = nu_bpm1 + alpha * theta;

% Get position and velocity at bpm arrival
[rsa_bpm,vsa_bpm] = KEP2ICF_O(sma,ecc,inc,nu_bpm2,argp,raan,mu);

% Transfer angle of P1-BPM
theta_2d_bpm = DeltaNu3(r1,rsa_bpm,1); % Transfer angle
if theta_2d_bpm > pi, lw = 1; else, lw = 0; end % Long-way

% Time of flight of the BPM-P2 transfer
c = norm3(rsa_bpm - r1); % Length of chord P1_PBPM
s = 0.5 * (norm3(r1) + norm3(rsa_bpm) + c); % Semiperimeter
am = s/2; % Minimum-energy ellipse sma
x = sqrt(1 - am/sma); % Lambert universal parameter x
[tof_2d,~] = Lambert_Izzo_2015_X_EQ(x,r1,rsa_bpm,mu,lw,0);
tof_bpm = tof - tof_2d/days2secs;

% Transfer angle of BPM-P2
theta_bpm = DeltaNu3(rsa_bpm,r2_3d,1); % Transfer angle
if theta_bpm > pi, lw = 1; else, lw = 0; end % Long-way

% Solve Lambert problem between BPM and P2
[vsd_bpm,vsa_3d] = Lambert(rsa_bpm,r2_3d,tof_bpm*days2secs,mu,lw,mr,lp);

% Calculate DeltaV [km/s]
% Keplerian 2BP point-mass model: Vinf ~ DeltaV_heliocentric
dvd = vsd_2d - v1; % DeltaV at departure
dva = vsa_3d - v2_3d; % DeltaV at arrival
dvbpm = vsd_bpm - vsa_bpm; % DeltaV at BPM

% Total DeltaV
dvt = dvd + dva + dvbpm;

% Calculate C3 ( C3 = |Vsc-Vp|^2 ) [km/s]
c3d = norm(dvd)^2; % C3 departure
c3a = norm(dva)^2; % C3 arrival
c3bpm = norm(dvbpm)^2; % C3 BPM

end

