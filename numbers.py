def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0:
        leap = True
    elif year % 100 != 0:
        leap = False

    return leap


year = 2100
print(is_leap(year))
