#!/usr/bin/env python3
import time
from datetime import datetime
import signal
import sys
import spidev

# SPI config
#	CLK => Rpi 23
#	MOSI => Rpi 19
#	CS => Rpi 24  (LE on HV5530) 
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629  #HV5530 can go up to 8MHz, but let's stay sane for now
spi.mode = 2
spi.bits_per_word = 8

#not a lot of shutdown hooks required, so just stuffing it all in the signal handler (like a dummy)
def signal_handler(sig, frame):
	print('Graceful Exit')

	# Close SPI
	spi.close()

	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


while True:
	data = [0xaa, 0xdd]
	spi.writebytes(data)
	time.sleep(10)
