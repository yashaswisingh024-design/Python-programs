
# Looping statement - Factorial

n = int(input("Enter a number: "))
factorial = 1

if n < 0:
    print("Factorial is not defined for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial of the given number is:", factorial)