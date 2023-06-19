total = 0
count = 0
user_input = int(input("Please enter a number (-1 to stop)"))

#Loop structure
while user_input != -1:
    total += user_input
    count += 1
    user_input = int(input("Please enter a number (-1 to stop)"))

    if user_input == -1:
        break

average = float(total / count)
print(average)