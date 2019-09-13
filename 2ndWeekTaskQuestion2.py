# 7380
# Zaheer Irshad

"""
Write a program for restaurant to calculate tip for a bill

Hints
    bill = #Input number
    tip for a bill will be 1.5% of bill
"""

bill = float(input("Your Bill is\n"))

tip = (bill * 1.5)/100

print("Tip against your bill is :",tip)
total = bill + tip #optional

print("Your total bill including Tip is :",total)#optional