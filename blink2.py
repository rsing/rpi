import RPi.GPIO as gpio
import time
import random
from flask import Flask, render_template, request

app=Flask(__name__)
gpio.setmode(gpio.BCM)

pins = {
	4: {'name': 'GPIO 02', 'state': gpio.LOW},
	14: {'name': 'GPIO 03', 'state': gpio.LOW}
	}

def setup_pi():
	print "Setting up LEDs.."
	for pin in pins:
		gpio.setup(pin, gpio.OUT)
		gpio.setup(pin, gpio.LOW)

# Set up flask to serve html
@app.route("/<my_pin>/<my_action>")
def pin_action(my_pin, my_action):
    if my_action.lower() == "off":
        gpio.output(my_pin, gpio.LOW)
    elif my_action.lower() == "on":
        gpio.output(my_pin, gpio.LOW)

@app.route("/gocrazy")
def crazy_action1():
    blink_uncontrollably(1.0)

@app.route("/goverycrazy")
def crazy_action2():
    blink_uncontrollably(10.0)

@app.route("/off")
def turn_off():
	gpio.cleanup()
	
# Blink uncontrollably
def blink_uncontrollably(delay_factor):
	try:
		while True:
			for pin in pins:
				time.sleep(random.random()/delay_factor)
				gpio.output(pin, gpio.HIGH)
			for pin in pins:
				time.sleep(random.random()/delay_factor)
				gpio.output(pin, gpio.LOW)
	except KeyboardInterrupt:
		print "Interrupt!"
	finally:
		gpio.cleanup()			

if __name__ == '__main__':
	setup_pi()	
	app.run(debug=True,host='0.0.0.0')
