import matplotlib.pyplot as plot 
import math as math


def f(x):
    return(math.sin(x))

xs = list(range(-5, 6))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()