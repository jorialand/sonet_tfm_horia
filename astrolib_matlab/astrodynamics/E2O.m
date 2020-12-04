function [ nu ] = E2O ( E, ecc )
%O2E Eccentric anomaly to true anomaly
%   Computes the true anomaly nu corresponding to an eccentric anomaly E
%
% Inputs:
%   E: eccentric anomaly [rad]
%   ecc: eccentricity [0-1]
%
% Outputs:
%   nu: true anomaly [rad]
%
% Example:
%   nu = E2O ( pi/2, 0.3 );
%
% References:
%	[-]
%
% See also:
%   T2O, O2E, E2M, M2E, E2O, O2T
%
%David de la Torre Sangra
%August 2014

% Compute true anomaly nu
if ecc < 1 % Elliptic orbits
    nu = 2.0 * atan(sqrt((1.0 + ecc) ./ (1.0 - ecc)) .* tan(E / 2.0));
elseif ecc > 1 % Hyperbolic orbits
    nu = 2.0 * atan(sqrt((ecc + 1.0) ./ (ecc - 1.0)) .* tanh(E / 2.0));
else % Parabolic orbits
    nu = 2.0 * atan(E);
end

end

