
# Autohor: Tor K Gjerde - OASIS bachelor thesis -  May 2020. 
import matplotlib.pyplot as plt
from scipy.fft import fft
import time 


data_raw = open("20mVrms_200kHz_LNA.txt", "r")

sampling_frequency = 1700000 # 1.7 MHz sampling frequency 

data = data_raw.read()
data = data.split(',')  # create a list containing all the datapoints 
nbr_of_samples = len(data)

# Number of samplepoints
N = nbr_of_samples
print(N)

# Convert string entries in data to float entries. 
float_data = [0]*nbr_of_samples
for i in range(0,nbr_of_samples):
	float_data[i] = float(data[i])

# Set up a frequency vector for the x-axis 
x_vect = [0] * N       
for i in range(0, N):
	x_vect[i] = (i * (sampling_frequency/N))/1000   # divide by 1000 to get KHz along X axis  


fft_data = fft(float_data, N) # Take the FFT of the original data

FFT_abs = abs(fft_data) # Absolute value 

FFT_scaled = ((FFT_abs / N) * 2) # Scaled and multiplied by 2 - only one mirrored part valid. 


file_object = open("FFT_data_ADC_bench_test.txt", "w")
for i in range(0, nbr_of_samples):
	file_object.write(str(FFT_scaled[i]))
	file_object.write("\n")



plt.style.use('seaborn-whitegrid')
plt.plot(x_vect, FFT_scaled, color ='red', linewidth=1)
plt.title('FFT of sampled signal')
plt.xlabel('Frequency KHz')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()









