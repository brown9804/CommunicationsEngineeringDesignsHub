% Diferents Process to study the ASK Modulation, with Noise.
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
%ampFactor = 1000;                                 % Amplifies the input signal to obtain greater precision in small values, when modulating, then it is reversed dividing by this same factor    
% plot(y);                                        % time domain graphic. Verification
% sound(y,fs)                                     % Play sound. Verification
Tbit = 1/fs;                                      % bit time, perid
Rbit = fs;                                        % bit rate bits/s                             
%dataAmp = y*ampFactor;                            % amplification
%% Anlyz and visualization in the frequency domain
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
%% ASK MODULATION STAGE
k = 8;
Tsym = k*Tbit;
Ns = 100;
levels = 2^k;
M = levels;
b = length(y);
fc = 400;
Ac = sqrt(2/Tsym);                          % amplitude for 1J of energy
Max = max(y);                               % max value of Input
Min = min(y);
Qrange = abs(Max)+ abs(Min);
Drange = Qrange/levels;
bfc = zeros(b,1);
X = zeros(b,1);
alphabet = zeros(M,1);
Fss = fs*Ns;
t0 = 0:1/fs:(b-1)/fs;                                   % Axis to plot and generate Carrier wave
phi = 2*pi*fc;
tc = 0:1/Fss:(b*Ns-1)/Fss;                                      % Axis to plot the ASK wave
carrier = transpose(Ac*cos(phi*t0));                % Carrier cos signal
c = zeros(Ns*b,1);

for a = 1:M
   alphabet(a)= a;                       % this is the Codification alphabet 
end
                
for i=1:b
    for j=1:levels
        if( (y(i)<= (Min + Drange*j)) && (y(i) > (Min + Drange*(j-1))) )
            bfc(i) = (Min + Drange*j);
            X(i) = alphabet(j);
            
        end
        c((i*Ns)-(Ns-1):i*Ns,1) = carrier(1:Ns,1)*X(i); 
    end
end


%% Plot
figure;                                     % Ploting results
grid on;
subplot(1,2,1);
plot(t0,carrier,'g');
%axis([0 0.2 -1.2 1.2]);
xlabel('Time (sec)');
ylabel('Amplitude');
title('Carrier wave');
subplot(1,2,2);
plot(t0,X,'r');
xlabel('Time (sec)');
ylabel('Amplitude');
title('Input data Result wave');
%%
subplot(1,2,1);
plot(t0,X,'r');
xlabel('Time (sec)');
ylabel('Amplitude');
title('Input data Result wave');
subplot(1,2,2);
%%
figure;
grid on;
plot(tc,c,'g');
xlabel('Time (sec)');
ylabel('Amplitude');
title('ASK Result wave');

%% NOISE ADD STAGE
NSR = 1;                                         % Noise factor
maxN = (Max/4)*NSR;                                 % max Noise value
n = transpose(-maxN + (maxN + maxN)*rand(1,Ns*b));     % WG Noise
Xn = c + n;                                       % Adding Noise
figure;
grid on;
subplot(1,2,1);                                 % Plotting results
plot(tc,c,'r');
xlabel('Time (sec)');
ylabel('Amplitude');
title('ASK Result wave');
legend('Clear');
grid on;
subplot(1,2,2);                                 % Plotting results
plot(tc,Xn,'g');
grid on;
xlabel('Time (sec)');
ylabel('Amplitude');
title('ASK wave with Noise');
legend('Noise');
grid on;
%% Plotting Noise Vs Clean overlap

figure;                                     % Ploting results
grid on;
plot(tc,c,'g',tc,Xn,'--');
xlabel('Time (sec)');
ylabel('Amplitude');
title('ASK Result wave vs ASK with Noise');
legend('Clear','Noise');
grid on;
%% ASK Demodulation stage 
%envelope = envelope(c,Fss);
env = abs(hilbert(c));
up1 = envelope(c,fs);
%% to plot the envelope signal
plot_param = {'Color', [0.6 0.1 0.2],'Linewidth',2}; 
plot(tc,c);
hold on;
plot(tc,env,plot_param{:});
hold off;
xlim([0 0.04]);
title('Hilbert Envelope');
%% by direct indexing ---: beta
dem = zeros(1,b);
demod = zeros(1,b);
j = 1;
for i=1:Ns:b*Ns
    demod(j,1) = c(i,1);
    dem(j,1) = max(c(i:i+Ns,1));
    j = j+1;
end
%% to plot the envelope signal
plot_param = {'Color', [0.9 0.4 0.2],'Linewidth',2}; 
plot(tc,c);
hold on;
plot(tc,up1,plot_param{:});
hold off;
xlim([0 0.04]);
title('Direct Envelope');

%% to plot the envelope signal

figure;                                     % Ploting results
grid on;
plot(tc,envelope,'g');
xlabel('Time (sec)');
ylabel('Amplitude');
title('ASK wave senvelope');
grid on;


%% Plotting results
figure;                                     % Ploting results
grid on;
subplot(1,2,1);
plot(t0,y,'g');
%axis([0 0.2 -1.2 1.2]);
xlabel('Time (sec)');
ylabel('Amplitude');
title('Original wave');
grid on;
subplot(1,2,2);
plot(t0,X,'r');
xlabel('Time (sec)');
ylabel('Amplitude');
title('Received wave');
grid on;
%% Play & output
sound(y,fs);                                                % Play
pause(3);   
sound(bfc,fs);                                               % Play
audiowrite('./outputs/snareNOISE.wav',bfc,fs);               % write audioFile
