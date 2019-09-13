# 7380
# Zaheer Irshad

""""
Write code for following scnerios

1. Computer area of circle by radius
r = ?
output should be area of circle. e.g
"Area of circle is: output"
"""
import math
# radius = r

r = float(input("Enter the radius: \n"))

# setting pi
p = math.pi
# Area a
a = p*r**2

#a = p*math.pow(r,2) # we can also use this
#print("Area of circle is: " + str(a))
print("Area of circle is: ", a)