# This program determines the discounted costs of various 
# quantities of items based on user inputted volume.

# Asking for user to input the retail price, amount purchased, and discount amount
retail_price = float(input("Please enter the retail price of the item: "))
purchase_quantity = int(input("Please enter the number of items purchased: "))
user_input_discount = int(input("Please enter the discount amount as a whole number (ex: 10, 20, 30, etc.): "))

def calculate_total ():
    discount_amount = (retail_price * purchase_quantity) * (user_input_discount * .01)
    final_price = (retail_price * purchase_quantity) - discount_amount
    print(f"You purchased {purchase_quantity} items and received a {user_input_discount}% discount amounting to ${discount_amount:,.2f}. Your final price is ${final_price:,.2f}.")

calculate_total()

print("This program was created by Sherouk Omara.")
