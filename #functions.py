#functions
number = int(input("ENTER A NUMBER: "))

if number <= 1:
    print("Neither Prime Nor Composite")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("PRIME NUMBER")
    else:
        print("COMPOSITE NUMBER")