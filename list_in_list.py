

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        first_n = []
        second_n = []
        first_n += [[name, score]]
        second_n += [score]
a = sorted(set(second_n))[1]
for name, score in sorted(first_n):
    if a == score:
        print(name)

#python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#a = python_students[0][0]
# grade_std = python_students[0][0]
# for stud in python_students:
#     if stud[0][0] <= grade_std:
#         grade_std = stud
#         print(stud)
#     for stud_num in stud:
#         if stud_num <= stud[1]:
#             stud_num = grade_std
#         print(grade_std)
    #if stud[1] <= 41:
       # grade_std.append(stud[0])
       # print(grade_std)
