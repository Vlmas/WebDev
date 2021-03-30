n = input()[::-1]
res = 0

for i in range(len(n)):
    res += int(n[i]) * (2 ** i)

print(res)