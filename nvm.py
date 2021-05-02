import sys
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def waterMe(sec):
    GPIO.output(18, True)
    time.sleep(sec)


def main(): 

    print(sys.argv[1])
    waterMe(float(sys.argv[1]))
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, False)
    return 0


main()

