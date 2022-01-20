inputraw = input().strip().split(' ')
scores = []
for i in inputraw:
    scores.append(int(i))
print(sum(scores)*100/(len(scores)*max(scores)))