% function [selected_departure_date, selected_tof] = PCP_Viewer ( a_mat_file_str  )
function [selected_trajectory] = PCP_Viewer ( a_mat_file_str  )
%PCP_VIEWER shows a PCP + transfer orbit plot in an interactive way.
%   This function requires the output mat file from a PCP_Simulation
%
% Inputs:
%   data_file: filepath to the PCP DATA file.
%
% Example:
%   ofile = PCP_Simulation('Earth','Mars',{2020,1,1,0,0,0},50:200,50:300);
%   PCP_Viewer(ofile);
%
% References:
%	
%
% See also:
%   PCP_Simulation, PCP_Grid, Lambert
%
%David de la Torre Sangra
%June 2014

clc
close all
% Prepare the data.

raw =   load(a_mat_file_str);
% raw = load('/Users/jorialand/code/tfm/sonet/sonet_tfm_horia/data/PCP_Viewer_tmp.mat');
departure_planet = raw.departure_planet;
arrival_planet = raw.arrival_planet;
departure_dates = raw.departure_dates; % Departure dates, tabular form.
departure_dates = departure_dates - departure_dates(1); % Normalize the departure_dates.
% m_departure_dates = raw.m_departure_dates - raw.m_departure_dates(1); % The original departure_dates vector, before I filtered the max dvt values within Python. The prepended m stands for matrix.
cal0 = raw.cal0;
tofs = raw.tofs;
% m_tofs = raw.m_tofs; % The original tofs vector, before I filtered the max dvt values within Python. The prepended m stands for matrix.
dvd = raw.dvd;
dva = raw.dva;
dvt = raw.dvt;
theta = raw.theta * pi/180;

% m_dvt = convert_table_to_matrix(dvt);
% m_dvd = convert_table_to_matrix(dvd);
% m_dva = convert_table_to_matrix(dva);
% m_theta = convert_table_to_matrix(theta);
% clearvars raw dvt dvd dva theta;

% Convert data from tabular to matrix form.
m_departure_dates = unique(departure_dates);
m_tofs = unique(tofs);

% Matrix size.
m = length(m_departure_dates);
n = length(m_tofs);
m_dvt = nan(m,n);
m_dvd = nan(m,n);
m_dva = nan(m,n);
m_theta = nan(m,n);
% Traverse the table, and assign each Z(dvt/dvd/dva/theta) to the new (m,n)
% matrix.
for row = 1:length(departure_dates)
    % ix, iy are the matrix indices for the current row.
    ix = find( m_departure_dates == departure_dates(row),1); % Give me which position in the matrix would correspond to the row row.
    iy = find( m_tofs == tofs(row),1); % Idem.
    m_dvt(ix,iy) = dvt(row);
    m_dvd(ix,iy) = dvd(row);
    m_dva(ix,iy) = dva(row);
    m_theta(ix,iy) = theta(row);
end
% PCP_Viewer options
contour_res = 32; % Contourplot resolution
max_days_to_years = 2*365.25; % Number of days to change axis to years

% Create figure
fh = figure(); % Figure
fh.Name = 'Lambert''s Problem'; % Figure name
fh.Renderer = 'opengl'; % Renderer
fh.NumberTitle = 'off'; % No 'Fig:1'
fh.Position = GetFigCC(1200,500); % Figure Dimensions
fh.PaperPositionMode = 'auto'; % Paper Position

% Draw canvas
fh.Name = 'Lambert''s Problem | Initializing...'; % Figure name
drawnow;

% Constants
mu = 1.32712440018E11; % Gravitational parameter (GM) of Sun [km3/s2]
au = 1.49597871E8; % Astronomical unit [km]
days2secs = 24*60*60; % Days to seconds


% Set x-axis magnitude
if max(m_tofs) > max_days_to_years % Years
    xlabelm = 'years';
    xtofs = m_tofs / 365.25;
else % Days
    xlabelm = 'days';
    xtofs = m_tofs;
end

% Set y-axis magnitude
departure_dates_span = m_departure_dates(end);
if departure_dates_span > max_days_to_years % Years
    ylabelm = 'years';
    dates0 = double(m_departure_dates);
    ydates = dates0 / 365.25;
else % Days
    ylabelm = 'days';
    dates0 = m_departure_dates;
    ydates = dates0;
end

% Just another hack.
% contourf function asks ydates to be strictly monothonic. So let's do it!

% Get orbit of planets
[rp1,~] = GetBodyOrbit(departure_planet,departure_dates(1),mu,100);
[rp2,~] = GetBodyOrbit(arrival_planet,departure_dates(1),mu,100);

