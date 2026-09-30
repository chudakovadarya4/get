import time
import r2r_dac as r2r
import signal_generator as sg

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], dynamic_range=3.183, verbose=False)
    start_time = time.time()

    while True:
        current_time = time.time() - start_time
        norm_val = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = norm_val * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    dac.deinit()