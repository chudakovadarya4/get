import time
import pwm_dac as pwm
import signal_generator as sg

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(gpio_pin=12, pwm_frequency=500, dynamic_range=3.290, verbose=False)
    start_time = time.time()

    while True:
        current_time = time.time() - start_time
        norm_val = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage = norm_val * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    dac.deinit()