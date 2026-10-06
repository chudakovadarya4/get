import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def get_triangle_wave_amplitude(freq, time):
    period = 1.0 / freq
    t = (time % period) / period
    if t < 0.5:
        return 2.0 * t
    else:
        return 2.0 * (1.0 - t)

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0 / sampling_frequency)
