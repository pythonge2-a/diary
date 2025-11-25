import pint 
ureg = pint.UnitRegistry()

def convert_liter_to_gallon(liters):
    """Convert liters to gallons."""
    gallons = (liters * ureg.liter).to(ureg.gallon)
    return gallons.magnitude
