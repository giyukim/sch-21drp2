from vpython import *

'''
F = 2
m = 1
a = F / m
print(a)
'''

scala_factor = 5.0
r = 384400000
G = 6.67e-11 # floating point, gravitational constant

earth = sphere(
    pos = vec(0, 0, 0),
    radius = 5.0 * 6371000,
    texture = textures.earth
)
moon = sphere(
    pos = vec(r, 0, 0),
    radius = 5.0 * 1737000,
    color = color.white
)

# mass
earth.mass = 5.974e-24
moon.mass = 7.7347e-22

# gravitation
F = G * earth.mass * moon.mass / (r ** 2)
# F = G * m * a^2

earth.force = F
moon.force = -F

# Newton's Third law
print("earth.force =", earth.force, "N")
print("moon.force =", moon.force, "N")

# acceleration f=ma
earth.acc = F / earth.mass
moon.acc = F / moon.mass

print("earth.acc =", earth.acc, "m/s^2")
print("moon.acc =", moon.acc, "m/s^2")

