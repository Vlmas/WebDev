n = int(input())
ar = [int(i) for i in input().split()]

for i in range(len(ar) - 1):
    if((ar[i] > 0 and ar[i + 1] > 0) or (ar[i] < 0 and ar[i + 1] < 0) or ar[i] == ar[i + 1]):
        print('YES')
        break
else:
    print('NO')