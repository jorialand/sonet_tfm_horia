function [  ] = Plot_PCP_DeltaV ( tofs, departure_dates, delta_v,...
    departure_planet, arrival_planet, delta_v_title_prefix, ...
    file_name, label_x, label_y, z_cap, fopts )
%PLOT_DELTAV_PCP plots a Porkchop plot with DeltaV values

% Set default inputs
if ~exist('fopts','var') || isempty(fopts) % Figure options
    fopts.placeholder = ''; % Empty
end
if ~exist('label_x','var') || isempty(label_x) % X label
    label_x = 'Time of Flight [days]';
end
if ~exist('label_y','var') || isempty(label_y) % Y label
    label_y = 'Departure date [days from 01/01/2000]';
end
if ~exist('z_cap','var') || isempty(z_cap) % Level cap for z axis
    z_cap = Inf;
end

% Set default figure options
if ~isfield(fopts,'Name'), fopts.Name = 'PCP'; end
if ~isfield(fopts,'Visible'), fopts.Visible = 'on'; end
if ~isfield(fopts,'Renderer'), fopts.Renderer = 'painters'; end
if ~isfield(fopts,'Position'), fopts.Position = GetFigCC(1200,600); end
if ~isfield(fopts,'savepng'), fopts.savepng = 1; end
if ~isfield(fopts,'saveeps'), fopts.saveeps = 0; end
if ~isfield(fopts,'savepdf'), fopts.savepdf = 0; end
if ~isfield(fopts,'doCtrs'), fopts.doCtrs = 1; end

% Figure
fh = figure(); % Figure
fh.Name = fopts.Name; % Figure name
fh.Visible = fopts.Visible; % Visibility
fh.Renderer = fopts.Renderer; % Renderer
fh.Position = fopts.Position; % Dimensions
fh.PaperPositionMode = 'auto'; % Paper Position
hold on;

% Colormap & Colorbar
colormap(jet(1024));
colorbar('EastOutside');

% Remove data values higher than the cap level
delta_v(delta_v > z_cap) = NaN;

% Plot Data
contourf(tofs,departure_dates,delta_v,256,'LineStyle','none'); % Contourf
if fopts.doCtrs % Draw contour lines/labels
    ctrs = [0,5,10,20:20:120,150,200:100:1000]; % Contours
    [C,~] = contour(tofs,departure_dates,delta_v,ctrs,'Color','w'); % Contours
    clabel(C,ctrs,'Color','w','FontWeight','Bold'); % Contourlabels
end

% Style
set(gca,'FontSize',18); box on; grid on; set(gca,'layer','top'); % Style
xlabel(label_x); ylabel(label_y); % Labels
xlim([0,tofs(end)]);

% Build extra title parts
if exist('departure_planet','var') && ~isempty(departure_planet) && ...
        exist('arrival_planet','var') && ~isempty(arrival_planet)
    planets_str = [departure_planet,' to ',arrival_planet,' | '];
else
    planets_str = '';
end
if ~exist('delta_v_title_prefix','var') || isempty(delta_v_title_prefix)
    delta_v_title_prefix = '';
end

% Title
title(['PCP | ',planets_str,delta_v_title_prefix,' \DeltaV [km/s]']);

% Save Plot
if fopts.savepng
    print(fh,'-dpng','-r300','-painters',[file_name,'.png']); % Save PNG
end
if fopts.saveeps
    print(fh,'-depsc','-r300','-painters',[filename,'.eps']); % Save EPS
end
if fopts.savepdf
    print(fh,'-dpdf','-r300','-painters',[filename,'.pdf']); % Save PDF
end

% Close figure
close(fh);

end

