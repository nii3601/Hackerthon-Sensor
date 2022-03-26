import RPi.GPIO as GPIO
from gpiozero import LightSensor
from time import sleep
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    INPUT_PIN = 16
    GPIO.setup(INPUT_PIN, GPIO.IN)
    reading = 0
    lastReading = 0
    volume = 0

    while (True):
        if (GPIO.input(INPUT_PIN) == 0):
            reading = 0
        else:
            reading = 1
        if (reading != lastReading):
            volume += 1.75
        lastReading = reading
        print(volume)

        sleep(0.01)

    return

if __name__ == '__main__':
    main()
