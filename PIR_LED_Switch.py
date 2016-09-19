import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) #LED
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Switch
GPIO.setup(25, GPIO.IN)	#PIR Sensor

eventCount = 0;
while True:
	if GPIO.input(23) :		 #if the switch is on, the security system is in place
		if GPIO.input(25) :  #If you found an intruder
			GPIO.output(24,True)	 #turn diode ON
			print ("Intruder found, EventCount: {}",eventCount)
			eventCount = eventCount + 1
			time.sleep(0.3)		#Wait 1 Second
		else:
			GPIO.output(24, False) #turn the LED Off
			eventCount =0;
			time.sleep(0.1)
	else: 
		GPIO.output(24,False) #if the switch is off, don't light it
		time.sleep(20)
