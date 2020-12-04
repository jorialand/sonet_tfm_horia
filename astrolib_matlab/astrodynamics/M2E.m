function [ E, i ] = M2E ( M, ecc, tol )
%M2E Mean anomaly to eccentric anomaly
%   Computes the eccentric anomaly E from the mean anomaly M and the orbit
%   eccentricity e by means of several algorithms
%
%   Allows for elliptic, parabolic and hyperbolic orbits
%
%   Elliptic form (0 < e < 1) of Kepler's equation:
%   M = E - ecc * sin(E)
%
%   Parabolic form (e = 1) of Kepler's equation:
%   M = D + D^3 / 3
%
%   Hyperbolic form (1 < e < INF) of Kepler's equation:
%   N = ecc * sinh(F) - F
%
% Inputs:
%   M: mean anomaly [rad]
%   ecc: eccentricity [0,INF)
%   tol: iteration tolerance [rad]
%
% Outputs:
%   E: eccentric anomaly [rad]
%   i: number of iterations performed
%
% Example:
%   [ E, i ] = M2E ( pi/2, 0.1, 1E-9 );
%
% References:
%   [1] ...
%   [2] Vieta's Substitution
%       http://mathworld.wolfram.com/VietasSubstitution.html
%   [3] de la Torre, D.
%       n/a
%
% See also:
%   T2O, O2E, E2M, M2E, E2O, O2T
%
%David de la Torre Sangra
%August 2014

% Parameters
ni = 1E3; % Maximum allowed iterations

% Fix M within allowed range
if ecc < 1.0 % Elliptic range: 0,2pi
    M = mod(M,2*pi);
elseif ecc == 1 % Parabolic range: 0,2pi
    M = mod(M,2*pi);
else % Hyperbolic range: -Inf,Inf
    
end

% Select most efficient method depending on eccentricity
if ecc < 1.0 % Newton-Raphson method, elliptic (eccentric anomaly: E)

    % Initial guess for E
    if ecc < 0.6 % Low eccentricity region
        E = M;
    elseif M < 1/2*pi % High ecc, low M region [3]
        E = 1.8 * M^(1/3);
    elseif M > 2*pi - 1/2*pi % High ecc, high M region [3]
        E = 2*pi - 1.8 * (2*pi - M)^(1/3);
    else % High ecc, mid M region
        E = pi;
    end

    % Iterate until convergence
    for i=1:ni

        % Backup current value
        Ebkp = E;

        % Compute new value
        E = E - (E - ecc * sin(E) - M) / (1 - ecc * cos(E));

        % Tolerance achieved
        if abs(E - Ebkp) < tol, break; end

    end
    
elseif ecc == 1 % Newton-Raphson method, parabolic (eccentric anomaly: D)
    
    % Initial guess for E
    % Polynomial fit, 3rd order (E = aM^2 + bM^2 + cM + d)
    % Valid only in the range M = [0, 2*pi]
    E = + 0.010339878573138 * M*M*M ...
        - 0.145808540593580 * M*M ...
        + 0.868928344112862 * M ...
        + 0.055225631234924;

    % Iterate until convergence
    for i=1:ni

        % Backup current value
        Ebkp = E;

        % Compute new value
        E = E - (E + E*E*E / 3 - M) / (1 + E*E);

        % Tolerance achieved
        if abs(E - Ebkp) < tol, break; end

    end
    
%     % Analytic formula to solve Barker's equation (M=D+1/3*D^3)
%     Q = 12 * M + 4 * sqrt(4 + 9 * M);
%     E = 1/2 * Q^(1/3) - 2 * Q^(-1/3);
    
else % Newton-Raphson method, hyperbolic (eccentric anomaly: F)
    
    % Initial guess for E
    E = asinh(M / ecc);

    % Iterate until convergence
    for i=1:ni

        % Backup current value
        Ebkp = E;

        % Compute new value
        E = E - (ecc * sinh(E) - E - M) / (ecc * cosh(E) - 1);

        % Tolerance achieved
        if abs(E - Ebkp) < tol, break; end

    end
    
end

end

