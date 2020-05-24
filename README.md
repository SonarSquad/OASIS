# OASIS
Contains the complete code, circuit schematics and design of the OASIS prototype system.
The full OASIS - A low-cost modular echosounder thesis report should also be red for a better understanding if further development of the system are to be investigated.  

**HARDWARE modules:**
- LNA board - Low noise amplifier. (designed and tested)
- MCU board - ATmega4809 Full-bridge module. (designed and tested)
- ADC board - ADS8422 board Analog to Digital converter. (designed and tested)
- Raspberry pi 4 model B (4GB RAM). (bought and tested)

![Screenshot](full_module_comp.JPG)
![Screenshot](RX_Main_Echo.png)


**OBJECTIVES:** 
1. Start the sonar system, transducer transmit chirp signal at preset frequency. 
    - Pulse generaton is done on sepparate microcontroller (MCU).  
    
2. Switch into "receive mode" - receive and sample incomming returning echo. 

3. Plotting and light processing of received signal.
    - FFT: Frequency
    - Plotting: Time vs. voltage 


**CONTENT:**
- Working OASIS python script for Raspberry pi 4 (4GB). 
- MCU C code for wave generation on the ATmega4809. 
- 

