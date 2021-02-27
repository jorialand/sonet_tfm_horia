% PCP Pork-chop plot
% Execution script
% David de la Torre Sangra
% (C) UPC-ETSEIAT 2016

% Para ver las dependencias del script. También se puede llamar al Matlab
% Dependencies Report desde la carpeta, con clic dcho
% [fList,pList] = matlab.codetools.requiredFilesAndProducts('PCP_Planet2Planet.m');

% Clean environment
close all; clear; clc;

% Ask for inputs
prompts = {'Departure Planet:', ...
           'Arrival Planet:', ...
           'Departure year:', ...
           'Synodic periods:', ...
           'TOF years:', ...
           'Manoeuvre: (n/a) BPM BPMA BPM2D', ...
           'Multi-revs:', ...
           'Long-Period:'};
       
defaultans = {'Earth','Mars','2020','1','2','','0','0'};
answer = inputdlg(prompts,'PCP',1,defaultans);
if isempty(answer), return; end

% Parse inputs
departure_planet = answer{1};
arrival_planet = answer{2};
Y0 = str2double(answer{3});
PsN = str2double(answer{4});
tofY = str2double(answer{5});
opts.mano = answer{6};
mr = str2double(answer{7});
lp = str2double(answer{8});
clearvars answer;

% Compute synodic period between the planets
mu = GetBodyProps('Sun');
sma1 = GetBodyKEP ( departure_planet, 0 );
sma2 = GetBodyKEP ( arrival_planet, 0 );
Ps = Synodic_Period ( sma1, sma2, mu );
Ps = Ps / 86400; % Synodic period [days]

% Dates
cal0 = {Y0,1,1,0,0,0}; % Y-M-D h-m-s
departure_dates = linspace(0,PsN*Ps,1E3); % Departure date array [days]
tofs = linspace(10,tofY*365,1E3); % Times of Flight array [days]

% Display info
fprintf('----- Lambert Problem | PCP%s %s 2 %s @ %.0f -----\n',...
    opts.mano,departure_planet,arrival_planet,cal0{1}); % Title

% Simulation options
opts.odir = fullfile('C:','workcopy_tfm_outputs','PCP',...
    sprintf('PCP_%s2%s_%d_%s_P%d_Y%d_mr%d_lp%d',...
    departure_planet,arrival_planet,cal0{1},...
    opts.mano,PsN,tofY,mr,lp)); % Output dir
opts.overwrite_sim = 0; % Overwrite simulation
opts.plot_results = 1; % Plot results
opts.info_level = 10; % Info level
opts.maxdv = 100; % Maximum value for the DeltaV plots

% PCP Simulation
PCP_Simulation(departure_planet,arrival_planet,...
    cal0,departure_dates,tofs,mr,lp,opts);

