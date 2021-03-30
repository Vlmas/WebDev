n = int(input())
cnt = 0

for i in range(n):
    t = int(input())
    cnt = cnt + 1 if t == 0 else cnt

print(cnt)