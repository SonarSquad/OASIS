# ---------- For Plotting -----------
import math
import matplotlib.pyplot as plt
	
# ---------- Other imports ------------------
from subprocess import Popen, PIPE
import time



while True:
    counter = 0
    Vref = 4.096

    # start a subprocess: call the C code and let it run to do a parallel ADC read. 

    c_process = Popen("./oasis_read_ADC_parallel", stdin = PIPE, stdout = PIPE)
    outs, errs = c_process.communicate()

    #print(outs)

    """---------------------------------------------------------------------------------------------------------------------------------
    # Now the variable "outs" (bytes object) contains the states og the GPIO register after each ADC sample.
    # Each integer represents a 32-bit register read. Read cycle = 3.33MHz, so sampling rate = 3.33MHz. 

    NEXT TO DO: 
     1. Sort all the integers into a list.
    2. Convert integers to bit-string.
    3. Manipulate string in order to extract the bits representing the GPIOs actually connected to the parallel ADC.
    4. Sort the manipulated bits so that they have the right place in a 16-bit string. 
    5. Convert the 16-bit ADC string to voltage reading - remember 16-bit value is two's complement.   

    FURTHER ON:
    1. Now we can plot data.
    2. Signal processing.
    3. FFT and so on! 
    ----------------------------------------------------------------------------------------------------------------------------------
    """    

    data = outs.decode('UTF-8')               # Decode outs from byte-object and make a python string
    data_list_string = data.split(',')        # Split the string at comma and put all entries into a python list 
    number_of_samples = len(data_list_string)
    
    #print(data_list_string)
    # Manipulate entries in the 'data' list to extract actual voltage reading from ADC: 

    data_list_int = list(map(int, data_list_string)) # convert string-entries to integers 

    bit32_list_string = [0]*number_of_samples
    for i in range(0,number_of_samples):     # Convert integers from data_list_int to bit-string of 32 bits
        bit32_list_string[i] = ('{0:032b}'.format(data_list_int[i]))  
    #print(bit32_list_string)

    bit16_list_string = [0]*number_of_samples
    for i in range(0,number_of_samples):    # Extract bit position for the 16 GPIOs of interest from 32-bit register string
        bits = bit32_list_string[i]      
        #                    ADC-bit = RaspberryPi            index = (31 - GPIO)
        bit0  = bits[17]   # bit 0 =  GPIO 14       bit32_list_string  index 17
        bit1  = bits[16]   # bit 1 =  GPIO 15       bit32_list_string  index 16 
        bit2  = bits[13]   # bit 2 =  GPIO 18       bit32_list_string  index 13
        bit3  = bits[8]    # bit 3 =  GPIO 23       bit32_list_string  index 8 
        bit4  = bits[7]    # bit 4 =  GPIO 24       bit32_list_string  index 7 
        bit5  = bits[6]    # bit 5 =  GPIO 25       bit32_list_string  index 6 
        bit6  = bits[23]   # bit 6 =  GPIO 8        bit32_list_string  index 23 
        bit7  = bits[24]   # bit 7 =  GPIO 7        bit32_list_string  index 24 
        bit8  = bits[19]   # bit 8 =  GPIO 12       bit32_list_string  index 19 
        bit9  = bits[15]   # bit 9 =  GPIO 16       bit32_list_string  index 15 
        bit10 = bits[11]   # bit 10 = GPIO 20       bit32_list_string  index 11 
        bit11 = bits[10]   # bit 11 = GPIO 21       bit32_list_string  index 10 
        bit12 = bits[5]    # bit 12 = GPIO 26       bit32_list_string  index 5 
        bit13 = bits[12]   # bit 13 = GPIO 19       bit32_list_string  index 12 
        bit14 = bits[18]   # bit 14 = GPIO 13       bit32_list_string  index 18 
        bit15 = bits[25]   # bit 15 = GPIO 6        bit32_list_string  index 25 

        

        # Format 16-bit string: MSB -> LSB, Two's complement 
        bit16_list_string[i] = (bit15 + bit14 + bit13 + bit12 + bit11 + bit10 + bit9 + bit8 + bit7 + bit6 + bit5 + bit4 + bit3 + bit2 + bit1 + bit0)
        #print(bit16_list_string[i])
    
    bit16_list_int = [0]*number_of_samples
    for i in range(0, number_of_samples):                   # Convert bit string back to integer 
        bit16_list_int[i] = int(bit16_list_string[i],2)     
    
        if bit16_list_int[i] > 32767:                       # Convert from two's complement   2**15-1 = 32767
            bit16_list_int[i] = -65536 + bit16_list_int[i]
            #bit16_list_int[i] = -(bit16_list_int[i] - 32768)   
    
    #for i in range(0,5):
    #   print(bit16_list_int[i])


    ADC_list_voltage = [0]*number_of_samples                # Convert ADC bit-data to voltage reading
    for i in range(0, number_of_samples):
        ADC_list_voltage[i] = (2*Vref) * (bit16_list_int[i] / (2**15))
    
    
    #time.sleep(1)
    # The list: ADC_list_voltage now contains all samples represented as voltage  
    #print(bit16_list_string[1])
    #print(bit16_list_int[1])

    '''
    for i in range(0,5):
        print(f'{(ADC_list_voltage[i]):04f}')
    '''


    #time.sleep(1)
    plt.style.use('ggplot')
    sample_list = range(0,number_of_samples)
    plt.plot(sample_list, ADC_list_voltage, color='green', linewidth=1)
    plt.tight_layout()
    plt.show()
    