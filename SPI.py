
import spidev
import time
import RPi.GPIO as GPIO              
from time import sleep               

CNV = 21
BUSY = 20

GPIO.setmode(GPIO.BCM)                # choose BCM or BOARD 
GPIO.setup(BUSY, GPIO.IN)             # set BUSY as input 
GPIO.setup(CNV, GPIO.OUT)             # set CNV as an output
GPIO.setup(CNV, GPIO.OUT, initial=0)  # set CNV initial state to zero 

spi = spidev.SpiDev()

spi.open(0, 1) # (channel/bus,device) 
spi.max_speed_hz = 1500000

sampled_data = [0]*1000000
cnt = 0
for i in sampled_data:
    GPIO.output(CNV,1)     # high to start conversion

    while GPIO.input(BUSY) == 1: # wait for ADC to finish conversion 
        ()
    GPIO.output(CNV,0) # reset start conversion high down to low 
    return_data = spi.readbytes(5)
    sampled_data[cnt] = return_data
    cnt = cnt + 1 
    #time.sleep(0.5)

print(sampled_data)