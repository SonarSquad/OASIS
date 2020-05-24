
# Autohor: Tor K Gjerde - OASIS bachelor thesis -  May 2020.  

import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import ion, show

data_raw = open("TEST2_12_MAY.txt", "r")

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


sample_nbr = [0]*nbr_of_samples
for i in range(0, nbr_of_samples):
    sample_nbr[i] = i
    
plt.style.use('seaborn-whitegrid')
plt.plot(sample_nbr, data, color ='red', linewidth=1)
plt.title('Plotting of ADC voltage data')
plt.xlabel('Sample nbr.')
plt.ylabel('voltage difference between inputs')
plt.tight_layout()
plt.show()



