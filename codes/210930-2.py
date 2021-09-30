from vpython import *
# Calc Vector

a = vec(1, 2, 3)
b = vec(-4, 5, 6)
c = a + b
d = a - b
a_vec = arrow(
    pos = vec(0, 0, 0),
    axis = a,
    shaftwidth = 0.1
)
b_vec = arrow(
    pos = a,
    axis = b,
    shaftwidth = 0.1
)

#add
c_vec = arrow(
    pos = vec(0, 0, 0),
    axis = c,
    shaftwidth = 0.1,
    color = color.red
)

a_vec2 = arrow(
    pos = vec(0, 0, 0),
    axis = a,
    shaftwidth = 0.1,
    color = color.yellow
)
b_vec2 = arrow(
    pos = vec(0, 0, 0),
    axis = b,
    shaftwidth = 0.1,
    color = color.yellow
)

#min
d_vec = arrow(
    pos = b,
    axis = d,
    shaftwidth = 0.1,
    color = color.blue
)