for _ in range(int(input())):
    a,b=map(int, input().split())
    ans = pow(a,b,10)
    print(10 if ans==0 else ans)