% Plot PCP
h1 = subplot(1,2,1);
hold on;
box on;
h1.Layer = 'top';
h1.FontSize = 14;
colormap(jet(contour_res)); % Colormap
contourf(xtofs,ydates,m_dvt,contour_res,'LineStyle','none'); % Contourf
min_dvt = min(min(m_dvt)); % Minimum DeltaV
[ix,iy] = find(m_dvt == min_dvt); % Minimum DeltaV location
plot3(xtofs(iy),ydates(ix),min_dvt,'y*'); % Plot minimum DeltaV marker
hmkr = plot3(xtofs(iy),ydates(ix),m_dvt(ix,iy),'rx'); % Plot marker
colorbar('EastOutside'); % Colorbar
caxis([0,min([15,max(max(dvt))])]); % Color axis
xlabel(['Time of Flight [',xlabelm,']']); % Label X
ylabel(['Departure date [',ylabelm,' from ',sprintf('%02d',cal0(3)),'/',...
    sprintf('%02d',cal0(2)),'/',sprintf('%04d',cal0(1)),']']); % Label Y
title([departure_planet,' to ',arrival_planet,' | Total \DeltaV [km/s]']);


% Plot Orbit
h2 = subplot(1,2,2);
hold on;
box on;
grid on;
axis equal;
view(0,90);
set(h2,'layer','top');
set(h2,'FontSize',14);
plot3(rp1(:,1)/au,rp1(:,2)/au,rp1(:,3)/au,'b-','LineWidth',0.5); % Orbit1
plot3(rp2(:,1)/au,rp2(:,2)/au,rp2(:,3)/au,'r-','LineWidth',0.5); % Orbit2
plot3(0,0,0,'yo','LineWidth',7); % Sun
htrj = plot3(0,0,0,'k-','LineWidth',2); % Trajectory
hp1 = plot3(0,0,0,'bo','LineWidth',2); % P1
hp2 = plot3(0,0,0,'ro','LineWidth',2); % P2
xlabel('AU'); ylabel('AU'); % Axis labels
if m_theta(ix,iy)>pi, otype = 'II'; else, otype = 'I'; end % Orbit type
title({['Orbital trajectory | Type ',otype,' transfer'];... % Title
    ['Departure day ',sprintf('%.0f',dates0(ix)),...
    ' | TOF = ',sprintf('%.0f',m_tofs(iy)),' days',' | ',...
    '\theta = ',sprintf('%.0f deg',round(m_theta(ix,iy)*180/pi))];...
    ['\DeltaVd = ',sprintf('%.1f',m_dvd(ix,iy)),' km/s',...
    ' | \DeltaVa = ',sprintf('%.1f',m_dva(ix,iy)),' km/s',...
    ' | \DeltaVt = ',sprintf('%.1f',m_dvt(ix,iy)),' km/s']});

% Draw canvas
drawnow;

% Attach the MouseClick EventFunction to the axes & children
h1.ButtonDownFcn = @mouseclick_callback; % Assign callback to axes
for i=1:length(h1.Children) % Assign callback to children
    h1.Children(i).ButtonDownFcn = @mouseclick_callback;
end

% Assign the KeyPress event to figure
fh.KeyPressFcn = @keypress_callback;

% Plot initial point (min dvt)
plot_data(ix,iy);

selected_trajectory = 0.;
disp('PCP_Viewer - Waiting till trajectory is chosen and PCP figure is closed.');
waitfor(fh);
disp('PCP_Viewer finished execution.');
disp(['Selected trajectory is: ', num2str(selected_trajectory)]);

% selected_trajectory = find( tofs == selected_tof,1);
% [ DISTANCE , selected_trajectory ] = min( abs( tofs-selected_tof));
% 'Selected trajectory index= '
% selected_trajectory = round(selected_trajectory)
STOP=1;
% Get the table's row corresponding to the selected trajectory.


