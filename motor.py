import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)  # mouth
GPIO.setup(24,GPIO.OUT)  # ears
GPIO.setup(25,GPIO.OUT)  #eyes

while(True):
	GPIO.output(23,True)
	time.sleep(0.5)
	GPIO.output(23,False)
	time.sleep(0.5)
