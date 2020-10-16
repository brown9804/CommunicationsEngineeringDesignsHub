% Brandon Esquivel Molina - B52571 %
% Quantization, in general, is the process of constraining an input from a continuous or otherwise
% large set of values (such as the real numbers) to a discrete set (such as the integers).

function [ bfc ] = Cuantization(y, k)

levels = 2^k;
b = length(y);
Max = max(y);                               % max value of Input
Min = min(y);
Qrange = abs(Max)+ abs(Min);
Drange = Qrange/levels;
bfc = zeros(b,1);

for i=1:b
    for j=1:levels
        if( (y(i)<= (Min + Drange*j)) && (y(i) > (Min + Drange*(j-1))) )
            bfc(i) = (Min + Drange*j);
        end
    end
end
    
    
end

