import heapq
import sys
input = sys.stdin.readline


def func():
    n = int(input())
    inputs = list(map(int,input().split()))
    for _ in range(n//10):
        inputs.extend(map(int,input().split()))
    cur = inputs[0]
    sml = []
    lge = []
    
    ans = [cur]
    for i in range(n-1):
        ne = inputs[i+1]
        if ne >= cur:
            if len(lge)-len(sml) == 1:
                heapq.heappush(sml, -cur)
                heapq.heappush(lge, ne)
                cur = heapq.heappop(lge)
            else:
                heapq.heappush(lge, ne)
        else:
            if len(sml) == len(lge):
                heapq.heappush(lge, cur)
                heapq.heappush(sml, -ne)
                cur = -heapq.heappop(sml)
            else:
                heapq.heappush(sml,-ne)
        if i%2==1:
            ans.append(cur)
    print(len(ans))
    print(' '.join(map(str, ans[:10])))
    for i in range(len(ans)//10):
        print(' '.join(map(str, ans[(i+1)*10:(i+2)*10])))

for _ in range(int(input())):
    func()