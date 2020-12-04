function [ pos ] = GetFigCC ( w, h )
%GETFIGCC Get Figure Centered Coordinates
%   Returns vector with coordinates [W0,H0,W,H] of a centered figure.
%
% Inputs:
%   w: figure width [px]
%   h: figure height [px]
%
% Outputs:
%   pos: [w0, h0, w, h]
%
% Example:
%   [ pos ] = GetFigCC ( 800, 600 );
%
% References:
%	
%
%David de la Torre Sangra
%August 2014

% Detect inputs
if nargin==1 && length(w)==2 % Single input with both magnitudes
    wh = w; % Save input array
    clear w; % Clear variable
    w = wh(1); % Get width
    h = wh(2); % Get height
elseif nargin < 2 % Too few inputs
    w = 600; % Set default width
    h = 400; % Set default height
end

% Get screen dimensions [pixels]
ss = get(0,'ScreenSize');

% Initial coordinates, centered on the screen
w0 = floor(ss(3)/2 - w/2); % Width-magnitude stating point
h0 = floor(ss(4)/2 - h/2); % Height-magnitude starting point
if h0 < 10, h0 = 10; end % Avoid figures out of screen
if w0 < 10, w0 = 10; end % Avoid figures out of screen

% Construct vector to be used in 'Position' property of figures
pos = [w0, h0, w, h];

end

