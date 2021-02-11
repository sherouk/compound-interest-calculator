# This program determines salary based on the 
# user inputted number of days

# Ask user to input the number of working days
print("This program will determine your salary ")
print("depending on how many days you've worked.")
days = int(input("How many days did you work?: "))

#Create table headings
print()
print("Days\tSalary")
print("----------")

# Define function to calculate salary
def user_salary ():
    for num in range(1, days + 1):
        if num == 1:
            salary = num * 100
            print(f"{num}\t${salary:,.2f}")
        else:
            salary = (salary * 2)
            print(f"{num}\t${salary:,.2f}")

user_salary()

print("This program was created by Sherouk Omara.")
