import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO.setup(9, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

i = 0

while 1:
    if (GPIO.input(9)):
        i+=1
        time.sleep(0.2)

    GPIO.output(24,   i%2)
    GPIO.output(22, (i % 4) // 2)
    GPIO.output(23, (i % 8) // 4)
    GPIO.output(27, (i % 16) // 8)
    GPIO.output(17, (i % 32) // 16)
    GPIO.output(25, (i % 64) // 32)
    GPIO.output(5,(i % 128) // 64)
    GPIO.output(16,(i % 256) // 128)
