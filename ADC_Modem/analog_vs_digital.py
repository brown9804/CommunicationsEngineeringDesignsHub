#ANALOG -> DIGITAL SIGNAL
# DISPLAY

import numpy as np
import matplotlib.pyplot as plt
import random
"""
 ____   Signal/Data   ______________    Signal*/Data  ____
|    |               |              |                |    |
| TX |---------------| HALF PROCESS |----------------| RX |
|____|               |______________|                |____|
"""

dt = 0.2
t = np.arange(0, 10, dt)
analog_signal = 10*np.sin(t)                       # Signal OUTPUT TX
digital_signal = [random.choice([-10,10]) for i in t]  # Data OUTPUT TX

noise_amplitude = 1
AWGN = noise_amplitude * np.random.randn(len(t))  # White  Noise - HALF PROCESS

analog_signal_ed = analog_signal + AWGN         # Signal* INPUT RX
digital_signal_ed = digital_signal + AWGN               # Data* INPUT RX

fig, axs = plt.subplots(3, 2)
axs[0,0].plot(t, analog_signal)
axs[0,0].set_ylabel('Signal')

axs[1,0].plot(t, AWGN, color='red')
axs[1,0].set_ylabel('Noise')

axs[2,0].plot(t, analog_signal_ed, color='purple')
axs[2,0].set_ylabel('Signal*')
axs[2,0].set_xlabel('Time')

axs[0,1].plot(t, digital_signal, linestyle = 'steps')
axs[0,1].set_ylabel('Data')

axs[1,1].plot(t, AWGN, color='red')
axs[1,1].set_ylabel('Noise')

axs[2,1].plot(t, digital_signal_ed, linestyle = 'steps', color='purple')
axs[2,1].set_ylabel('Data*')
axs[2,1].set_xlabel('Time')

plt.show()
