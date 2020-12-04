function [ x, tofb, flag, i ] = Lambert_Izzo_2015_X_Tmin ( ...
    r1, r2, mu, lw, mr )
%Lambert_Izzo_2015_X_Tmin Returns minimum tof for a multirev transfer
%   Algorithm: Dario Izzo (Lancaster-Blanchard) [1]
%   Parameter: universal variable x
%
% Inputs:
%   r1: position vector of departure point
%   r2: position vector of arrival point
%   mu: standard gravitational parameter of the central body
%   lw: transfer type
%       0: type I (short-way) transfer
%       1: type II (long-way) transfer
%   mr: number of revolutions [0,Inf]
%
% Outputs:
%   x: universal variable value
%   tofb: minimum time-of-flight value
%   flag: status flag
%
% Example:
%   [ x, tofb ] = Lambert_Izzo_2015_X_Tmin ( [1,0,0],[0,2,0],[],1,0,0 )
%
% References:
%	[1] D. Izzo
%       Revisiting Lambert's problem
%       Celest. Mech. Dyn. Astron., vol. 121, no. 1, pp. 1–15, Jan. 2015
%   [2] https://github.com/esa/pykep
%
%David de la Torre Sangra
%July 2015


%% Preprocess

% Internal parameters
flag = 0; % Status
tol_halley = 1E-13; % Convergence tolerance (Halley iterator)
itermax_halley = 1E2; % Maximum number of iterations (Halley iterator)
x = NaN; tofb = NaN; % Initialize output vars

% Auxiliary magnitudes
r1n = norm3(r1); % Norm of r1
r2n = norm3(r2); % Norm of r2
lws = -(2 * lw - 1); % Long-way sign (lw=-1, ~lw=1)

% Compute geometrical parameters
c = norm3(r2 - r1); % Length of chord P1_P2
s = 0.5 * (r1n + r2n + c); % Semiperimeter of triangle P1_P2_F
lam2 = 1.0 - c/s; % Battin's Lambda parameter, squared, [1]
lam = lws * sqrt(lam2); % Lambda parameter, [1]
lam3 = lam2 * lam; % Powers of Lambda
lam5 = lam3 * lam2; % Powers of Lambda

%% Initial guess

% Parameters
% mr = floor(t/pi);
t00 = acos(lam) + lam * sqrt(1 - lam2); % [1] Eq. 19
t0 = t00 + mr * pi; % [1] Eq. 19

% Find Tmin for multi-rev case via Halley root solver
if mr > 0
    
    % Starters
    xold = 0;
    t = t0;
    
    % Halley iterator
    for i=1:itermax_halley
        
        % Compute derivatives
        [ dt, d2t, d3t ] = dtdx ( xold, t, lam2, lam3, lam5 );
        
        % Compute new x value (Halley method)
        if dt~=0
            xnew = xold - dt * d2t / (d2t * d2t - dt * d3t / 2.0);
        end
        
        % Check convergence
        %if abs(xnew - xold) < tol_halley
        if abs(dt) < tol_halley
            break;
        elseif i > itermax_halley
        	flag = 3; % Status: Max iterations exceeded
        	return;
        end
        
        % Compute TOF
        Tmin = x2tof ( xnew, mr, lam, lam2 );
        
        % Update old x value
        xold = xnew;
        
    end

    % Normalize outputs
    x = xnew;
    tofb = Tmin / sqrt(2.0 * mu / (s*s*s));

end

end

% Compute 1st-3rd derivatives for the Householder iterations
function [ dt, d2t, d3t ] = dtdx ( x, t, lam2, lam3, lam5 )

% Pre-compute values
omx2 = 1.0 - x^2;
omx2inv = 1.0 / omx2;
y = sqrt(1.0 - lam2 * omx2); % [1] p. 6
y2 = y * y;
y3 = y2 * y;
y5 = y3 * y2;

% Compute derivatives, from [1] Eq. 22
if x==0.0, dt = -2.0; % Min energy ellipse
elseif x==1.0, dt = 0.4 * (lam5 - 1.0); % Parabola, [1] Eq. 23
else, dt = omx2inv * (3.0*t*x - 2.0 + 2.0*lam3*x/y); % Other cases
end
d2t = omx2inv * (3.0*t + 5.0*x*dt + 2.0*(1.0-lam2)*lam3/y3);
d3t = omx2inv * (7.0*x*d2t + 8.0*dt - 6.0*(1.0-lam2)*lam5*x/y5);

end

% Compute 1st-3rd derivatives for the Householder iterations
% From the original C++ code...
function [ dt, d2t, d3t ] = dtdx_org ( x, t, m_lambda )

l2 = m_lambda * m_lambda;
l3 = l2 * m_lambda;
umx2 = 1.0 - x * x;
y = sqrt(1.0 - l2 * umx2);
y2 = y * y;
y3 = y2 * y;
dt = 1.0 / umx2 * (3.0 * t * x - 2.0 + 2.0 * l3 * x / y);
d2t = 1.0 / umx2 * (3.0 * t + 5.0 * x * dt + 2.0 * (1.0 - l2) * l3 / y3);
d3t = 1.0 / umx2 * (7.0 * x * d2t + 8.0 * dt - 6.0 * (1.0 - l2) * l2 * l3 * x / y3 / y2);

end

% Compute time of flight from x
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
        s1 = 0.5 * (1.0 - lam - x * eta);
        q = 4/3 * hypergeo2F1(s1);
        t = (eta^3 * q + 4 * lam * eta) / 2 + n*pi / rho^1.5;
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
tol = 1E-11;
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

% Compute hypergeometric series 2F1(3,1,5/2,x);
% From the original C++ code...
function Sj = hypergeo2F1_org ( x )
tol = 1E-11;
z = x;
Sj = 1.0;
Cj = 1.0;
err = 1.0;
j = 0;
while err > tol
    Cj1 = Cj * (3.0 + j) * (1.0 + j) / (2.5 + j) * z / (j + 1);
    Sj1 = Sj + Cj1;
    err = fabs(Cj1);
    Sj = Sj1;
    Cj = Cj1;
    j = j + 1;
end
end