% ----- Help functions -----

   function mouseclick_callback(~,~)
   % Action on MouseClick

   % Get the point that was clicked on
   cpoint = get(gca,'Currentpoint'); % MouseClick coordinates

   % Ensure coordinates are within range
   clicked_date = cpoint(1,2);
   clicked_tof = cpoint(1,1);
   min_date = ydates(1);
   max_date = ydates(end);
   min_tof = xtofs(1);
   max_tof = xtofs(end);

   if clicked_date<min_date || clicked_date>max_date, return; end
   if clicked_tof<min_tof || clicked_tof>max_tof, return; end

   % Get the data indices corresponding to the clicked point
   ix = find(ydates>=clicked_date,1);
   iy = find(xtofs>=clicked_tof,1);

   % Plot data
   plot_data(ix,iy);
   
   % Get the selected trajectory.
   the_departure_date = m_departure_dates(ix);
   the_departure_tof = m_tofs(iy);
   candidate_rows = find(departure_dates == the_departure_date);
   candidate_rows_tofs = tofs(candidate_rows);
   candidate_rows2 = find(candidate_rows_tofs == the_departure_tof);
   
   if (size(candidate_rows2) > 1) | (size(candidate_rows2) == [1,0])
        disp('Error in mouseclick_callback. More than one possible trajectory. Please, review.')
        return
   end
   
   selected_trajectory = candidate_rows(candidate_rows2);
   STOP = 1;
   end

   function keypress_callback(~,evt)
   % Action on KeyPress

   % Get current point
   ix_new = ix;
   iy_new = iy;

   % Move current point (tentatively)
   switch evt.Key
       case 'uparrow'
           ix_new = ix_new + 1;
       case 'downarrow'
           ix_new = ix_new - 1;
       case 'leftarrow'
           iy_new = iy_new - 1;
       case 'rightarrow'
           iy_new = iy_new + 1;
   end

   % Ensure new point coordinates are within range
   if ix_new < 1 || ix_new > length(ydates), return; end
   if iy_new < 1 || iy_new > length(xtofs), return; end

   % Update the new point coordinates
   ix = ix_new;
   iy = iy_new;

   % Plot data
   plot_data(ix,iy);
   
    cpoint = get(gca,'Currentpoint'); % MouseClick coordinates
    clicked_date = cpoint(1,2);
    clicked_tof = cpoint(1,1);
   end

   function plot_data(i,j)
   % Plot data

   % Figure name (info)
   fh.Name = 'Lambert''s Problem | Computing...';

   % Plot current PCP position marker
   axes(h1); % Select PCP subplot
   delete(hmkr); % Delete old marker
   hmkr = plot3(xtofs(j),ydates(i), m_dvt(i,j),'rx'); % Plot marker

   % Replot data
   axes(h2); % Select orbital transfer subplot
   delete(htrj); delete(hp1); delete(hp2); % Delete old transfer
   trj = computeTrajectory(i,j); % Ease of coding
   htrj = plot3(trj(:,1),trj(:,2),trj(:,3),'k-','LineWidth',3); % Traj
   hp1 = plot3(trj(1,1),trj(1,2),trj(1,3),'bo','LineWidth',3); % P1
   hp2 = plot3(trj(end,1),trj(end,2),trj(end,3),'ro','LineWidth',3); % P2
   if m_theta(i,j)>pi, otype = 'II'; else, otype = 'I'; end % Orbit type
   title({['Orbital trajectory | Type ',otype,' transfer'];... % Title
       ['Departure day ',sprintf('%.0f',dates0(ix)),...
       ' | TOF = ',sprintf('%.0f',m_tofs(iy)),' days',' | ',...
       '\theta = ',sprintf('%.0f deg',round(m_theta(i,j)*180/pi))];...
       ['\DeltaVd = ',sprintf('%.1f',m_dvd(i,j)),' km/s',...
       ' | \DeltaVa = ',sprintf('%.1f',m_dva(i,j)),' km/s',...
       ' | \DeltaVt = ',sprintf('%.1f',m_dvt(i,j)),' km/s']});

   % Figure name (info)
   fh.Name = 'Lambert''s Problem | Pork-chop plot';

   end

   function trj = computeTrajectory ( i, j )

       % Current iteration values
       tof = m_tofs(j); % Time of flight [days]
       departure_date = m_departure_dates(i); % Departure date [JD2K days]
       arrival_date = departure_date + tof; % Arrival date [JD2K days]

       % State vector of departure/arrival planets [km] [km/s]
       [r1,~] = GetBodyICF(departure_planet,departure_date);
       [r2,~] = GetBodyICF(arrival_planet,arrival_date);

       % Default long-way (Type II)
       if m_theta(i,j) > pi, lw = 1; else, lw = 0; end

       % Solve Lambert problem
       [vsd,vsa] = Lambert(r1,r2,tof*days2secs,mu,lw,0,0);

       % Compute trajectory
       trj = ICF2Arc(r1,vsd,r2,vsa,mu,100);
       trj = trj / au; % normalize units

   end

end

