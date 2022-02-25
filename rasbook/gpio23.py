import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print ("setup LED pin")

GPIO.setup(23,GPIO.OUT)
GPIO.output(23, False)

GPIO.output(23,True)

time.sleep(2)

GPIO.output(23,False)

GPIO.cleanup()

