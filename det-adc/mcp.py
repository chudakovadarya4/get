import time
import adc_plot
import mcp3021_driver

voltage_values = []
time_values = []
duration = 3.0

try:
    adc = mcp3021_driver.MCP3021(5.0)
    start_time = time.time()

    while (time.time() - start_time) < duration:
        current_time = time.time() - start_time
        voltage = adc.get_voltage()
        time_values.append(current_time)
        voltage_values.append(voltage)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)

finally:
    adc.deinit()
