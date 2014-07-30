from blockext import *
import sphero


class Sphero:
    def __init__(self):
        self.bot = sphero.Sphero()
        self.bot.connect()
        self.name = self.bot.get_bluetooth_info().name
        
    """def _is_connected(self):
        try:
            self.bot.get_bluetooth_info()
        except:
            self.bot = False
        
        if not self.bot:
            try:
                self.bot.connect()
                self.name = self.bot.get_bluetooth_info().name
            except:
                pass
            return bool(self.bot)"""
    
    def _problem(self):
        if not self.bot:
            return "Your Sphero is not connected"
    
    def _on_reset(self):
        self.bot.roll(0,0)
    def get_sphero_name(self):
        return self.name
    
    def set_sphero_name(self, name):
        self.name = name
        self.bot.set_device_name(name)
        
    def roll_sphero(self, power, heading):
        self.bot.roll(power*2.55, heading)
        
    """def set_sphero_color(self, r, g, b):
        self.bot.set_rgb(r,g,b)"""
    

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