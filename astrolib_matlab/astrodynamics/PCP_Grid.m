function [ c3d, c3a, dvd, dva, dvt, theta ] = PCP_Grid ( ...
    departure_planet, arrival_planet, departure_dates, tofs, mr, lp )
%PCP_GRID Pork-chop plot
%   Returns the results from a Pork-chop plot grid simulation via Lambert
%   arcs
%
% Inputs:
%   departure_planet: Departure planet [string]
%   arrival_planet: Arrival planet [string]
%   departure_dates: Departure Julian day array (J2000 reference) [days]
%   tofs: Time of flight array [days]
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
%       'Earth','Mars',7300:50:7500,100:5:600);
%
% References:
%	[]
%
% See also:
%   PCP_Simulation, PCP_Grid_BPM, PCP_Grid_BPM2D
%
%David de la Torre Sangra
%UPC-ETSEIAT 2014

% Preallocate variables
ndd = length(departure_dates); % Length of departure dates array
ntf = length(tofs); % Length of tof array
c3d = zeros(ndd,ntf); % C3 departure velocity
c3a = zeros(ndd,ntf); % C3 arrival velocity
theta = zeros(ndd,ntf); % Transfer angle

% Iterate on departure date
for i=1:ndd
    
    % Iterate on time of flight
    for j=1:ntf
        
        % Info
        fprintf('  %d/%d %d/%d (%.1f%%)\n',i,ndd,j,ntf,...
            ((i-1)*ntf+j)/(ndd*ntf)*100);
        
        % Current iteration values
        tof = tofs(j); % Time of flight [days]
        departure_date = departure_dates(i); % Departure date [JD2K days]
        
        % Compute interplanetary transfer via Lambert arc
        [ c3d(i,j), c3a(i,j), ~, ~, ~, theta(i,j) ] = ...
            InterplanetaryTransfer_Lambert ( ...
            departure_planet, arrival_planet, ...
            departure_date, tof, mr, lp );

    end
    
end

% Calculate DeltaV values
dvd = sqrt(c3d); % Departure DeltaV
dva = sqrt(c3a); % Arrival DeltaV
dvt = dvd + dva; % Total DeltaV

end

