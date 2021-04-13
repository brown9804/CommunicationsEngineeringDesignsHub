% Diferents Process to study the PAM Modulation, with Noise.
% Brandon Esquive Molina
% UCR
% github: @brandonEsquivel

%% Reset Protocol
clear;
close all;
clc;

%% source encoding, getting source data --> audio  
[y, fs] = audioread('./inputs/snare.wav');        % reading file
b = length(y);                                    % array size
t = b/fs;                                         % Duration, time, seconds
ampFactor = 1000;                                 % Amplifies the input signal to obtain greater precision in small values, when modulating, then it is reversed dividing by this same factor    
% plot(y);                                        % time domain graphic. Verification
% sound(y,fs)                                     % Play sound. Verification
Tbit = 1/fs;                                      % bit time, perid
Rbit = fs;                                        % bit rate bits/s                             
dataAmp = y*ampFactor;                            % amplification
%% Analysis and visualization in the frequency domain
figure;
Y = fft(y);                                       % Fast fourier transform
P2 = abs(Y/b);                                    % Positive  values
P1 = P2(1:b/2+1);           
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(b/2))/b;                               % axis to plot
plot(f,P1,'--');                                  % plotting
grid on;            
xlabel('Frecuency (Hz)');
ylabel('Amplitude');
title('frequency spectrum of source data');


%% PAM MODULATION STAGE
k = 5;                                      % bit grouping, k bits/symb
M = 2^k;                                    % PAM Order M = 2^k --> k = 5  32 possibles symbols
Tsym = k*Tbit;                              % symbol time
Rsym = 1/Tsym;                              % Symbols rate
Max = max(y);                               % max value of Input   
t0 = 0:1/fs:(b-1)/fs;                       % Axis to plot and generate Carrier wave
carrier = transpose(square(2*pi*500*t0));   % square signal PAM 
PAM = y.*carrier;                           % obtaining PAM
figure;                                     % Ploting results
grid on;
subplot(1,2,1);
plot(t0,carrier,'g');
axis([0 0.2 -1.2 1.2]);
xlabel('Time (sec)');
ylabel('Amplitude');
title('Square Periodic Wave -> Carrier wave');
subplot(1,2,2);
plot(t0,PAM,'r');
xlabel('Time (sec)');
ylabel('Amplitude');
title('PAM Result wave');

%% NOISE ADD STAGE
NSR = 0.01;                                         % Noise factor
maxN = (Max/4)*NSR;                                 % max Noise value
n = transpose(-maxN + (maxN + maxN)*rand(1,b));     % WG Noise
Xn = PAM + n;                                       % Adding Noise
figure;                                             % Plotting results
plot(t0,PAM,'r',t0,Xn,'g');
xlabel('Time (sec)');
ylabel('Amplitude');
title('PAM Result wave vs PAM wave with Noise');
legend('Clear', 'Noise');

%% Codification, Encoding, quantization by M levels with NOISE

data = uencode(Xn,M);                           % quantization  and encoding by M levels with NOISE, more leves = more quality
decoded = udecode(data,M);                      % decoding
figure;                                         % plot results
grid on;
subplot(1,2,1);
plot(t0,y,'g');
xlabel('Time (sec)');
ylabel('Amplitude');
title('Original source sigal');
subplot(1,2,2);
plot(t0,decoded,'r');
xlabel('Time (sec)');
ylabel('Amplitude');
title('Decoded PAM signal');

%% Play & output
sound(y,fs);                                                % Play
pause(3);   
sound(decoded,fs);                                          % Play
audiowrite('./outputs/snareNOISE.wav',decoded,fs);           % write audioFile
