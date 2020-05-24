/*
 * OASIS 
 * Sine chirp generator
 * Created: 05.03.2020 10:26:09
 * Edited:  04.05:2020 10:13:37
 */

#ifndef F_CPU
#define F_CPU 20000000
#endif

#define TR_Switch_TX_and_CPU_Sync	PORTD_OUTSET = 0x03
#define TR_Switch_RX_and_CPU_Sync	PORTD_OUTCLR = 0x03

#include <avr/io.h>
#include "test.h"
#include <avr/interrupt.h>

void ClkSelect(void);

int main(void)
{
	ClkSelect(); //Forces 20MHz system clock
	PORTD_DIR		|= PIN0_bm |PIN1_bm;  //TX/RX and CPU_sync as OUTPUT 
	PORTF_DIR		|= PIN4_bm |PIN5_bm;  //PWM pins as OUTPUT
	PORTD.PIN0CTRL	|= PORT_ISC_RISING_gc;//Enable PORTD pin change interrupt 
	sei();		//Enable global interrupt
    while (1) 
	{  
		//Waits for CPU signal
    }
}

ISR(PORTD_PORT_vect)
{
	cli();						//Disable global interrupt
	PORTD_INTFLAGS = 0xFF;		//Clearing interrupt flags
	TR_Switch_TX_and_CPU_Sync;  //Switches the transducer to transmit mode
	chirp();				    //Down Chirp from 208kHz - 192 kHz
	TR_Switch_RX_and_CPU_Sync;	//Switches the transducer to receive mode
	sei();						//reenable global interrupts
}

void ClkSelect(void)
{	//Forces 20MHz CPU clock frequency (disables prescaler)
	_PROTECTED_WRITE(CLKCTRL.MCLKCTRLB, 0<<CLKCTRL_PEN_bp); 
}


