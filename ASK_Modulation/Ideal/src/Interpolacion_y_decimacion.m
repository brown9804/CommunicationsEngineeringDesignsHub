% Interpolacion y decimacion

clc; clear all; close all;

%  Primero se lee el archivo de audio

[yin,fs] = audioread('/home/est/Documentos/IE1116/Archivos de Audio/piano C6.wav');
b = length(yin);                        % Tamano del arreglo leido
t = b/fs;                               % Tiempo en segundos del archivo
%  plot(yin);                             grafico en el tiempo
%  sound(yin,fs)                        % Reproducir sonido 
 
%% DECIMACION

e1 = 1/3;                                % Se define la escala de interpolacion 
fs1 = fs*e1;

% Definicion de nuevo array

c = 0;                                   % Contador
b1 = b*e1;                               % Tamano del nuevo array
t1 = b1/fs;                              % Tiempo del nuevo array

for i=1:b                                
    c = c+1;
    if c==3
y1(i/3,1) = yin(i,1);
    c=0;
    end
end
sound(yin,fs)
pause(5)
sound(y1,fs)
% Al reproducir el sonido se puede escuchar el efecto "ardilla" 
% en el sonido, esto sin modificar la frecuencia a la que se reproduce.


% Graficas en el tiempo y frecuencia


% Grafica en el tiempo

plot(yin);
hold on;
plot(y1);
title('Señal original(Yin) y procesada(Y1) en el tiempo');xlabel('tiempo(s)'); ylabel('amplitud');
grid on;

% Grafica en la frecuencia

% Se  obtienen los espectros 

Yo1 = fft(yin);
yf = abs(Yo1/b);
yff = yf(1:b/2+1);
yff(2:end-1) = 2*yff(2:end-1);
f = fs*(0:(b/2))/b;

Yo11 = fft(y1);
yf = abs(Yo11/b1);
yff1 = yf(1:b1/2+1);
yff1(2:end-1) = 2*yff1(2:end-1);
f1 = fs*(0:(b1/2))/b1;


plot(f1,yff1);
hold on;
plot(f,yff)
title('Señal original(Yin) y procesada(Y1) en la frecuencia');
xlabel('frecuencia(Hz)');
ylabel('amplitud'); grid on;




% Escritura del archivo de audio

audiowrite('PianoC6_decimacion.wav',y1,fs);

%% INTERPOLACION


e2 = 1/e1;                % misma escala que decimacion en este caso. Siempre es inversa
fs2 = fs1*e2;
b2 = b*e2;                % Tamano del nuevo array interpolado
t2 = b2/fs;               % Tiempo del nuevo array interpolado

for i=1:b
 y2(e2*i:i*e2+e2,1) = yin(i,1);
end

sound(y2,fs);


% Graficas en el tiempo y frecuencia

% Grafica en el tiempo

plot(yin);
hold on;
plot(y2);
title('Señal original(Yin) y procesada(Y2) en el tiempo - Interpolacion - efecto ballena');xlabel('tiempo(s)'); ylabel('amplitud');
grid on;

% Grafica en la frecuencia

% Se  obtienen los espectros 

Yo12 = fft(y2);
yf = abs(Yo12/b2);
yff2 = yf(1:b2/2+1);
yff2(2:end-1) = 2*yff2(2:end-1);
f2 = fs*(0:(b2/2))/b2;


plot(f2,yff2);
hold on;
plot(f,yff)
title('Señal original(Yin) y procesada(Y2) en la frecuencia - Interpolacion');
xlabel('frecuencia(Hz)');
ylabel('amplitud'); grid on;







% Escritura del archivo de audio

audiowrite('PianoC6_interpolacion.wav',y2,fs);