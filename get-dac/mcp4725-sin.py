import mcp4725_driver as mcp
import signal_generator as sg
import time 

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 500


if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(12, sampling_frequency, 3.3)
        time = 0
        
        while True:
            time += 1/ sampling_frequency
            dac.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, time))
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()
