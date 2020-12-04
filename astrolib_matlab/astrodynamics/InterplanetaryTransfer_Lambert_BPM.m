function [ c3d, c3a, c3bpm, dvd, dva, dvbpm, dvt, theta ] = ...
    InterplanetaryTransfer_Lambert_BPM ( ...
    departure_planet, arrival_planet, departure_date, tof, mr, lp )
%PCP_GRID Pork-chop plot
%   Returns the results from a Pork-chop Plot via Lambert arcs + BPM
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
%   [c3d,c3a,dvd,dva,dvt,trj,theta] = PCP_Grid_BPM(...
%       'Earth','Mars',7300:50:7500,100:5:600);
%
% References:
%	[-]
%
% See also:
%   PCP_Simulation, PCP_Grid, PCP_Grid_BPM2D
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
[r1,v1] = GetBodyICF(departure_planet,departure_date,mu);

% State vector of arrival planet [km] [km/s]
[r2,v2] = GetBodyICF(arrival_planet,arrival_date,mu);

% Intersect arrival planet position with departure planet's orbital plane
h1 = cross3(r1,v1); % Specific angular momentum of P1
z2_inc1 = -(r2(1)*h1(1) + r2(2)*h1(2)) / h1(3); % Plane eq: ax+by+cz=0
r2_inc1 = [r2(1:2),z2_inc1]; % Projection of P2 onto P1's orbital plane

% Transfer angle from P1 to P2_inc1
theta_inc1 = DeltaNu3(r1,r2_inc1,1); % Angle between planets
if theta_inc1 > pi, lw = 1; else, lw = 0; end % Long-way

% Solve Lambert problem between P1 and P2_inc1
[vsd,~] = Lambert(r1,r2_inc1,tof*days2secs,mu,lw,0,lp);

% Get orbital elements of initial state
[sma,ecc,inc,nu_bpm1,argp,raan] = ICF2KEP_O(r1,vsd,mu);

% BPM location
nu_bpm2 = nu_bpm1 + alpha * theta_inc1;

% Get position and velocity at bpm arrival
[rsa_bpm,vsa_bpm] = KEP2ICF_O(sma,ecc,inc,nu_bpm2,argp,raan,mu);

% Transfer angle of P1-BPM
theta_bpm1 = DeltaNu3(r1,rsa_bpm,1); % Transfer angle
if theta_bpm1 > pi, lw = 1; else, lw = 0; end % Long-way

% Compute time of flight of the P1-BPM transfer
c = norm3(rsa_bpm - r1); % Length of chord P1_PBPM
s = 0.5 * (norm3(r1) + norm3(rsa_bpm) + c); % Semiperimeter
am = s/2; % Minimum-energy ellipse sma
x = sqrt(1 - am/sma); % Lambert universal parameter x
[tof1,~] = Lambert_Izzo_2015_X_EQ(x,r1,rsa_bpm,mu,lw,0);

% Compute time of flight of the BPM-P2 transfer
tof2 = tof - tof1/days2secs;

% Transfer angle of BPM-P2
theta_bpm2 = DeltaNu3(rsa_bpm,r2,1); % Transfer angle
if theta_bpm2 > pi, lw = 1; else, lw = 0; end % Long-way

% Solve Lambert problem between BPM and P2
[vsd_bpm,vsa] = Lambert(rsa_bpm,r2,tof2*days2secs,mu,lw,mr,lp);

% Calculate DeltaV [km/s]
% Keplerian 2BP point-mass model: Vinf ~ DeltaV_heliocentric
dvd = vsd - v1; % DeltaV at departure
dva = vsa - v2; % DeltaV at arrival
dvbpm = vsd_bpm - vsa_bpm; % DeltaV at BPM

% Case of alpha=0: full 3D Lambert transfer
if alpha==0
    dvd = vsd_bpm - v1;
    dvbpm = 0;
end

% Case of alpha=1: full 3D Lambert transfer
if alpha==1
    dva = vsd_bpm - v2;
    dvbpm = 0;
end

% Total DeltaV
dvt = norm(dvd) + norm(dva) + norm(dvbpm);

% Calculate C3 ( C3 = |Vsc-Vp|^2 ) [km/s]
c3d = norm(dvd)^2; % C3 departure
c3a = norm(dva)^2; % C3 arrival
c3bpm = norm(dvbpm)^2; % C3 BPM

% Transfer angle
theta = theta_bpm1;

end

