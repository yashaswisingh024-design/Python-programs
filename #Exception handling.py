#Exception handling
try:

	a=int(input("Enter First number:"))

	h=int(input('Enter second number:'))

	result=a/h

	print("Division is:", result)

except ZeroDivisionError:

	print("Cannot divide by zero")

except ValueError:

	print("Enter number real value")

finally:

	print("This will accept inspite of error or no error")