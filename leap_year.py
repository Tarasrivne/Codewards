def is_leap(year):
    leap = False

    # Write your logic here

    if year % 400 != 0:
        leap = True
    elif year % 4 != 0:
        leap = True
    elif year % 100 == 0:
        leap = False


    return leap


assert is_leap(2100) is True, "2000 is outputting True"
assert is_leap(2011) is False, "2011 is outputting False"
assert is_leap(2003) is False, "2023 is outputting False"
