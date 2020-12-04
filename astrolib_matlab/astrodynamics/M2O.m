function [ nu ] = M2O ( M, ecc, tol )
%O2M True anomaly to mean anomaly
%   Computes the true anomaly O corresponding to a mean anomaly M
%
%Inputs:
%   M: mean anomaly [rad]
%   ecc: eccentricity [0-1]
%   tol: tolerance
%
%Outputs:
%   nu: true anomaly [rad]
%
%Example:
%   nu = M2O ( pi/2, 0.3 );
%
% References:
%	[-]
%
% See also:
%   T2O, O2E, E2M, M2E, E2O, O2T
%
%David de la Torre Sangra
%January 2016

% Compute eccentric anomaly E
E = M2E(M,ecc,tol);

% Compute true anomaly nu
nu = E2O(E,ecc);

end

