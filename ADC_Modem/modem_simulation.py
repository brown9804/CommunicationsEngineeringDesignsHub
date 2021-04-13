# MODEM 
# DISPLAY

import numpy as np
import matplotlib.pyplot as plt
import random

"""
 information  ____   signal   _______   signal*  ____  information*
      |    |         |       |         |    |
------| TX |---------| Mean |---------| RX |-------
      |____|         |_______|         |____|
"""

dt = 0.01
t = np.arange(0, 15, dt)

information = 10*np.sin(t)*np.sin(2*t)           # signal INPUT TX
awgn = 1*np.random.randn(len(t))  # white noise (Mean)
attenuation = 1/2                 # attenuation (Mean)
carrier = 3*np.cos(40*t)          # modulator

senal = information * carrier            # signal OUTPUT TX

senal_ed = attenuation * (senal) + awgn # signal INPUT RX

information_ed = senal_ed * 1/6 * carrier # signal OUTPUT RX

fig, axs = plt.subplots(5, 1)
axs[0].plot(t, information, color='blue')
axs[0].set_ylabel('Information')

axs[1].plot(t, senal, color='blue')
axs[1].set_ylabel('Signal')

axs[2].plot(t, awgn, color='red')
axs[2].set_ylabel('Noise')

axs[3].plot(t, senal_ed, color='purple')
axs[3].set_ylabel('Signal*')


axs[4].plot(t, information_ed, color='purple')
axs[4].set_ylabel('Information*')
axs[4].set_xlabel('Time')

fig.tight_layout()
plt.show()
