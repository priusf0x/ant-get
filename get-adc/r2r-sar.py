import r2r_adc as r2r
import time as t 
import adc_plot as plt 

if __name__ == "__main__":
    try:
        dac = r2r.R2R_ADC(3.3, 0.001)
        time_values = []
        voltage_values = []
        start_time = t.time()        
        duration = 3.0
        while (t.time() - start_time) < duration:
            voltage = dac.get_sar_voltage()
            time_values.append((t.time() - start_time)) 
            voltage_values.append(voltage)
        plt.plot_voltage_vs_time(time_values,voltage_values, 3.3)
        plt.plot_sampling_period_hist(time_values)
        
    finally:
        dac.deinit()