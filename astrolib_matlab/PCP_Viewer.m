function [  ] = PCP_Viewer ( data_file )
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

% PCP_Viewer options
contour_res = 64; % Contourplot resolution
max_days_to_years = 2*365.25; % Number of days to change axis to years

% Load data_file filepath
if ~exist('data_file','var') || isempty(data_file)
    data_file = uigetpath();
end

% Exit on data_file cancel
if isnumeric(data_file)
    close(fh); % Close figure
    return; % Return
end

% Error on data_file not found
if ~exist(data_file,'file')
    error(['Datafile "',data_file,'" does not exist.']);
end

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

% Get DataFile
raw = load(data_file);
departure_planet = raw.departure_planet;
arrival_planet = raw.arrival_planet;
departure_dates = raw.departure_dates;
jd2k0 = raw.jd2k0;
cal0 = raw.cal0;
tofs = raw.tofs;
dvd = raw.dvd;
dva = raw.dva;
dvt = raw.dvt;
theta = raw.theta;
clearvars raw;

% Hack
dvt(dvt>15)=15;

% Set x-axis magnitude
if max(tofs) > max_days_to_years % Years
    xlabelm = 'years';
    xtofs = tofs / 365.25;
else % Days
    xlabelm = 'days';
    xtofs = tofs;
end

% Set y-axis magnitude
departure_dates_span = max(departure_dates)-min(departure_dates);
if departure_dates_span > max_days_to_years % Years
    ylabelm = 'years';
    dates0 = departure_dates - jd2k0;
    ydates = dates0 / 365.25;
else % Days
    ylabelm = 'days';
    dates0 = departure_dates - jd2k0;
    ydates = dates0;
end

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
contourf(xtofs,ydates,dvt,contour_res,'LineStyle','none'); % Contourf
min_dvt = min(min(dvt)); % Minimum DeltaV
[ix,iy] = find(dvt == min_dvt); % Minimum DeltaV location
plot3(xtofs(iy),ydates(ix),min_dvt,'y*'); % Plot minimum DeltaV marker
hmkr = plot3(xtofs(iy),ydates(ix),dvt(ix,iy),'rx'); % Plot marker
colorbar('EastOutside'); % Colorbar
caxis([0,min([15,max(max(dvt))])]); % Color axis
xlabel(['Time of Flight [',xlabelm,']']); % Label X
ylabel(['Departure date [',ylabelm,' from ',sprintf('%02d',cal0{3}),'/',...
    sprintf('%02d',cal0{2}),'/',sprintf('%04d',cal0{1}),']']); % Label Y
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
if theta(ix,iy)>pi, otype = 'II'; else, otype = 'I'; end % Orbit type
title({['Orbital trajectory | Type ',otype,' transfer'];... % Title
    ['Departure day ',sprintf('%.0f',dates0(ix)),...
    ' | TOF = ',sprintf('%.0f',tofs(iy)),' days',' | ',...
    '\theta = ',sprintf('%.0f deg',round(theta(ix,iy)*180/pi))];...
    ['\DeltaVd = ',sprintf('%.1f',dvd(ix,iy)),' km/s',...
    ' | \DeltaVa = ',sprintf('%.1f',dva(ix,iy)),' km/s',...
    ' | \DeltaVt = ',sprintf('%.1f',dvt(ix,iy)),' km/s']});

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

% ----- Help functions -----

    function mouseclick_callback(~,~)
    % Action on MouseClick

    % Get the point that was clicked on
    cpoint = get(gca,'Currentpoint'); % MouseClick coordinates
    
    % Ensure coordinates are within range
    if cpoint(1,2)<ydates(1) || cpoint(1,2)>ydates(end), return; end
    if cpoint(1,1)<xtofs(1) || cpoint(1,1)>xtofs(end), return; end
    
    % Get the data indices corresponding to the clicked point
    ix = find(ydates>=cpoint(1,2),1);
    iy = find(xtofs>=cpoint(1,1),1);

    % Plot data
    plot_data(ix,iy);

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

    end

    function plot_data(i,j)
    % Plot data

    % Figure name (info)
    fh.Name = 'Lambert''s Problem | Computing...';
    
    % Plot current PCP position marker
    axes(h1); % Select PCP subplot
    delete(hmkr); % Delete old marker
    hmkr = plot3(xtofs(j),ydates(i),dvt(i,j),'rx'); % Plot marker

    % Replot data
    axes(h2); % Select orbital transfer subplot
    delete(htrj); delete(hp1); delete(hp2); % Delete old transfer
    trj = computeTrajectory(i,j); % Ease of coding
    htrj = plot3(trj(:,1),trj(:,2),trj(:,3),'k-','LineWidth',3); % Traj
    hp1 = plot3(trj(1,1),trj(1,2),trj(1,3),'bo','LineWidth',3); % P1
    hp2 = plot3(trj(end,1),trj(end,2),trj(end,3),'ro','LineWidth',3); % P2
    if theta(i,j)>pi, otype = 'II'; else, otype = 'I'; end % Orbit type
    title({['Orbital trajectory | Type ',otype,' transfer'];... % Title
        ['Departure day ',sprintf('%.0f',dates0(ix)),...
        ' | TOF = ',sprintf('%.0f',tofs(iy)),' days',' | ',...
        '\theta = ',sprintf('%.0f deg',round(theta(i,j)*180/pi))];...
        ['\DeltaVd = ',sprintf('%.1f',dvd(i,j)),' km/s',...
        ' | \DeltaVa = ',sprintf('%.1f',dva(i,j)),' km/s',...
        ' | \DeltaVt = ',sprintf('%.1f',dvt(i,j)),' km/s']});
    
    % Figure name (info)
    fh.Name = 'Lambert''s Problem | Pork-chop plot';
    
    end

    function trj = computeTrajectory ( i, j )
        
        % Current iteration values
        tof = tofs(j); % Time of flight [days]
        departure_date = departure_dates(i); % Departure date [JD2K days]
        arrival_date = departure_date + tof; % Arrival date [JD2K days]
        
        % State vector of departure/arrival planets [km] [km/s]
        [r1,~] = GetBodyICF(departure_planet,departure_date);
        [r2,~] = GetBodyICF(arrival_planet,arrival_date);
        
        % Default long-way (Type II)
        if theta(i,j) > pi, lw = 1; else, lw = 0; end

        % Solve Lambert problem
        [vsd,vsa] = Lambert(r1,r2,tof*days2secs,mu,lw,0,0);
        
        % Compute trajectory
        trj = ICF2Arc(r1,vsd,r2,vsa,mu,100);
        trj = trj / au; % normalize units
        
    end

end

