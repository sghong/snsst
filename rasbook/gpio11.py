import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print ("setup LED pin")

GPIO.setup(11,GPIO.OUT)
GPIO.output(11, False)

GPIO.output(11,True)

time.sleep(2)

GPIO.output(11,False)

GPIO.cleanup()

