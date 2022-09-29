float_number = input()
sum = 0
for i in float_number:
    if i != '.' and i != ',':
        sum += int(i)
print("Сумма цифр =", sum)
