import math

p = int(input())
b = int(input())
h = math.sqrt(p**2+b**2)
MC = h/2
C = math.atan(p/b)
MB = math.sqrt(b**2+MC**2-2*b*MC*math.cos(C))
print(str(round(math.degrees(math.asin(math.sin(C)*(MC/MB)))))+u'\N{DEGREE SIGN}')
