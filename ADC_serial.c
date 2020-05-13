

#include <bcm2835.h>
#include <stdio.h>

#define BUSY RPI_V2_GPIO_P1_10  // GPIO pin 15, BUSY to ADC board 
#define CONV RPI_V2_GPIO_P1_11  // GPIO pin 17, CNV to ADC board 


int main(int argc, char **argv)
{
    if (!bcm2835_init())
    {
      printf("bcm2835_init failed. Are you running as root??\n");
      return 1;
    }
    if (!bcm2835_spi_begin())
    {
      printf("bcm2835_spi_begin failed. Are you running as root??\n");
      return 1;
    }

    uint64_t nbr_of_samples = 4000000;
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    bcm2835_gpio_fsel(CONV, BCM2835_GPIO_FSEL_OUTP); // set Gpio 17 to output 
    bcm2835_gpio_fsel(BUSY, BCM2835_GPIO_FSEL_INPT);  // set Gpio 15 to input 
    //bcm2835_gpio_set_pud(BUSY, BCM2835_GPIO_PUD_UP);  // pull up resistor

    bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);      // The default
    bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);                   // The default
    bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_2);    // The default
    bcm2835_spi_chipSelect(BCM2835_SPI_CS0);                      // The default
    bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);      // the default
    
    uint8_t value = bcm2835_gpio_lev(BUSY); // read BUSY pin
    printf("read from pin 15: %d\n", value); 

    for (int i = 0; i < nbr_of_samples; i++) // print the data array out 
    {
      uint8_t send_data = 0x23;
      uint8_t read_data = bcm2835_spi_transfer(send_data);
      //printf("Sent to SPI: 0x%02X. Read back from SPI: 0x%02X.\n", send_data, read_data);
    }
    // Send a byte to the slave and simultaneously read a byte back from the slave
    // If you tie MISO to MOSI, you should read back what was sent
    return 0;
}
