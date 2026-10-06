import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led = 26
light_sensor = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(light_sensor, GPIO.IN)

try:
    while True:
        sensor_state = GPIO.input(light_sensor)
        GPIO.output(led, not sensor_state)
        time.sleep(0.05)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
