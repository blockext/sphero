from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *

from blockext import *

import sphero

__version__ = '0.2'

class Sphero:
    def __init__(self):
        self.robot = sphero.Sphero()
        self.robot.connect()
        self.name = self.robot.get_bluetooth_info().name
        
    """def _is_connected(self):
        try:
            self.robot.get_bluetooth_info()
        except:
            self.robot = False
        
        if not self.robot:
            try:
                self.robot.connect()
                self.name = self.robot.get_bluetooth_info().name
            except:
                pass
            return bool(self.robot)"""
    
    def _problem(self):
        if not self.robot:
            return "Your Sphero is not connected"
    
    def _on_reset(self):
        self.robot.roll(0,0)
    def get_sphero_name(self):
        return self.name
    
    def set_sphero_name(self, name):
        self.name = name
        self.robot.set_device_name(name)
        
    def roll_sphero(self, power, heading):
        self.robot.roll(power*2.55, heading)
        
    """def set_sphero_color(self, r, g, b):
        self.robot.set_rgb(r,g,b)"""
    

descriptor = Descriptor(
    name = "Orbotix Sphero",
    port = 7575,
    blocks = [
        Block('roll_sphero', 'command', 'roll Sphero %n percent speed at %n degrees', defaults=[100,0]),
        Block('get_sphero_name', 'reporter', 'get Sphero name'),
        Block('set_sphero_name', 'command', 'set Sphero name to %s', defaults=['Rob Orb'])
        
    ]
)

extension = Extension(Sphero, descriptor)

if __name__ == '__main__':
    extension.run_forever(debug=True)