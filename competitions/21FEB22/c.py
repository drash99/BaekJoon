n = int(input())

i = n
fromright = 0
while i >0:
    i >>= 1
    fromright +=1

ans = n
ans2 = 2**fromright -1 - n
if ans2:
    print(2)
    print(ans2)
    print(ans)
else:
    print(1)
    print(ans)