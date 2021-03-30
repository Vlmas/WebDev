n = int(input())
ar = []
min_score = 1e9
second_min_score = 1e9

for i in range(n):
    name = input()
    score = float(input())
    if score < min_score:
        second_min_score = min_score
        min_score = score
    elif score < second_min_score and score != min_score:
        second_min_score = score
    ar.append([name, score])

ar.sort()

for i in range(n):
    if ar[i][1] == second_min_score:
        print(ar[i][0])