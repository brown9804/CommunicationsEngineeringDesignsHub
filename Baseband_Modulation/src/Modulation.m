% Brandon Esquivel Molina - B52571 %
% 

function [ bfc, X, PAM ] = Modulation(y, fs, k)
levels = 2^k;
M = levels;
b = length(y);
Max = max(y);                               % max value of Input
Min = min(y);
Qrange = abs(Max)+ abs(Min);
Drange = Qrange/levels;
bfc = zeros(b,1);
X = zeros(b,1);
alphabet = zeros(M,1);
t0 = 0:1/fs:(b-1)/fs;                       % Axis to plot and generate Carrier wave
phi = 2*pi*500;
carrier = transpose(square(phi*t0));   % square signal PAM 


for a=1:M
   alphabet(a) = a; 
end

for i=1:b
    for j=1:levels
        if( (y(i)<= (Min + Drange*j)) && (y(i) > (Min + Drange*(j-1))) )
            bfc(i) = (Min + Drange*j);
            X(i) = alphabet(j);
        end
    end
end
    
    
PAM = X.*carrier;  





end

