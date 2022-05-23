def convert(lst: list) -> int:
    length = len(lst)
    total = 0
    for i in range(length):
        total += lst[i] * 10**(length - (i+1))

    return total


print(convert([1, 2, 3, 4]))
