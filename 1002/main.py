import math
t = int(input())


def chkd(a,b,c):
    if b*b-4*a*c >= -0.001:
        return False
    else:
        return True



for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    ans = 0
    if x1==x2 and y1==y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif (x2-x1)**2+(y2-y1)**2 > (r1+r2)**2:
        print(0)
    
    elif (x2-x1)**2+(y2-y1)**2 == (r1+r2)**2:
        print(1)
    
    elif (x2-x1)**2+(y2-y1)**2 < (r1-r2)**2:
        print(0)
    
    elif (x2-x1)**2+(y2-y1)**2 == (r1-r2)**2:
        print(1)    
    else:
        print(2)
        