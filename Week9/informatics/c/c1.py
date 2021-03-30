a = int(input())
b = int(input())

for i in range(a, b + 1):
    if int((i ** (1/2))) * int((i ** (1/2))) == i:
        print(i, end = " ")