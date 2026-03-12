import mcp3021_driver as r2r
import time as t 
import adc_plot as plt 

if __name__ == "__main__":
    try:
        dac = r2r.MCP4725(5.2, False)
        time_values = []
        voltage_values = []
        start_time = t.time()        
        duration = 3.0
        while (t.time() - start_time) < duration:
            voltage = dac.get_voltage()
            time_values.append((t.time() - start_time)) 
            voltage_values.append(voltage)
        plt.plot_voltage_vs_time(time_values,voltage_values, 3.3)
        plt.plot_sampling_period_hist(time_values)
        
    finally:
        dac.deinit()