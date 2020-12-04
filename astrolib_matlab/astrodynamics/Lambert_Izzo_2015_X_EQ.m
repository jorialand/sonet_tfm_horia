function [ tt, dt ] = Lambert_Izzo_2015_X_EQ ( xx, r1, r2, mu, lw, mr )
%Lambert_Izzo_2015_X_EQ Returns algorithm's equation values
%   Algorithm: Dario Izzo [1]
%
%   The free parameter x has the following range:
%   - 1 < x < 1: elliptic orbits
%   x = 0: minimum energy orbit
%   x = 1: parabolic orbit
%   1 < x < INF: hyperbolic orbits
%
% Inputs:
%   x: iterator variable values
%   r1: position vector of departure point
%   r2: position vector of arrival point
%   mu: standard gravitational parameter of the central body
%   lw: transfer type
%       0: type I (short-way) transfer
%       1: type II (long-way) transfer
%   mr: number of revolutions [0,Inf]
%
% Outputs:
%   tt: time-of-flight values
%   dt: derivative of time-of-flight values
%
% Example:
%   x0 = linspace(-1,5,1E2); % Iterator variable range for mr = 0
%   x1 = linspace(-1,1,1E2); % Iterator variable range for mr > 0
%   t0 = Lambert_Izzo_2015_X_EQ(x0,[1,0,0],[0,2,0],pi,1,0,0);
%   t1 = Lambert_Izzo_2015_X_EQ(x1,[1,0,0],[0,2,0],4*pi,1,1,1);
%   t2 = Lambert_Izzo_2015_X_EQ(x1,[1,0,0],[0,2,0],8*pi,1,1,2);
%   t3 = Lambert_Izzo_2015_X_EQ(x1,[1,0,0],[0,2,0],12*pi,1,1,3);
%   tTOF = ones(1,length(x)); % TOF target value
%   plot(x0,t0,x1,t1,x1,t2,x1,t3,x,tTOF,'--');
%   legend('0-rev','1-rev','2-rev','3-rev','TOF');
%   xlabel('x'); ylabel('t'); ylim([0,20]);
%
% References:
%	[1] D. Izzo
%       Revisiting Lambert's problem
%       Celest. Mech. Dyn. Astron., vol. 121, no. 1, pp. 1–15, Jan. 2015
%   [2] https://github.com/esa/pykep
%
%David de la Torre Sangra
%August 2015

% Auxiliary magnitudes
r1n = norm3(r1); % Norm of r1
r2n = norm3(r2); % Norm of r2
lws = -(2 * lw - 1); % Long-way sign (lw=-1, ~lw=1)

% Compute geometrical parameters
c = norm3(r2 - r1); % Length of chord P1_P2
s = 0.5 * (r1n + r2n + c); % Semiperimeter of triangle P1_P2_F
lam2 = 1 - c/s; % Battin's Lambda parameter, squared, [1]
lam = lws * sqrt(lam2); % Lambda parameter, [1]
lam3 = lam2 * lam; % Powers of Lambda
lam5 = lam3 * lam2; % Powers of Lambda

% Initialize parameters
tt = NaN(1,length(xx));
dtt = NaN(1,length(xx));

% Iterate until convergence
for i=1:length(xx)
    
    % Get iteration parameters
    x = xx(i);
    
    % Avoid stupid values
    if mr>0 && x>1, continue; end
    
    % Compute t (TOF)
    t = x2tof ( x, mr, lam, lam2 );
    
    % Compute derivatives
    [ dt, ~, ~ ] = dtdx ( x, t, lam2, lam3, lam5 );

    % Recover un-normalised value for tof/dtof
    if isreal(t)
        tt(i) = t / sqrt(2 * mu / (s*s*s));
        dtt(i) = dt / sqrt(2 * mu / (s*s*s));
    else
        tt(i) = NaN;
        dtt(i) = NaN;
    end

end

end

% Compute 1st-3rd derivatives for the Householder iterations
function [ dt, d2t, d3t ] = dtdx ( x, t, lam2, lam3, lam5 )

% Pre-compute values
omx2 = 1 - x * x;
omx2inv = 1 / omx2;
y = sqrt(1 - lam2 * omx2); % [1] p. 6
y2 = y * y;
y3 = y2 * y;
y5 = y3 * y2;

% Compute derivatives, from [1] Eq. 22
if x==0, dt = -2; % Min energy ellipse
elseif x==1, dt = 0.4 * (lam5 - 1); % Parabola, [1] Eq. 23
else, dt = omx2inv * (3*t*x - 2 + 2*lam3*x/y); % Other cases
end
d2t = omx2inv * (3*t + 5*x*dt + 2*(1-lam2)*lam3/y3);
d3t = omx2inv * (7*x*d2t + 8*dt - 6*(1-lam2)*lam5*x/y5);

end

% Compute TOF via Lagrange equation
function t = x2tof ( x, n, lam, lam2 )

% Distance from x=1 to trigger Battin / Lancaster expressions
battin = 0.01;
lagrange = 0.2;
dist = abs(x - 1);

% Select optimal expression to compute TOF
if dist < lagrange && dist > battin % Use Lagrange TOF expression

    % Semi-major axis
    a = 1 / (1 - x*x);

    % Compute TOF
    if a > 0 % Ellipse
        alpha = 2 * acos(x); % [1] Eq. 10
        beta = 2 * asin(sqrt(lam2 / a)); % [1] Eq. 11
        if lam < 0, beta = -beta; end
        t = (a*sqrt(a) * ((alpha - sin(alpha)) ...
            - (beta - sin(beta)) + 2*pi*n))/2; % [1] Eq. 9
    else % Hyperbola
        alpha = 2 * acosh(x); % [1] Eq. 10
        beta = 2 * asinh(sqrt(-lam2/a)); % [1] Eq. 11
        if lam < 0, beta = -beta; end
        t = -a*sqrt(-a) * ((beta - sinh(beta)) ...
            - (alpha - sinh(alpha)))/2; % [1] Eqn. 9
    end

else % Use Battin's / Lancaster TOF expressions

    % Compute universal variable z
    e = x*x - 1;
    rho = abs(e);
    z = sqrt(1 + lam2 * e);

    % Compute TOF
    if dist < battin % Use Battin TOF expression, [1] Eq. 20
        eta = z - lam * x;
        s1 = (1 - lam - x * eta) / 2;
        q = 4/3 * hypergeo2F1(s1);
        t = (eta^3 * q + 4 * lam * eta) / 2 + n*pi / (rho*sqrt(rho));
    else % Use Lancaster TOF expresion
        y = sqrt(rho);
        g = x * z - lam * e;
        if e < 0
            l = acos(g);
            d = n*pi + l;
        else
            f = y * (z - lam * x);
            d = log(f + g);
        end
        t = (x - lam * z - d / y) / e;
    end

end

end

% Compute hypergeometric series 2F1(3,1,5/2,x);
function f = hypergeo2F1 ( x )

% Parameters
tol = 1E-9;
kmax = 1E3;

% Initialize
f = 1;
term = 1;

% Compute series
for k = 0:kmax
    term = term * (3+k) * (1+k) / (2.5+k) * x / (k+1); % New term
    f = f + term; % Add new term to the series
    if abs(term) <= tol, break; end % Series has converged
end

end

