n = int(input())

i = 1

while i <= n:
    if int((i ** (1/2))) * int((i ** (1/2))) == i:
        print(i)
    i += 1