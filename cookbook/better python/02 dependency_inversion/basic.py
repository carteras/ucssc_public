class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print('the light is on...')

    def turn_off(self):
        print('the light is off...')

class ElectricPowerSwitch:
    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True

foo = LightBulb()
switch = ElectricPowerSwitch(foo)
switch.press()
switch.press()