x = int(input())
d = int(input())
cnt = 0

for i in x.__str__():
    if(int(i) == d):
        cnt+=1

print(cnt)