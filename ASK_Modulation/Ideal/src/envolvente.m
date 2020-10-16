% Deteccion de ritmo / tiempo de un archivo de Audio.
close all
clear;
clc;

% Se lee el archivo

[x fs1] = audioread("IE1116/Archivos de Audio/piano C6.wav"); 

np1 = 800;                                  % ganancia de la envolvente
[up1,lo1] = envelope(x,np1,'peak');          % Obtencion de la envolvente
np2 = 3000;
[up2,lo2] = envelope(x,np2,'peak');
subplot(2,1,1);
plot(up1,'Linewidth',3);
hold on;
plot(x);

subplot(2,1,2)
plot(up2,'Linewidth',3);
hold on;
plot(x);

% Prueba con otro archivo


[x fs1] = audioread("IE1116/Archivos de Audio/Escala1.wav"); 

np1 = 800;                                  % ganancia de la envolvente
[up1,lo1] = envelope(x,np1,'peak');          % Obtencion de la envolvente
np2 = 8000;
[up2,lo2] = envelope(x,np2,'peak');
subplot(2,1,1);
plot(up1,'Linewidth',3);
hold on;
plot(x);

subplot(2,1,2)
plot(up2,'Linewidth',3);
hold on;
plot(x);


% Otro archivo

[x fs1] = audioread("IE1116/Archivos de Audio/Ritmo bateria.wav"); 

np1 = 800;                                  % ganancia de la envolvente
[up1,lo1] = envelope(x,np1,'peak');          % Obtencion de la envolvente
np2 = 8000;
[up2,lo2] = envelope(x,np2,'peak');
subplot(2,1,1);
plot(up1,'Linewidth',3);
hold on;
plot(x);

subplot(2,1,2)
plot(up2,'Linewidth',3);
hold on;
plot(x);





% Se concluye que para un archivo de audio de mayor frecuencia o de mayores
% cambios, es debido utilizar una ganancia de suavizado mucho mayor, cuando
% el sonido es mas limpio, y de menor frecuencua, como una bateria, se
% puede utilizar una ganancia de suavizado menor. Esta es mejor encontrarla
% de forma empirica o experimental.



