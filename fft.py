

#matplotlib inline

import matplotlib.pyplot as plt
from scipy.fft import fft 


data_raw = open("50KHZ_200mV_p-p_1-5V_offset.txt", "r")

sampling_frequency = 1700000 # 1.7 MHz sampling frequency 

data = data_raw.read()
data = data.split(',')  # create a list containing all the datapoints 
nbr_of_samples = len(data)

# Number of samplepoints
N = nbr_of_samples

# Convert string entries in data to float entries. 
float_data = [0]*nbr_of_samples
for i in range(0,nbr_of_samples-1):
	float_data[i] = float(data[i])

# Set up a frequency vector for the x-axis 
x_vect = [0] * N       
for i in range(0, N):
	x_vect[i] = (i * (sampling_frequency/N))/1000   # divide by 1000 to get KHz along X axis  

#x_vect = x_vect * (sampling_frequency/N)  # convert the x axis to frequency 


fft_data = fft(float_data) # take the FFT of the original data
FFT_abs = abs(fft_data)/N 

plt.style.use('seaborn-whitegrid')
plt.plot(x_vect, FFT_abs, color ='red', linewidth=1)
plt.title('FFT of sampled signal')
plt.xlabel('Frequency KHz')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()









