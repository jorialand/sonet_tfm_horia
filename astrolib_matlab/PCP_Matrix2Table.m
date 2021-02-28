clc; clear; close all;

% Load the pcp .mat file in matrix format.
addpath(genpath("astrodynamics"));
data_file = uigetpath();
in = load(data_file);

% Create the table.
cols = ["DepDates","tof","c3d","c3a","dvd","dva","dvt","theta"];
N = length(in.tofs); %A N by N matrix has N^2 elements

t = table(nan(N^2,1) , ...
          nan(N^2,1) , ...
          nan(N^2,1) , ...
          nan(N^2,1) , ...
          nan(N^2,1) , ...
          nan(N^2,1) , ...
          nan(N^2,1) , ...
          nan(N^2,1) , 'VariableNames', cols); %trasposed vectors .

% Fill it.
tic; k = 1;
for i = 1:N %DepDates
  for j = 1:N %tof

      % Variables independientes
      t.DepDates(k) = in.departure_dates(i); %DepDates
      t.tof(k) = in.tofs(j); %tof

      % Variables dependientes
      t.c3d(k) = in.c3d(i,j); %c3d
      t.c3a(k) = in.c3a(i,j); %c3a
      t.dvd(k) = in.dvd(i,j); %dvd
      t.dva(k) = in.dva(i,j); %dva
      t.dvt(k) = in.dvt(i,j); %dvt
      t.theta(k) = in.theta(i,j); %theta

      k = k+1;
  end
  disp(i)
end

% Write it.
writetable(t);