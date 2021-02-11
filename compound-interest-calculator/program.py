# This program will calculate compound interest for a savings account
# based on the user's input of principal amount, annual interest rate, compound rate, and year

# Ask user to enter principal amount, interest rate, compound rate, 
# and number of years interest will accumulate
Principal = float(input("Please enter the amount of money you will deposit: "))
Rate = float(input("Please enter your annual interest rate: "))/100
compoundNum = int(input("Please enter the number of times per year the interest compounds: "))
Years = int(input("Please enter the number of years your account will be left to earn interest: "))

def interest_calculation():
  FinalAmt = (Principal * (1 + (Rate/compoundNum))**(compoundNum * Years))
  print("The amount of money that will be in your account after",Years,"years is $",(f'{FinalAmt:,.2f}'))

interest_calculation()

print("This program was written by Sherouk Omara")
