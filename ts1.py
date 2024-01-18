import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = (b*b) - (4 * a * c)
sd = math.sqrt(d)
x1 = (0 - b - sd) / (2*a)
x2 = (0 - b + sd) / (2*a)

print(f'x1 = {x1}, x2 = {x2}')