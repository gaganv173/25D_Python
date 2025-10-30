# Miles to km converter

# Constants
mil_in_km = 1.609344

# Input
Miles = 20
KMs = 30

# Conversion
mil_to_km = Miles * mil_in_km
km_to_mil = KMs / mil_in_km

# Output
print(f'{Miles} Miles == {mil_to_km:.2f} Kilometers')
print(f'{KMs} Kilometers == {km_to_mil:.2f} Miles')