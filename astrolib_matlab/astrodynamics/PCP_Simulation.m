function [ dbname ] = PCP_Simulation ( ...
    departure_planet, arrival_planet, cal0, ...
    departure_dates, tofs, mr, lp, opts )
%PCP_SIMULATION Pork-chop plot simulation
%   Simulates a Pork-chop Plot via Lambert arcs and post-processes the
%   results (saving data files and plotting results)
%
% Inputs:
%   departure_planet: departure planet [string]
%   arrival_planet: arrival planet [string]
%   cal0: Initial calendar date cell array {Y,M,D,h,m,s}
%   departure_dates: departure date array, starts from cal0 [days]
%   tof_bounds: time of flight array [days]
%   opts: simulation options
%       opts.mano: type of transfer manoeuvre. Default '' (none)
%                  '': No manoeuvre
%                  'BPM': 3D broken plane manoeuvre at 50% theta
%                  'BPM2D': 2D broken plane manoeuvre at 50% theta
%       opts.maxdv: Maximum value for DeltaV in plots. Default Inf
%       opts.odir: output directory. Default 'output/PCP/'
%       opts.suffix: optional filename suffix. Default '' (empty)
%       opts.overwrite_sim: overwrite simulation. Default 0
%       opts.plot_results: plot results. Default 1
%       opts.info_level: see PCP_Lambert. Default 10
%
% Outputs:
%   dbname: path to the mat file with the resuts
%
% Example:
%   PCP_Simulation('Earth','Mars',{2030,1,1,0,0,0},0:5:300,50:5:600);
%
% References:
%   [-]
%	
% See also:
%   PCP_Grid, Lambert
%
%David de la Torre Sangra
%UPC-ETSEIAT 2014

% Default inputs
if nargin < 6 || isempty(opts), opts.placeholder = []; end
if ~isfield(opts,'mano'), opts.mano = ''; end
if ~isfield(opts,'maxdv'), opts.maxdv = Inf; end
if ~isfield(opts,'odir'), opts.odir = fullfile('output','PCP'); end
if ~isfield(opts,'suffix'), opts.suffix = ''; end
if ~isfield(opts,'overwrite_sim'), opts.overwrite_sim = 0; end
if ~isfield(opts,'plot_results'), opts.plot_results = 1; end
if ~isfield(opts,'info_level'), opts.info_level = 10; end

% Dates
jd2k0 = Cal2JD(cal0{:},'J2000'); % Days from J2000 [days]
departure_dates = departure_dates + jd2k0; % Departure Dates [days]

% Create output dir
if ~exist(opts.odir,'dir'), mkdir(opts.odir); end

% Results file name (without extension)
fname = fullfile(opts.odir,...
    ['PCP_',departure_planet,'2',arrival_planet,opts.suffix]);

% Results mat filename
dbname = [fname,'.mat'];

% Simulate if required
if ~exist(dbname,'file') || opts.overwrite_sim

    % Info
    if opts.info_level > 0, disp('Computing PCP...'); end
    
    % Compute Pork-Chop-Plot
    switch opts.mano
        case '' % No manoeuvre
            [c3d,c3a,dvd,dva,dvt,theta] = PCP_Grid( ...
                departure_planet,arrival_planet,...
                departure_dates,tofs,mr,lp); %#ok
        case 'BPM' % Broken pane manoeuvre (3D, full range)
            [c3d,c3a,c3bpm,dvd,dva,dvbpm,dvt,theta] = PCP_Grid_BPM( ...
                departure_planet,arrival_planet,...
                departure_dates,tofs,mr,lp); %#ok
        case 'BPMA' % Broken pane manoeuvre (3D, automatic range)
            [c3d,c3a,c3bpm,dvd,dva,dvbpm,dvt,theta] = PCP_Grid_BPMA( ...
                departure_planet,arrival_planet,...
                departure_dates,tofs,mr,lp); %#ok
        case 'BPM2D' % Broken pane manoeuvre (2D, full range)
            [c3d,c3a,c3bpm,dvd,dva,dvbpm,dvt,theta] = PCP_Grid_BPM2D( ...
                departure_planet,arrival_planet,...
                departure_dates,tofs,mr,lp); %#ok
        case 'GLS' % Broken pane manoeuvre (2D, full range)
            [c3d,c3a,dvd,dva,dvt,theta] = PCP_Grid_GLS( ...
                departure_planet,arrival_planet,...
                departure_dates,tofs,mr,lp); %#ok
        otherwise % Manoeuvre not implemented
            error('Manoeuvre "%s" not implemented',opts.mano);
    end

    % Save results
    save(dbname);
    
else % Load variables
    [c3d,c3a,dvd,dva,dvt] = loadVar(dbname,...
        'c3d','c3a','dvd','dva','dvt');
    switch opts.mano
        case 'BPM'
            [dvbpm] = loadVar(dbname,'dvbpm');
        case 'BPMA'
            [dvbpm] = loadVar(dbname,'dvbpm');
        case 'BPM2D'
            [dvbpm] = loadVar(dbname,'dvbpm');
    end
end

% Plot PCPs if required
if opts.plot_results
    
    % Info
    disp('Plotting results...');
    
    % Departure dates, starting from 0
    dates0 = departure_dates - jd2k0;
    
    % String for ylabel (Departure date)
    if dates0(end) > 365
        lbl_y = sprintf('Departure Date [years from %02.0f/%02.0f/%4.0f]',...
            cal0{3},cal0{2},cal0{1});
        dates0 = dates0 / 365.25;
    else
        lbl_y = sprintf('Departure Date [days from %02.0f/%02.0f/%4.0f]',...
            cal0{3},cal0{2},cal0{1});
    end
        
    % Departure C3 plot
    Plot_PCP_C3(tofs,dates0,c3d,...
        departure_planet,arrival_planet,...
        'Departure',[fname,'_Departure_C3'],...
        [],lbl_y,opts.maxdv);
    
    % Arrival C3 plot
    Plot_PCP_C3(tofs,dates0,c3a,...
        departure_planet,arrival_planet,...
        'Departure',[fname,'_Arrival_C3'],...
        [],lbl_y,opts.maxdv);
    
    % Departure DeltaV plot
    Plot_PCP_DeltaV(tofs,dates0,dvd,...
        departure_planet,arrival_planet,...
        'Departure',[fname,'_Departure'],...
        [],lbl_y,opts.maxdv);
    
    % Arrival DeltaV plot
    Plot_PCP_DeltaV(tofs,dates0,dva,...
        departure_planet,arrival_planet,...
        'Arrival',[fname,'_Arrival'],...
        [],lbl_y,opts.maxdv);
    
    % Total DeltaV plot
    Plot_PCP_DeltaV(tofs,dates0,dvt,...
        departure_planet,arrival_planet,...
        'Total',[fname,'_Total'],[],...
        lbl_y,opts.maxdv);
    
    % BPM DeltaV plot
    switch opts.mano
        case 'BPM'
            Plot_PCP_DeltaV(tofs,dates0,dvbpm,...
                departure_planet,arrival_planet,...
                'BPM',[fname,'_BPM'],...
                [],lbl_y,opts.maxdv);
        case 'BPM2D'
            Plot_PCP_DeltaV(tofs,dates0,dvbpm,...
                departure_planet,arrival_planet,...
                'BPM',[fname,'_BPM'],...
                [],lbl_y,opts.maxdv);
    end
    
end

end

