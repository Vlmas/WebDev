n = int(input())
cnt = 0

for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0 and i * i != n:
        cnt += 2
    elif n % i == 0 and i * i == n:
        cnt += 1

print(cnt)