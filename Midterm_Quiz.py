class TempConversion:
    def __init__(self, temp, unit):
        self.temp = temp
        self.unit = unit

    def to_celsius(self):
        if self.unit == 'F':
            return (self.temp - 32) * 5/9
        elif self.unit == 'K':
            return self.temp - 273.15
        else:
            return self.temp

    def to_fahrenheit(self):
        if self.unit == 'C':
            return (self.temp * 9/5) + 32
        elif self.unit == 'K':
            return (self.temp - 273.15) * 9/5 + 32
        else:
            return self.temp

    def to_kelvin(self):
        if self.unit == 'C':
            return self.temp + 273.15
        elif self.unit == 'F':
            return (self.temp + 459.67) * 5/9
        else:
            return self.temp

# get user input for temperature and unit
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C, F, K): ")

# create TempConversion object and convert to all units
tc = TempConversion(temp, unit)
celsius = tc.to_celsius()
fahrenheit = tc.to_fahrenheit()
kelvin = tc.to_kelvin()

# show conversions
print("{} {} is equal to {:.2f} C, {:.2f} F, and {:.2f} K.".format(temp, unit, celsius, fahrenheit, kelvin))
