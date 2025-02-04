class SmartDevice:
    def __init__(self, name, status=False):
        self.name = name
        self.status = status

    def turn_on(self):
        '''
        sets the status of the Device to on
        '''
        self.status = True
        
    def turn_off(self):
        '''
        sets the status of the Device to off
        '''
        self.status = False
        
    def __str__(self):
        '''
        if the device status is true, it will return the name of the device and "on"
        if the device status is false, it will return the name of the device and "off"
        '''
        if self.status == True:
            return f'{self.name}: ON'
        else:
            return f'{self.name}: OFF'
        

class Light(SmartDevice):
    def __init__(self, name, status=False, brightness=100):
        super().__init__(name, status=False)
        self.brightness = brightness

    def adjust_brightness(self, level):
        '''
        changes the level of brightness to whatever the input is
        '''
        self.brightness = level

    def __str__(self):
        '''
        if the device status is true, it will return the name of the device and "on", and then returns the brightness
        if the device status is false, it will return the name of the device and "off", and then returns the brightness
        '''
        if self.status == True:
            return f'{self.name}: ON, Brightness: {self.brightness}'
        else:
            return f'{self.name}: OFF, Brightness: {self.brightness}'
        

class Thermostat(SmartDevice):
    def __init__(self, name,  status=False, temperature=65.0):
        super().__init__(name, status=False)
        self.temperature = temperature

    def adjust_temperature(self, temp):
        '''
        check the temperature and if it is within the preset limits,
        will change the temperature to the input temp
        '''
        if self._check_temperature_limits(temp) == True:
            self.temperature = temp
        
    def __str__(self):
        '''
        if the device status is true, it will return the name of the device and "on", and then returns the temperature
        if the device status is false, it will return the name of the device and "off", and then returns the temperature 
        '''
        if self.status == True:
            return f'{self.name}: ON, Temperature: {self.temperature}'
        else:
            return f'{self.name}: OFF, Temperature: {self.temperature}'
        
    def _check_temperature_limits(self, temp):
        '''
        checks if the temperature is between 80 and 55, if it is it returns
        true, if not returns false
        '''
        if temp <= 80 and temp >= 55:
            return True
        else:
            return False
        

class Speaker(SmartDevice):
    def __init__(self, name, status=False, volume=3):
        super().__init__(name, status=False)
        self.volume = volume

    def increase_volume(self):
        '''
        if volume is under ten, increases by one
        '''
        if self.volume < 10:
            self.volume += 1
        
    def decrease_volume(self):
        '''
        if volume is over 1, decreases by one
        '''
        if self.volume > 1:
            self.volume -= 1
        
    def __str__(self):
        '''
        if the device status is true, it will return the name of the device and "on", and then returns volume
        if the device status is false, it will return the name of the device and "off", and then returns volume
        '''
        if self.status == True:
            return f'{self.name}: ON, Volume: {self.volume}'
        else:
            return f'{self.name}: OFF, Volume: {self.volume}'
        

class SmartHome():
    def __init__(self, devices=()):
        self.devices = [i for i in devices]

    def __add__(self, other):
        ''' 
        checks if the input is an instance, if it is it appends to the device list
        '''
        if isinstance(other, SmartDevice):
            self.devices.append(other)
            return self
        

    def turn_off_all(self):
        '''
        sets all devices status to false
        '''
        for i in self.devices:
            i.status = False
        

    def __str__(self):
        '''
        eturns all devices and if the are on or off, and their respective status, ex. 
        speakers volume
        '''
        return f'{self.devices}'
    
