
%%%......... Modulación ASK........%%%

% Se carga la imagen que se quiere transmitir %

C = imread('entrada.jpeg');


J = imresize(C,[70 70]);
image(J)
G = reshape(J,[],1);
O = int16(G);

% Codificación de fuente %
% Se cofican los píxeles de la imagen J, se obtiene un vector de 1s y 0s

R = de2bi(O);

T = reshape(R,[],1);

% Se obtienen los bits que se quieren transmitir
bl = transpose(T);

% Periodo de bits
Tb=.000001;                                           
disp(' Bits de información en el transmisor :');
disp(bl);
%%
% Representacion de bits de información transmitida como senal digital x
x=[]; 
for n=1:1:length(bl)
    if bl(n)==1;
       se=ones(1,100);
    else bl(n)==0;
        se=zeros(1,100);
    end
     x=[x se];
end

tx=Tb/100:Tb/100:100*length(bl)*(Tb/100);

% Se pasa de bit a simbolo y se obtiene la señal x(t) %

plot(tx,x,'lineWidth',0.000001);grid on;
axis([ 0 Tb*length(bl) -.5 1.5]);
ylabel('x(t)');
xlabel('t[s])');
title('Señal moduladora');
%%
% Señal portadora %

% Como la señal x(t) oscila entre 1 y 0 se determina lo siguiente: %

Amp1 = 10; % Amplitud para señal portadora para 1s
Amp2 = 5; % Amplitud para señal portadora para 0s
Rb = 1/Tb; % Tasa de bits
f=Rb*10;  %Frecuencia de señal portadora

tp=Tb/99:Tb/99:Tb;  %Tiempo de la señal portadora

ss=length(tp);
s=[];

for (i=1:1:length(bl))
    if (bl(i)==1)
        y=Amp1*cos(2*pi*f*tp);
    else
        y=Amp2*cos(2*pi*f*tp);
    end
    s=[s y];
end

s_ruido = awgn(s,10,'measured');  %Adicion del ruido a la senal modulada
ts=Tb/99:Tb/99:Tb*length(bl)
plot(ts,s_ruido);
xlabel('t[s])');
ylabel('s(t)[V]');
title('Senal modulada s(t)con ruido aditivo blanco gaussiano');
%%
%>>>>>>>Demodulacion binaria ASK<<<<<<<%
blp=[]; % bl*
for n=ss:ss:length(s_ruido)
  t=Tb/99:Tb/99:Tb;
  y=cos(2*pi*f*t);                   % Senal portadora 
  mm=y.*s_ruido((n-(ss-1)):n);
  t4=Tb/99:Tb/99:Tb;
  z=trapz(t4,mm)                      % integracion 
  zz=round((2*z/Tb))                                     
  if(zz>7.5)                     % Nivel logico = (A1+A2)/2=7.5
    a=1;
  else
    a=0;
  end
  blp=[blp a];
end
disp(' Informacion binaria recibida en el receptor :');
disp(blp);


% Se realiza una prueba para comparar bl con bl*

if bl==blp
   disp(' A y b son d');
else
     disp(' A y b son d no');
end

% De manera visual %
xp=[]; % Sería como x(t)*
for n=1:length(blp);
    if blp(n)==1;
       se=ones(1,100);
    else blp(n)==0;
        se=zeros(1,100);
    end
     xp=[xp se];
end
t4=Tb/100:Tb/100:100*length(blp)*(Tb/100);
plot(t4,xp,'LineWidth',0.000001);grid on;
axis([ 0 Tb*length(blp) -.5 1.5]);
ylabel('x(t)*');
xlabel(' t[s] ');
title('Senal x(t)* recibida despues de demodulacion ASK');

%% Decodificación

W = reshape(blp ,[14700,8]);
%De bits a símbolos
Q = bi2de(W);
% De símbolos a pixeles
M = uint8(Q);
Cp = reshape(M,[70,70,3]);

 if Cp==J
   disp(' La información enviada es igual ala recibida');
else
     disp(' La información enviada no es igual ala recibida');
 end
%Información recibida.
image(Cp)