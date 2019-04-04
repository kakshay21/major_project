import RPi.GPIO as GPIO

LED_PIN = 32

def turnOn(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(LED_PIN, 1)
    return HttpResponse('')

def turnOff(request):
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(LED_PIN, 0)
    Return HttpResponse('')