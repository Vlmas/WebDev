n = int(input())
ar = [int(i) for i in input().split()]

ar.sort()
cnt = 0

mx = ar[len(ar) - 1]

for i in ar:
    if i == mx:
        cnt += 1

for i in range(cnt):
    ar.pop()

print(ar[len(ar) - 1])