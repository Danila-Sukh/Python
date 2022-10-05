d = int(input('Введите натуральное число: '))


def primfacs(d):
    i = 2
    primfac = []
    while i * i <= d:
        while d % i == 0:
            primfac.append(i)
            d //= i
        i += 1
    if d > 1:
        primfac.append(d)
    return primfac


print(primfacs(d))
