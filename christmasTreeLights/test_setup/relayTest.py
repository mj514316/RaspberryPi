import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) #ch1  7
GPIO.setup(17,GPIO.OUT) #ch2  0
GPIO.setup(27, GPIO.OUT) #ch3 2
GPIO.setup(22,GPIO.OUT) #ch4  3
GPIO.setup(5, GPIO.OUT) #ch5  
GPIO.setup(6,GPIO.OUT) #ch6
GPIO.setup(13, GPIO.OUT) #ch7
GPIO.setup(19, GPIO.OUT) #ch8
gpioList = [4,17,27,22,5,6,13,19]
sleepTime = 0.1

def scrollThrough(gpioList, sleepTime):
	for pin in gpioList:
		GPIO.output(pin,True)
		time.sleep(sleepTime)
		GPIO.output(pin,False)
		
def evenOn(gpioList, sleepTime):
	for pin in range(len(gpioList)):
		if(pin%2==0):
			GPIO.output(gpioList[pin],True)
	time.sleep(sleepTime)
	for pin in range(len(gpioList)):
		if(pin%2==0):
			GPIO.output(gpioList[pin],False)

def oddOn(gpioList, sleepTime):
	for pin in range(len(gpioList)):
		if(pin%2!=0):
			GPIO.output(gpioList[pin],True)
	time.sleep(sleepTime)
	for pin in range(len(gpioList)):
		if(pin%2!=0):
			GPIO.output(gpioList[pin],False)			
		
		
for i in range(3):
	scrollThrough(gpioList,0.1)
	evenOn(gpioList,0.5)
	oddOn(gpioList,0.5)
	evenOn(gpioList,0.5)
	oddOn(gpioList,0.5)
	time.sleep(0.5)
GPIO.cleanup()
