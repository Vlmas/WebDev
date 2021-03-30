def min_among_four(a, b, c, d):
    return min(a, b, c, d)

ar = [int(i) for i in input().split()]

print(min_among_four(ar[0], ar[1], ar[2], ar[3]))