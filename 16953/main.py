a, b = map(int, input().split())

step = 0
ans = -1
current = [a]
isFin = False
if a == b:
    isFin = True

while not isFin:
    tmp = []
    step +=1
    isFin = True
    for i in current:
        if 2*i <= b:
            tmp.append(2*i)
        if 10*i+1 <= b:
            tmp.append(10*i+1)
    for i in tmp:
        if i < b:
            isFin = False
    if b in tmp:
        isFin = True
        ans = step+1
    current = tmp
    
print(ans)
