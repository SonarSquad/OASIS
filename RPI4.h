// OASIS Parallel ADC SW test 0.2 
// Author: Tor K. Gjerde 

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>

#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>

#include <unistd.h>

// Define which Raspberry Pi board/chipset you are using  -> OASIS = RaspberryPi 4

#define BCM2711_PERI_BASE       0xFE000000    // Peripheral base register for RPI4 
#define GPIO_BASE               (BCM2711_PERI_BASE + 0x00200000)	// GPIO controller 

#define PAGE_SIZE 		(4*1024)
#define BLOCK_SIZE 		(4*1024)

// Access 
struct bcm2835_peripheral {
    unsigned long addr_p;
    int mem_fd;
    void *map;
    volatile unsigned int *addr;
};

extern struct bcm2835_peripheral gpio; 	// 
extern struct bcm2835_peripheral bsc0;	//


// GPIO setup macros. Always use INP_GPIO(x) before using OUT_GPIO(x) or SET_GPIO_ALT(x,y)
#define INP_GPIO(g) 	*(gpio.addr + ((g)/10)) &= ~(7<<(((g)%10)*3))
#define OUT_GPIO(g) 	*(gpio.addr + ((g)/10)) |=  (1<<(((g)%10)*3))

#define GPIO_SET 	*(gpio.addr + 7)  // sets    bits which are 1 ignores bits which are 0
#define GPIO_CLR 	*(gpio.addr + 10) // clears  bits which are 1 ignores bits which are 0

#define GPIO_READ	        *(gpio.addr + 13) 
#define GPIO_READ_PIN(g)	*(gpio.addr + 13) &= (1<<(g))

// Functions 
int map_peripheral(struct bcm2835_peripheral *p);
void unmap_peripheral(struct bcm2835_peripheral *p);



