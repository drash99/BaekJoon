import math

start = int(input())
end = int(input())

def isSq(num):
    if(int(math.sqrt(num))**2 == num):
        return True
    else:
        return False

res = []
for i in range(start, end+1):
    if isSq(i):
        res.append(i)

if(len(res)>0):
    print(sum(res))
    print(res[0])
else:
    print(-1)