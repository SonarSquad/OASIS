
// OASIS ADC driver for ADS8422 Texas Instrument, parallel interface. 

#include "RPI4.h" 
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>



//---------------------- FUNCTIONS ---------------------------------------------------
struct bcm2835_peripheral gpio = {GPIO_BASE};


// Exposes the physical address defined in the passed structure using mmap on /dev/mem
int map_peripheral(struct bcm2835_peripheral *p)
{
   // Open /dev/mem
   if ((p->mem_fd = open("/dev/mem", O_RDWR|O_SYNC) ) < 0) {
      printf("Failed to open /dev/mem, check permissions.\n");
      return -1;
   }

   p->map = mmap(
      NULL,
      BLOCK_SIZE,
      PROT_READ|PROT_WRITE,
      MAP_SHARED,
      p->mem_fd,  // File descriptor to physical memory virtual file '/dev/mem'
      p->addr_p      // Address in physical map that we want this memory block to expose
   );

   if (p->map == MAP_FAILED) {
        perror("mmap");
        return -1;
   }

   p->addr = (volatile unsigned int *)p->map;

   return 0;
}

void unmap_peripheral(struct bcm2835_peripheral *p) {

    munmap(p->map, BLOCK_SIZE);
    close(p->mem_fd);
}

// -------------------------------------- MAIN -------------------------------------------------------
int main()
{
	if(map_peripheral(&gpio) == -1)
	{
		printf(" ERROR! failed to map physical GPIO registers into the virtual memory.\n");
		return -1; 
	}

	/*
   Define GPIOs as input 
   GPIOs used as laid out on the parallel ADC circuit board: ADS8422 -> Raspberry Pi 
   bit 0 =  GPIO 14     32-bit-string index 15
   bit 1 =  GPIO 15     32-bit-string index 16
   bit 2 =  GPIO 18     32-bit-string index 19
   bit 3 =  GPIO 23     32-bit-string index 24
   bit 4 =  GPIO 24     32-bit-string index 25
   bit 5 =  GPIO 25     32-bit-string index 26
   bit 6 =  GPIO 8      32-bit-string index 9
   bit 7 =  GPIO 7      32-bit-string index 8
   bit 8 =  GPIO 12     32-bit-string index 13
   bit 9 =  GPIO 16     32-bit-string index 17
   bit 10 = GPIO 20     32-bit-string index 21
   bit 11 = GPIO 21     32-bit-string index 22
   bit 12 = GPIO 26     32-bit-string index 27
   bit 13 = GPIO 19     32-bit-string index 20
   bit 14 = GPIO 13     32-bit-string index 14
   bit 15 = GPIO 6      32-bit-string index 7
   */

   INP_GPIO(6); 
   INP_GPIO(7);
   INP_GPIO(8);
   INP_GPIO(12);
   INP_GPIO(13);
   INP_GPIO(14);
   INP_GPIO(15);
   INP_GPIO(16);
   INP_GPIO(18);
   INP_GPIO(19);
   INP_GPIO(20);
   INP_GPIO(21);
   INP_GPIO(23);
   INP_GPIO(24);
   INP_GPIO(25);
   INP_GPIO(26);
    
   INP_GPIO(17);
   INP_GPIO(3); // Define GPIO 3 as input for BUSY pin from ADC 
	INP_GPIO(4); // Define GPIO 4 as input before next step 
   OUT_GPIO(17); // Redefine GPIO 17 as output RD 
	OUT_GPIO(4);  // Redefine GPIO 4 as output CONVST
  
   int CONVST = 4; 
   int BUSY = 3;
   int RD = 17;

   GPIO_SET = 1 << RD;        // set RD HIGH 
   GPIO_SET = 1 << CONVST;    // set CONVST HIGH 


   int nbr_of_samples = 1700000; 
   int data_array[1700000] = {}; 
   int counter = 0; 
   // Disable IRQ  
   // Local_irq_disable()  <-- This would need to be done with a sepparate kernel module  
   // Local_fiq_disable()  <-- This would need to be done with a sepparate kernel module 

	while(counter < nbr_of_samples)
	 {
      GPIO_CLR = 1 << CONVST; 	// Reset CONVST to LOW - initiate adc conversion
      GPIO_CLR = 1 << RD;        // Bring synchronization pin RD low to make parallel data out available 

      while(GPIO_READ_PIN(3) == 1){ 
        // printf("entered BUSY loop");
        // while the BUSY pin is high wait for ADC to finish conversion and change apears on BUSY pin
        //BUSY_state = GPIO_READ_PIN(3);
      }

      data_array[counter] = GPIO_READ; // read the whole 32-bit GPIO register (includes ADC output)
      //sleep(0.001);
      GPIO_SET = 1 << RD;        // Bring RD pin HIGH again 
      GPIO_SET = 1 << CONVST;   // Bring CONVST pin high again 
      
      counter++;
    }

   //Enable IRQ
   //local_fiq_enable(); <-- Needs to be done with a sepparate kernel module 
   //local_irq_enable(); <-- Needs to be done with a sepparate kernel module 

   for (int i = 0; i < nbr_of_samples; i++) // print the data array out 
   {
      printf("%i", data_array[i]); 
      if(i < nbr_of_samples - 1) // in order to NOT print a comma after last value 
      {
         printf(","); 
      }
   }

    
	return 0; 




}