x = int(input())
still_zeros = True

for i in reversed(x.__str__()):
    if i == '0' and still_zeros:
        continue
    elif i != '0' and still_zeros:
        still_zeros = False
    print(i, end = '') 