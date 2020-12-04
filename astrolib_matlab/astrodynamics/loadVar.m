function [ varargout ] = loadVar ( fn, varargin )
%loadVar returns the variables from a file.
%Improves Matlab's vanilla 'load' function.
%
%   Inputs:
%   - fileName: name of file to load variables from.
%   - varargin: name of selected variables. Empty returns all vars.
%
%   Outputs:
%   - varargout = selected variables
%
%
%   Examples:
%
%   % Returns all variables from file directly to workspace
%   loadVar('db.mat');
%
%   % Assigns all variables from file to the output vars
%   % The variables will be assigned by storage order, up to nargout
%   [a,b,c] = loadVar('db.mat');
%
%   % Assigns all variables from file to the output vars
%   % Overload the function to return only the first variable in file
%   a = loadVar('db.mat');
%
%   % Returns only selected variables from file
%   [c,b,a] = loadVar('db.mat','c','b','a');
%
%   % If a variable does not exist in 'db.mat' file, returns empty
%   [VARS{:}] = loadVar('db.mat','c','b','a');
%   ...if 'b' does not exist: VARS == {c,[],a}
%
%
%   This code is part of the MEMM software.
%   David de la Torre Sangra
%   (C) UPC-ETSEIAT 2013-2014

% Load file via UI if required
if ~exist('fn','var') || isempty(fn)
    [fileName,pathName] = uigetfile; % Get file via UI
    fn = [pathName,fileName]; % Build file path
end

% Ensure file path is string
if ~ischar(fn)
    warning('File path is not a string. Returning empty array');
    varargout = cell(nargout,1); return; % Return empty array
end

% Ensure file exists
if ~exist(fn,'file')
    warning(['File "',fn,'" does not exist. Returning empty array']);
    varargout = cell(nargout,1); return; % Return empty array
end

% Load variables
if nargin<2 % Return all variables in file
    if nargout>0 % Assign variables to outputs
        varargout = struct2cell(load(fn));
    else % Return all variables to base workspace
        aux = load(fn); % Load variables
        ff = fieldnames(aux); % Get fields = var names
        for i=1:length(ff)
            assignin('base',ff{i},aux.(ff{i})); % Copy vars to workspace
        end
    end
else % Return selected variables from file
    varargout = cell(nargout,1); % Preallocate varargout
    allvars = whos('-file',fn); % Get file information
    varindx = ismember(varargin,{allvars.name}); % Get valid vars
    aux = load(fn,varargin{varindx}); % Load valid vars from file
    [~,posindx] = ismember(fields(aux),varargin); % Get indexes of valid vars
    posindx = posindx(posindx~=0); % Remove zeroes in array
    varargout(posindx) = struct2cell(aux); % Return valid vars only
end

end

