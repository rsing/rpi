import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

pins = {
    3: {'name': 'GPIO 02', 'state': gpio.LOW},
    2: {'name': 'GPIO 03', 'state': gpio.LOW}
    }

for pin in pins:
    gpio.setup(pin, gpio.OUT)
    gpio.setup(pin, gpio.LOW)
    gpio.output(pin, gpio.LOW)
