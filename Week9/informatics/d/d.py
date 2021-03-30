n = int(input())
ar = [int(i) for i in input().split()]
cnt = 0

for i in range(len(ar) - 1):
    if(ar[i] < ar[i + 1]):
        cnt += 1

print(cnt)