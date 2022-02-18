import math

for _ in range(int(input())):
    x, y = map(int ,input().split())
    ans = math.ceil(math.sqrt(y-x+2)-2)
    if (y-x-ans*(ans+1))//(ans+1) >= 1:
        ans1 = math.ceil((y-x-ans*(ans+1))/(ans+1))
    elif (y-x-ans*(ans+1))//(ans) >= 1:
        ans1 = math.ceil((y-x-ans*(ans+1))/(ans))
    elif ans > 1:
        ans1 = math.ceil((y-x-ans*(ans+1))/(ans-1))
    else:
        ans1 = 1

    print(ans*2+ans1)