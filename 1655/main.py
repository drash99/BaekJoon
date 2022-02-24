import heapq
import sys
input = sys.stdin.readline

n = int(input())

cur = int(input())
sml = []
lge = []
print(cur)
for _ in range(n-1):
    ne = int(input())
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
    print(cur, sml, lge)

        