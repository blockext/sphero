from __future__ import division

import time

import blockext
from blockext import *

import sphero



@command("stop Sphero")
def stop_sphero():
    s.roll(0, 0)

@command("roll %n percent speed at %n degrees")
def roll(speed, heading):
    s.roll(speed * 2.55, heading)

menu("onOff", ["on", "off"])
@command("turn stabilization %m.onOff")
def set_stability(onOff="on"):
	if onOff == "on":
	    s.set_stabilization(1)
	else:
		s.set_stabilization(0)

@command("set color r: %n g: %n b: %n")
def set_color(r, g, b):
    s.set_rgb(r, g, b)

menu("onOff", ["on", "off"])
@command("turn back LED %m.onOff")
def back_led(onOff="on"):
	if onOff == "on":
		s.set_back_led_output(255)
	else:
		s.set_back_led_output(0)

@command("set Sphero name to %s")
def set_name(name):
    s.set_device_name(name)

@reporter("get Sphero name")
def get_name():
    return s.get_bluetooth_info().name

@reset
def reset_sphero():
    s.stop(0, 0)



# TODO find the Sphero automatically
port = raw_input("What port is your Sphero on? ")
s = sphero.Sphero(port)
s.connect()
s.set_back_led_output(255)
s.set_stabilization(0)
print "Turn the Sphero until the blue light points toward you"
time.sleep(5)
s.set_heading(0)
s.set_back_led_output(0)
s.set_stabilization(1)

blockext.run("Orbotix Sphero", "sphero", 7575)
