import RPi.GPIO as GPIO
import time

TILT_SENSOR_PIN = 21
LED1_PIN = 17
LED2_PIN = 27
LED3_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(TILT_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)

start_time = None

try:
    while True:
        tilt_state = GPIO.input(TILT_SENSOR_PIN)

        if tilt_state == GPIO.LOW:
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time >= 3:
                GPIO.output(LED1_PIN, GPIO.LOW)
                GPIO.output(LED2_PIN, GPIO.LOW)
                GPIO.output(LED3_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED1_PIN, GPIO.LOW)
                GPIO.output(LED2_PIN, GPIO.HIGH)
                GPIO.output(LED3_PIN, GPIO.LOW)
        else:
            start_time = None
            GPIO.output(LED1_PIN, GPIO.HIGH)
            GPIO.output(LED2_PIN, GPIO.LOW)
            GPIO.output(LED3_PIN, GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()