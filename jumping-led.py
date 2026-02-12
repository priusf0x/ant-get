import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

meow = [24,22,23,27,17,25,12,16]

GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

while 1:
    for i in meow:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

    for i in reversed(meow):
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)