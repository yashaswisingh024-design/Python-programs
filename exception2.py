try:
	b=int(input("Enter first number: "))
	y=int(input("Enter second number: "))
	result=b/y
	print("Division is:", result)
except Exception as e:
	print("Your error is",e)
finally:
	print('This will accept Inspite of error or no error')