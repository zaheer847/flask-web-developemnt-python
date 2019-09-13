# 7380
# Zaheer Irshad

'''
Write a program to input a number from user and check if that number is odd or even

Hints:
    num = #Input number
    'num % 2' to check if it is even or odd
    use if-else statements
'''

num = int(input('Enter the Number\n'))
if num % 2 == 0:
    print(num,"is Even.")
else:
    print(num, "is Odd.")