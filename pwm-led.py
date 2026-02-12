import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 100)
duty = 0.0
pwm.start (duty)

while 1:
    pwm.ChangeDutyCycle(duty)
    duty = (duty+1) % 100
    time.sleep(0.05)