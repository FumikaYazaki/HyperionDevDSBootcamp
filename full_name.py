import math

def calculate_investment():
    deposit = float(input("Enter the amount of money you would like to deposit: "))
    interest_rate = float(input("Enter the interest rate as a percentage (%): "))
    years = int(input("Enter the number of years you plan to invest for: "))

    # calculate the total amount after interest
    total_amount = deposit * math.pow((1 + (interest_rate / 100)), years)
    interest_earned = total_amount - deposit

    # round the results to 2 decimal places
    total_amount = round(total_amount, 2)
    interest_earned = round(interest_earned, 2)

    # display the results
    print(f"Total amount after {years} years: R{total_amount}")
    print(f"Interest earned: R{interest_earned}")

def calculate_bond():
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate as a percentage (%): "))
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    # calculate the monthly repayment amount
    interest_rate = (interest_rate / 100) / 12
    repayment_amount = present_value * ((interest_rate * math.pow((1 + interest_rate), months)) / ((math.pow((1 + interest_rate), months)) - 1))

    # round the result to 2 decimal places
    repayment_amount = round(repayment_amount, 2)

    # display the result
    print(f"Monthly bond repayment amount: R{repayment_amount}")

# display the menu and get the user's choice
print("Enter 'investment' or 'bond' to proceed:")
choice = input().lower()

# calculate based on user's choice
if choice == "investment":
    calculate_investment()
elif choice == "bond":
    calculate_bond()
else:
    print("Invalid choice. Please enter either 'investment' or 'bond'.")