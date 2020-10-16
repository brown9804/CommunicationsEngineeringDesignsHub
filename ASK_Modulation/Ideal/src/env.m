%%EE-320 Matlab Assignment-1
%%Envelope Detection Technique
close all;
clear all;
t=0:1e-7:1000e-6;               %sampling time instants
s=size(t,2);
tau=26e-6:1e-6:499e-6;          %varying time constant
sizetau=size(tau,2);
output=zeros(474,s);            %output of Envelope Detector
fm=2000;                        %Message frequency
fc=40000;                       %Carrier frequency
low_bound=1/fc;                 %lower bound on Time Constant
high_bound=1/fm;                %upper bound on Time constant
msg_sig=cos(2*pi*fm*t);         %message signal
carr_sig=cos(2*pi*fc*t);        %carrier signal
ka=0.5;                         %sensitivity factor
mod_sig=zeros(1,s);             %modulated signal
output(:,1)=1+ka;
for k=1:s
    mod_sig(k)=(1+ka*msg_sig(k))*carr_sig(k);
    msg_sig1(k)=1+ka*msg_sig(k);           %message signal to calculate MSE
end
msqe=zeros(1,sizetau);                     %Mean Square Error
for j=1:sizetau
    for k=1:s-1
        if(mod_sig(k)<output(j,k))
            output(j,k+1)=output(j,k)*exp(-1e-7/tau(j));
        else
            output(j,k+1)=mod_sig(k);
        end
    end
    error=msg_sig1-output(j,:);
    errorsq=error.^2;
    sum=0;
    for l=1:s
        sum=sum+errorsq(l);
    end
    mse(j)=sum/s;
end
[a,b]=min(mse);
mintau=tau(b);                      %Optimum Value of Time Constant
minmse=a;
plot(t,mod_sig);
hold on
plot(t,output(b,:),'r');xlabel('Time'),ylabel('Modulated Signal and Envelope');
title('Output of Envelope Detector at Least MSE')
figure(2)
plot(tau,mse);xlabel('TAU'),ylabel('MSE'),title('MSE v/s Time Constant')
