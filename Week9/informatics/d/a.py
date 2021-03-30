n = int(input())
ar = [int(i) for i in input().split()][::2]

for i in ar:
    print(i, end = ' ')