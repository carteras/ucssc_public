# Create a Function that calculates the surface area and volume of a Cylinder using the radius and height:

# Examples:
# Cylinder(2, 3, "surface_area") --> 62.8
# Volume(6, 4, "volume") --> 452.39

def Cylinder(Radius, Height, Calculation):
  Radius = float(Radius)
  Height = float(Height)
  pi = 22/7

  if Calculation == 'surface_area':
    return (2 * pi * Radius * Height) + (2 * pi * Radius * Radius)

  if Calculation == 'volume':
    return pi * Radius * Radius * Height

print(Cylinder(input(), input(), input()))