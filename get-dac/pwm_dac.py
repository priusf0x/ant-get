import RPi.GPIO as GPIO
import time 


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dynamic_range=3

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(gpio_pin, pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.183, True)
        
        while True:
            voltage = float(input("Введите напряжение в Вольтах: "))
            dac.set_voltage(voltage)

    finally:
        dac.deinit()
