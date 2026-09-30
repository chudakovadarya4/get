import time
import numpy as np

def get_sin_wave_amplitude(freq, t):
    return (np.sin(2 * np.pi * freq * t) + 1.0) / 2.0

def get_triangle_wave_amplitude(freq, t):
    period = 1.0 / freq
    phase = (t % period) / period
    
    if phase < 0.5:
        return 2.0 * phase
    else:
        return 2.0 * (1.0 - phase)

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)