menu = ["coffee", "latte", "espresso", "milk"]

stock_dict = {"coffee": 10, "latte": 20, "espresso": 30, "milk": 40}
price_dict = {"coffee": 10, "latte": 20, "espresso": 30, "milk": 40}

total_stock_value = 0
for item in menu:
    item_value = (stock_dict[item]*price_dict[item])
    total_stock_value += item_value

print(total_stock_value)