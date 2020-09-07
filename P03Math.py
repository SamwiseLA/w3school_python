# Math Functions
# https://www.w3schools.com/python/module_math.asp

# min/max -> Minimum and Maximum is List
x = min(5, 10, 25)
y = max(5, 10, 25)
z = min("Donut", "Bomb", "a", "A", "0")
z_max = max("A", "a", "0")
z_min = min("A", "a")

print(f"Min: {x} Max: {y}")
print(f"Min Alpha: {z}")
print("<------>")
print(f"Min Alpha: {z_min}")
print(f"Max Alpha: {z_max}")
print("")

# abs -> Absolute
x = -5
y = abs(x)

print(f"Reg: {x} Absolute: {y}")

# pos -> to the power of
x = 5
y = 4

z = pow(x, y)
print(f"{x} to the Power of: {y} = {z}")
# also this...
print(f"**: works the same as POW(): {x**y}")

import math  # More Math Functions


# math. - sqrt -> Gives the square root...
y = 144
x = math.sqrt(y)

print(f"\n{x} is the Square Root of {y}.")

# Ceil & floor -> rounds down or up to the nearest integer

a = 1.4  # Floating Point #
x = math.ceil(a)
y = math.floor(a)

print(f"\nCeiling of {a} is: {x}\nFloor   of {a} is: {y}") # returns 2

# Pi

x = math.pi
print(f"\npi is: {x}")
