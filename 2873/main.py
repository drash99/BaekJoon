n,m=map(int, input().split())

field = []

for _ in range(n):
    field.append(list(map(int,input().split())))




ans = ''
if n%2==1:
    tmp = []
    for i in range(n):
        anstmp = ''
        for j in range(m-1):
            if i%2==0:
                anstmp+='R'
            else:
                anstmp+='L'
        tmp.append(anstmp)
    ans = 'D'.join(tmp)
elif m%2==1:
    tmp = []
    for i in range(m):
        anstmp = ''
        for j in range(n-1):
            if i%2==0:
                anstmp+='D'
            else:
                anstmp+='U'
        tmp.append(anstmp)
    ans = 'R'.join(tmp)

else:
    findmin = []
    for idxi,i in enumerate(field):
        for idxj, j in enumerate(i):
            if (idxi+idxj)%2 == 1:
                findmin.append((j, (idxi,idxj)))
    #print(findmin)
    avoid = min(findmin)
    avoidx = avoid[1][1]
    avoidy = avoid[1][0]
    ansfront = ''
    ansrear = ''
    for i in range((avoidx//2)*2):
        if i%2==0:
            ansfront+='D'*(n-1)
        else:
            ansfront+='U'*(n-1)
        ansfront+='R'
    for i in range(((m-1-avoidx)//2)*2):
        ansrear+='R'
        if i%2==0:
            ansrear+='U'*(n-1)
        else:
            ansrear+='D'*(n-1)
  
    #print(ansfront, ansrear)
    for i in range(avoidy//2):
        ansfront += 'RDLD'
    for i in range((n-1-avoidy)//2):
        ansrear= 'DLDR'+ansrear
    if avoidx%2==0:
        ans = ansfront+'RD'+ansrear
    else:
        ans = ansfront + 'DR'+ansrear

print(ans)