# 7380
# Zaheer Irshad
"""
Check grade of a student from result.
> 90 -> A grade
> 80 -> B grade
> 65 -> C grade
> 50 -> D grade
<= 50 -> F grade
"""
marks = float(input("Enter your marks\n"))

if marks >= 0 and marks <= 50:
    print("Your Grade is 'F'")
elif marks >50 and marks <= 65:
    print("Your Grade is 'D'")
elif marks >65 and marks <= 80:
    print("Your Grade is 'C'")
elif marks >80 and marks <= 90:
    print("Your Grade is 'B'")
elif marks >90 and marks <= 100:
    print("Your Grade is 'A'")
else:
    print("Please Enter the Valid NUMBER in range between '0 to 100'")