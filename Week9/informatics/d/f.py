n = int(input())
ar = [int(i) for i in input().split()]
cnt = 0

for i in range(1, len(ar) - 1):
    if(ar[i - 1] < ar[i] and ar[i + 1] < ar[i]):
        cnt += 1

print(cnt)