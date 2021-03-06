# OASIS
Contains the complete code, circuit schematics and designs for the OASIS prototype system.
The full OASIS - A low-cost modular echosounder thesis report should also be red for a better understanding if further development of the system are to be investigated.  


**CONTENT: folder and content**
- LNA_Rev3: PCB design files for the LNA board (ALTIUM).
- Oasis_ADC_PCB: PCB design files and gerbers for the ADC board (KICAD).
- Oasis_MCU_bridge_PCB: PCB design files and gerbers for MCU board (KICAD).
- Python code and drivers: Main python script and C- code drivers for the OASIS system
- MCU_ATmega4809: Code for waveform-generation on the ATmega4809. 
- SPI_test_alternative_ADC: Example code for setting up SPI communication on the Raspberry Pi 4 (not used in OASIS prototype).  


**HARDWARE modules:**
- LNA board - Low noise amplifier. (designed and tested)
- MCU board - ATmega4809 Full-bridge module. (designed and tested)
- ADC board - ADS8422 board Analog to Digital converter. (designed and tested)
- Raspberry pi 4 model B (4GB RAM). (bought and tested)

![Screenshot](full_module_comp.JPG)

**OASIS Prototype achievements:** 
1. System startup, Transmit a pulse at preset frequency (200kHz).
    - Pulse generaton is done on sepparate microcontroller (MCU).
    
2. Amplify returning echo with LNA.  
    
3. Sample returning echo, (switch not developed yet - two transducers used while testing, one for transmit and one for receive). 
    - Receive and sample incomming returning echo. Sampling @ 1.7 Msps.  

4. Plotting and light processing of received signal.
    - Plot: FFT. 
    - Plot: Time vs. voltage. 
    
![Screenshot](sampled_ADC_data.png)
________________________________________________________________________________________________________
**CONTACT:** 
- Martin Ericsson - tlf: 92649342, email: martincse94@gmail.com 
- Tor K. Gjerde - tlf: 46934462, email: torgjerde.nor@gmail.com
- Torbjørn Willson - tlf: 46810798, email: torbjorw@ntnu.no
- Einar Avdem - tlf: 98813120, email: einarav@stud.ntnu.no 


