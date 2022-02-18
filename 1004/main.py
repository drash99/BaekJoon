for _ in range(int(input())):
    x1,y1,x2,y2  = map(int,input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        cx,cy,r = map(int,input().split())
        disa = (cx-x1)**2+(cy-y1)**2
        disb = (cx-x2)**2+(cy-y2)**2
        if disa < r**2 and disb > r**2:
            ans+=1
        elif disa > r**2 and disb < r**2:
            ans+=1
    print(ans)
