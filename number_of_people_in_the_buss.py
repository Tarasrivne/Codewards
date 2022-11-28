def number(arr):

    people_in = 0
    people_out = 0
    for stops in arr:
        people_in += stops[0]
        people_out += stops[1]
    return people_in - people_out

people = number([[10,0],[3,5],[5,8]])
print(people)
