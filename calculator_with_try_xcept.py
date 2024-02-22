print("Give me two  numbers and i will divide them")
print("Enter 'q' to quit")
while True:
    first_number = input("first number")
    if first_number == 'q':
        break
    second_number = input("your second number")
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by '0' ")
    else:
        print(result)