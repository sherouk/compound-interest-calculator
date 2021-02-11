# This program determines whether a given year, inputted by the user,
# is a leap year
def leap_year():
    input_year = int(input("Enter a year: "))
    if input_year % 100 == 0 and input_year % 400 == 0:
        print(f"In {input_year}, February has 29 days.")
    elif input_year % 100 != 0 and input_year % 4 == 0:
        print(f"In {input_year}, February has 29 days.")
    else:
        print(f"In {input_year}, February has 28 days.")

leap_year()

print("This program was created by Sherouk Omara.")
