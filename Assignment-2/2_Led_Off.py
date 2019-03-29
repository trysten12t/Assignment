import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) # set GPIO17 as an OUTPUT 
GPIO.setup(27,GPIO.OUT) # set GPIO27 as am OUTPUT


 print ("LED off")
 GPIO.output(17,GPIO.LOW)
 GPIO.output(27,GPIO.LOW)
 
 


