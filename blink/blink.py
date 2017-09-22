import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

while(True):
    GPIO.output(10, True)
    GPIO.output(16, True)
    print("\LEDs are ON")
    time.sleep(1)
    GPIO.output(10, False)
    GPIO.output(16, False)
    print("\LEDs are OFF")
    time.sleep(1)

GPIO.cleanup()    