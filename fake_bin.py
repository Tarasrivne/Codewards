def fake_bin(x):
    binary_x = ''
    for number in x:                        # йде ітерація по fake_bin('178923')
        if int(number) < 5:                 # переводить строку в чило та порівнює з 5
            binary_x += '0'                 # якщо менше 5 додає в пустий список binary_x 0
        else:
            binary_x += '1'                 # якщо більше 5 додає в пустий список binary_x 1
    return binary_x
a = fake_bin('178923')
print(a)