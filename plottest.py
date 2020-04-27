
import math
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import signal 
from scipy.signal import chirp	
import numpy as np	

plt.style.use('dark_background')

x_vals = []
y_vals = []
z_vals = []
index = count()

chirp_hz_start = 200
chirp_hz_end   = 2.5
freq = 10
pi = np.pi
time_chirp = np.linspace(0, 1, 5000)
sample = 8000
time = np.arange(sample)
length = len(time)

#signal_sin = np.sin(2 * pi * freq * time / sample) + 0.1*np.cos(2 * pi * 800 * time / sample) + 0.2 * np.cos(2* pi * 50 * time /sample)
#signal_chirp = chirp(time_chirp, f0 = chirp_hz_start, f1 = chirp_hz_end, t1=1, method='linear')
signal_sin = np.sin(2 * pi * freq * time / sample )

def animate(i):
	x_vals.append(time[next(index)])
	y_vals.append(signal_sin[next(index)]) # plotting sine signal 
	plt.cla()
	plt.plot(x_vals, y_vals, color='green', linewidth=1)

	#print(signal_chirp[next(index)])



ani = FuncAnimation(plt.gcf(), animate,  interval=1)

plt.tight_layout()
plt.show()

