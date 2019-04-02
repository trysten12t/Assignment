import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) # set GPIO17 as an OUTPUT 
GPIO.setup(27,GPIO.OUT) # set GPIO27 as am OUTPUT

loop = 0

while (loop < 100):
 print ("LED on")
 GPIO.output(17,GPIO.HIGH)
 GPIO.output(27,GPIO.HIGH)
 time.sleep(1)
 print ("LED off")
 GPIO.output(17,GPIO.LOW)
 GPIO.output(27,GPIO.LOW)
 time.sleep(1)
 loop = loop + 1
 
print ("Finished")

