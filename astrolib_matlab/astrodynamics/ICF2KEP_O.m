function [ sma, ecc, inc, nu, argp, raan ] = ICF2KEP_O ( r, v, mu )
%ICF2KEP State vector to keplerian elements
%   Converts a state vector (position and velocity) in Inertial Coordinate
%   Frame ICF (xyz) into the corresponding set of orbital elements
%
%   OPTIMIZED CODE
%
% Inputs:
%   r: position [x,y,z] in ICF coordinates (ijk) [km]
%   v: velocity [vx,vy,vz] in ICF coordinates (ijk) [km s^-1]
%   mu: standard gravitational parameter of the central body [km^3 s^-2]
%
% Outputs:
%   sma: semi-major axis [km]
%   ecc: eccentricity [#]
%   inc: inclination [rad]
%   nu: true anomaly [rad]
%   argp: argument of periapsis [rad]
%   raan: right ascension of ascending node [rad]
%
% Example:
%   [ sma, ecc, inc, nu, argp, raan ] = ICF2KEP_O ( [1.5E8,0,0], [0,30,0], 1.32E11 )
%
% References:
%   [1] Curtis, Howard D.
%       Orbital mechanics for Engineering Students, Chapter 4.4
%       Butterworth-Heinemann, Elsevier, Oxford, 2010
%
%David de la Torre Sangra
%August 2014

% Auxiliary magnitudes
rn = sqrt(r(1)*r(1) + r(2)*r(2) + r(3)*r(3)); % Position norm
vn = sqrt(v(1)*v(1) + v(2)*v(2) + v(3)*v(3)); % Velocity norm
vr = (r(1)*v(1) + r(2)*v(2) + r(3)*v(3)) / rn; % Radial velocity
twopi = 2.0 * pi;

% Specific angular momentum vector (cross product between r and v)
h(1) = r(2)*v(3) - r(3)*v(2);
h(2) = r(3)*v(1) - r(1)*v(3);
h(3) = r(1)*v(2) - r(2)*v(1);
hn = sqrt(h(1)*h(1) + h(2)*h(2) + h(3)*h(3)); % Norm

% Eccentricity vector
e = 1/mu * ((vn*vn - mu / rn) * r - (rn * vr) * v); % [1] Eq. 4.10
ecc = sqrt(e(1)*e(1) + e(2)*e(2) + e(3)*e(3)); % Norm

% Semi-major axis
if ecc ~= 1 % Elliptic, Hyperbolic orbits
    sma = (hn*hn / mu) / (1 - ecc*ecc); % [1] Eq. 2.71, Eq. 2.103
else % Parabola: assign value of semi-latus rectum (p) to variable sma
    sma = hn*hn / mu;
end

% Inclination (angle between hz and h)
inc = acos(h(3) / hn); % [1] Eq. 4.7

% Node vector (cross product between z and h)
if inc > 0 && inc < pi % Inclined orbit
    n = [-h(2),h(1),0]; % [1] Eq. 4.8
else
    n = [1,0,0]; % By convention
end
nn = sqrt(n(1)*n(1) + n(2)*n(2)); % Norm

% Longitude of the ascending node (angle between nx and n)
raan = acos(n(1) / nn); % [1] Eq. 4.9
if n(2) < 0, raan = twopi - raan; end % 3rd/4th quadrant angle

% Argument of periapsis (angle between raan and e)
if (inc > 0 && inc < pi) && (ecc > 0) % Eccentric inclined orbit
    argp = acos((n(1)*e(1) + n(2)*e(2) + n(3)*e(3)) / (nn * ecc)); % [1] Eq. 4.12
    if e(3) < 0, argp = twopi - argp; end % 3rd/4th quadrant angle
elseif ecc > 0 % Equatorial eccentric orbit (assumes raan = 0)
    argp = atan2(e(2),e(1)); % 2D geometry
    if h(3) < 0, argp = twopi - argp; end % Retrograde orbit
else % Equatorial circular orbit (assumes raan = 0)
    argp = 0; % Convention: places w at raan
end

% True anomaly
% Eccentric orbit: true anomaly 'nu' (angle between e and r)
% Circular inclined orbit: argument of latitude 'u' (angle between n and r)
% Circular equatorial orbit: true longitude 'l' (angle between rx and r)
if ecc > 0 % Eccentric orbit
    cos_nu = (e(1)*r(1) + e(2)*r(2) + e(3)*r(3)) / (ecc * rn);
    cos_nu = max([-1, min([+1, cos_nu])]); % Avoid overshooting bounds
    nu = acos(cos_nu); % [1] Eq. 4.13
    if vr < 0, nu = twopi - nu; end % 3rd/4th quadrant angle
elseif inc > 0 && inc < pi % Circular inclined orbit
    nu = acos((n(1)*r(1) + n(2)*r(2) + n(3)*r(3)) / (nn * rn)); % []
    if (n(1)*v(1) + n(2)*v(2) + n(3)*v(3)) > 0, nu = twopi - nu; end % 3rd/4th quadrant angle
else % Circular equatorial orbit
    nu = acos(r(1) / rn); % []
    if v(1) > 0, nu = twopi - nu; end % 3rd/4th quadrant angle
end

% Fix nu within allowed range
if ecc < 1 % Elliptic range: 0,2pi
    nu = mod(nu,twopi);
else % Parabolic/Hyperbolic range: -pi,pi
    while nu > pi, nu = nu - twopi; end
    while nu < -pi, nu = nu + twopi; end
end

end

