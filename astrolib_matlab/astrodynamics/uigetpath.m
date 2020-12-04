function [ file_path ] = uigetpath (  )
%UIGETPATH Returns the full path for a uigetfile command

% Get file via GUI
[ file_name, path_name ] = uigetfile;

% Return on cancel
if isnumeric(file_name)
    file_path = file_name;
    return;
end

% Build file path
file_path = fullfile ( path_name, file_name );

end

