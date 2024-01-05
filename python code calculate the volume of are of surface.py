Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... radius = float(input("Enter the radius of the sphere: "))
... 
... volume = (4/3) * math.pi * (radius**3)
... 
... surface_area = 4 * math.pi * (radius**2)
... print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")
... print(f"The surface area of the sphere with radius {radius} is: {surface_area:.2f}")
... 
