def xor(x, y):
    return (not x and y) or (x and not y)

ar = [int(i) for i in input().split()]

print(1 if xor(ar[0], ar[1]) else 0)