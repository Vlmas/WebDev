n = int(input())
ar = [int(i) for i in input().split() if int(i) % 2 == 0]

for i in ar:
    print(i, end = ' ')