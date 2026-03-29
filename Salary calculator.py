BS = float(input("Enter your Salary: "))#Base Salary
DA = BS*0.70 #Dearness Allowance
TA = BS*0.30 #Travel Allowance
HRA = BS*0.10 #House Rent Allowance
GrossSalary = BS+DA+TA+HRA 
print(f"Your Gross Salary is {GrossSalary}")