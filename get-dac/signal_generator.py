import numpy 
import time
import numpy 

def get_sin_wave_amplitude(freq, time):
    return (numpy.sin(2 * 3.14 * freq * time) + 1)/2

def get_triangle_amplitude(freq, time):
    period = 1 / freq
    time %= period
    if time < period /2 :
        return time / (period / 2)
    else:
        time %= period/ 2
        return 1 - time / (period / 2)
        


def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)