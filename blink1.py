import RPi.GPIO as gpio
from flask import Flask

app=Flask(__name__)
gpio.setmode(gpio.bcm)

pins = {
    3: {'name': 'GPIO 02', 'state': gpio.LOW},
    5: {'name': 'GPIO 03', 'state': gpio.LOW}
    }

for pin in pins:
    gpio.setup(pin, gpio.OUT)
    gpio.setup(pin, gpio.LOW)
