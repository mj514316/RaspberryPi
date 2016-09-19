import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

while True:
	if GPIO.input(23) :		 #if the switch is on, light the diode
		GPIO.output(24,True)	 #turn diode ON
		time.sleep(0.1)		#Wait 1 Second
		GPIO.output(24, False) #turn the LED Off
		time.sleep(0.1)
	else: 
		GPIO.output(24,False) #if the switch is off, don't light it
		time.sleep(1)



