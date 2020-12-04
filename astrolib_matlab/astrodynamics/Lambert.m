function [ v1, v2, flag, i ] = Lambert ( r1, r2, tof, mu, lw, mr, lp )
%LAMBERT Solves the Lambert problem
%   Gateway to Lambert problem: normalises untits, solves Lambert's
%   problem, and de-normalises units.
%
% Inputs:
%   r1: position vector of departure point
%   r2: position vector of arrival point
%   tof: time of flight
%   mu: standard gravitational parameter of the central body
%   lw: transfer type
%       0: type I (short-way) transfer
%       1: type II (long-way) transfer
%   mr: number of revolutions [0,Inf]
%   lp: multi-revolution orbit type
%       0: short-period orbit
%       1: long-period orbit
%
% Outputs:
%   v1: final velocity at departure point (after the manoeuvre)
%   v2: initial velocity at arrival point (before the manoeuvre)
%   flag: function status: 0=OK, 1=BAD_IN, 2=NO_SOL, 3=MAX_IT, 4=PI_FG
%   i: number of iterations
%   dbg: debugging data
%
% Example:
%   [ v1, v2 ] = Lambert ( [1,0,0], [0,2,0], pi, 1, 0, 0 );
%
% References:
%   [-]
%
%David de la Torre Sangra
%September 2015

% Default transfer direction (prograde)
if nargin < 5 || isempty(lw)
    theta = DeltaNu3(r1,r2,1); % Cosine of transfer angle (3D), [0-2pi]
    if theta > pi, lw = 1; else, lw = 0; end % Long-way transfer (Type II)
end

% Default multi-revolution case (single-rev)
if nargin < 6 || isempty(mr), mr = 0; end

% Default mr-period case (multi-rev)
if nargin < 7 || isempty(lp), lp = 0; end

% Iteration tolerance
tol = 1E-6;

% Normalize magnitudes
[ nr1, nr2, ntof, nmu, xr, xt, ~ ] = NorMag_Lambert( r1, r2, tof, mu );

% Call Lambert algorithm
[ nv1, nv2, flag, i ] = Lambert_Izzo_2015_X_HH_RT ( ...
    nr1, nr2, ntof, nmu, lw, mr, lp, tol );

% De-normalise magnitudes
v1 = nv1 * xr / xt;
v2 = nv2 * xr / xt;

% Force row-wise output
v1 = v1(:)';
v2 = v2(:)';

end

