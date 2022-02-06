from math import ceil


d, p, q = map(int, input().split())

if p>q:
    l = p
    s = q
else:
    l = q
    s = p

if l%s == 0:
    print(s*ceil(d/s))
elif d%s == 0 or d%l == 0:
    print(d)
else:
    tmp = d%s
    tmp2 = l%s
    ans = tmp + s
    cur = 0
    for i in range(d//l+1):
        if ans > (tmp2*i-tmp)%s:
           cur = i
           ans = (tmp2*i-tmp)%s
    

    if ans > (tmp2*((d//l)+1)-tmp)%s and l*(d//l+1) < ans+d:
        print(l*(d//l+1))
    elif (l*i>ans+d):
        print(min(l*i,s*ceil(d/s)))
    else:
        print(ans+d)