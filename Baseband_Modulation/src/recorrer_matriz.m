% Recorrer vector o matriz - Brandon Esquivel Molina - B52571%

% Se define o se tiene una matriz.
% m = fix(rand(7,3)*10); % matriz de 7 filas 3 columnas con enteros de 0 a 10
ma = [1 1 1 1;1 1 1 1;1 1 1 1;1 2 3 4]
% Obtener dimensiones de la matriz
[f,c] = size(ma);

% Como tenemos dos dimensiones necesito dos bucles for, operando primero
% por columna j y luego la fila i.

for j=1:c
    for i=1:f
        ma(i,j) = 2*ma(i,j);
    end
end

ma
ma(2,2)