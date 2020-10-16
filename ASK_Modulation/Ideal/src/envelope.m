function y=envelope(signal,Fs)
%Envelope Detection based on Hilbert Transform
%Normal FFT
y=signal;
N=length(y);
T=N/Fs;
sig_f=abs(fft(y(1:N)',N));
sig_n=sig_f/(norm(sig_f));
freq_s=(0:N-1)/T;
[a,b]=butter(2,0.25);  %butterworth Filter of 2 poles and Wn=0.25
analy=hilbert(signal);
y=analy;
sig_sq=2*y.*conj(y);
y_sq = filter(a,b,sig_sq); %applying filter
 y=sqrt(y_sq);%taking Square root for voltage
% y=y_sq; % Power