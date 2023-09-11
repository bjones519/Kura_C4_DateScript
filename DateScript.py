
#User inputs who is on the date with thm
from time import sleep


date_name = input ("Who are you going on a date with? ")
date_location = input("Where are you going on your date? ")

print("Welcome to your date with " + date_name + " at " + date_location)
#User inputs their budget for the date

#budget = input("What is your budget? $")

sleep(2)
#User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)

menu = {
    "Steak with Mashed Potatoes": 45, 
    "Tacos": 20, 
    "Lobster": 40, 
    "Chicken Alfredo": 30,
    "Coke": 5, 
    "Margarita": 15, 
    "Cosmopolitan": 16, 
    "Lemon Drop": 14 
    }

print(f"Here is the memu for tonight: {menu}")


#Script tells the user how much money they have left after each order.

def placeOrder(budget):
    
    while True:
        order = input("Enter your order: ")
        
        if order == 'done':
            return budget
        
        if order not in menu :
            print("Invalid item. Please choose from the menu.")
            continue

        orderPrice = menu[order]

        if budget < orderPrice:
            print(f"Sorry, you don't have enough in your budget for {order}.")
        else:
            budget -= orderPrice
            print(f"You ordered {order}. Remaining budget: ${budget}")
    
    return budget

personalBudget = int(input("What is your budget for this date? "))
dateBudget = placeOrder(personalBudget)
budgetRemaining = dateBudget


#At the end of the date user must agree to pay the bill and then their final budget is shown to them.
print("The Date is over")
payBill= input("Will you be paying the bill? ")

if payBill == "yes":
    print(f"You will be getting a second date! You also have ${budgetRemaining} left in your budget.")
else:
    print("There will not be a second date :(")
  
