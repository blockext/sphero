from __future__ import division

import time

import blockext
from blockext import *

import sphero



@command("stop Sphero")
def stop_sphero():
    s.stop()

@command("roll %n percent speed at %n degrees")
def roll(speed, heading):
    s.roll(speed * 2.55, heading)

@command("set color r: %n g: %n b: %n")
def set_color(r, g, b):
    s.set_rgb(r,g,b)

@command("set Sphero name to %s")
def set_name(name):
    s.set_device_name(name)

@reporter("get Sphero name")
def get_name():
    s.get_device_name()

@reset
def reset_sphero():
    s.stop()

port = raw_input('What port is your Sphero on?')
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
