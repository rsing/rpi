import RPi.GPIO as gpio
import time
from flask import Flask

app=Flask(__name__)
gpio.setmode(gpio.BCM)

pins = {
    3: {'name': 'GPIO 02', 'state': gpio.LOW},
    2: {'name': 'GPIO 03', 'state': gpio.LOW}
    }

for pin in pins:
    gpio.setup(pin, gpio.OUT)
    gpio.setup(pin, gpio.LOW)

for i in range(5):
    time.sleep(0.3)
    for pin in pins:
        gpio.output(pin, gpio.HIGH)
    time.sleep(0.3)
    for pin in pins:
        gpio.output(pin, gpio.LOW)
