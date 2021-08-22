def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(5, 6, 7, 8, 9, 2))
