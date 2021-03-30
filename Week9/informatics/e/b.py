def power(a, n):
    res = 1

    for _ in range(int(n)):
        res *= a
    
    return res

ar = [float(i) for i in input().split()]

print(power(ar[0], ar[1]))