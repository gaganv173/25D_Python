# Constants
FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5
OFFSET = 32

# Input
celcius_input = 20
fahrenheit_input = 85

# Conversion
c_to_f = (celcius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
f_to_c = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS

# Output
print(f'{celcius_input}°C == {c_to_f:.1f}F')    #.1f is a format specifier which limits decimal to 1 place
print(f'{fahrenheit_input}F == {f_to_c:.1f}°C')

