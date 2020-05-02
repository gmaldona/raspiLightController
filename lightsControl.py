import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

time.sleep(1)

while True:
    blink(17, 1)
    blink(27, 1)
    blink(22, 1)
    
def blink(pin, t):
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(t)
    