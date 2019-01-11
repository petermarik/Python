import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5,0)

try:
    while True:
        if (GPIO.input(16) == 1):
            GPIO.output(5,1)
        else:
            GPIO.output(5,1)
            time.sleep(0.1)
            GPIO.output(5,0)
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
