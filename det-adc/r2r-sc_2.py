import time
import adc_plot
import r2r_adc

voltage_values = []
time_values = []
duration = 3.0

try:
    adc = r2r_adc.R2R_ADC(3.3, compare_time=0.0001)
    start_time = time.time()

    while (time.time() - start_time) < duration:
        current_time = time.time() - start_time
        voltage = adc.get_sc_voltage()
        time_values.append(current_time)
        voltage_values.append(voltage)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
