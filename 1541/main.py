raw = input()


pos = raw.split('-')[0]
neg = raw[len(pos)+1:]

possum = sum(map(int, pos.split('+')))
negsum = 0
for i in neg.split('+'):
    for j in i.split('-'):
        if j.isdigit():
            negsum+=int(j)

print(possum-negsum)