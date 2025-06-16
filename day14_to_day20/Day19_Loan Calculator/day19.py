print()
print("Loan Calculator")
print()
dollar = int(input("How much was the loan?"))
spook = dollar
years = int(input("For how many years do you have to pay the loan?"))
interestp = float(input("What is the interest rate (percentage)?"))
print()
for number in range(years):
    interest = dollar * interestp/100
    dollar = dollar + interest
    print("For year" ,number+1, "it is" ,round(dollar + interest , 2))
print()
