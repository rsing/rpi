import RPi.GPIO as gpio
import time
import random


def setup_pi(pins):
	gpio.setmode(gpio.BCM)
	for pin in pins:
		gpio.setup(pin, gpio.OUT)

def blink(pins):
	for pin in pins:
		time.sleep(random.random())
		gpio.output(pin, gpio.HIGH)
	for pin in pins:
		time.sleep(random.random())
		gpio.output(pin, gpio.LOW)

def cleanup():
	gpio.cleanup()


if __name__ == '__main__':
	pins = {
		4: {'name': 'GPIO 02', 'state': gpio.LOW},
		14: {'name': 'GPIO 03', 'state': gpio.LOW}
	}
	setup_pi(pins)
	try:
		while True:
			blink(pins)
	except KeyboardInterrupt:
		print "Interrupt!"
	finally:
		print "Cleaning up..."
		cleanup()
