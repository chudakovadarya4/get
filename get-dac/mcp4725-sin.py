import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.3
signal_frequency = 10
sampling_frequency = 500

try:
    dac = mcp.MCP4725(5.0, 0x61, verbose=False)
    start_time = time.time()

    while True:
        current_time = time.time() - start_time
        normalized_val = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_val * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass
finally:
    dac.deinit()
