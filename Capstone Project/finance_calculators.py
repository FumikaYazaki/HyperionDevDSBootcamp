import math

#investment
def calculate_investment():
    deposit = int(input("Enter the amount of money that you are depositing."))
    interest_rate = int(input("Enter the interest rate (as a percentage).")) 
    years = int(input("Enter the number of years you plan on investing."))
    #choose interest type
    print("Do you want 'simple' or 'compound' interest?")
    interest_type = input().lower()

    #Interest calculation
    if interest_type == "simple":
        total_amount = deposit * (1 + interest_rate * years)
    elif interest_type == "compound":
        total_amount = deposit * math.pow((1 + (interest_rate / 100)), years)
    else:
        print("Please enter 'simple' or 'compund.")
    
    print(f"After", years, "years of", interest_type, "interest at a rate of", interest_rate, ", you will earn", round(total_amount, 2), "in total.")

       
#bond
def calculate_bond():
    present_value = int(input("Enter the present value of the hourse. e.g.100000"))
    interest_rate = int(input("Enter the interest rate. e.g.7"))
    months = int(input("Enter the number of months you plan to take to repay the bond. e.g.120"))

    interest_rate = (interest_rate / 100) / 12

    #calculation
    repayment = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-months))

    print(f"You will have to repay", round(repayment, 2), "each month.")

#Ask user to choose an option.
print("investment - to calculate the amount of tinterest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("Enter either 'investment' or 'bond' from the menu above to proceed:")
user_choice = input().lower()

#calculation
if user_choice == "investment":
    calculate_investment()
elif user_choice == "bond":
    calculate_bond()
else:
    print("Please enter either 'investment' or 'bond'.")


    
 
