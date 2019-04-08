import RPi.GPIO as GPIO


def turn_on(LED_PIN, status):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    if status:
        GPIO.output(LED_PIN, 1)
    else:
        GPIO.output(LED_PIN, 0)
