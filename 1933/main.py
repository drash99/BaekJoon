import sys
import heapq
import bisect

n = int(input())

leftsort = []
stops = []
current = []
passing = []
ans = ''
pos = 0
for _ in range(n):
    l, h, r = map(int, sys.stdin.readline().split())
    heapq.heappush(leftsort, (l,h,r))
    heapq.heappush(stops, l)
    heapq.heappush(stops, r)
while stops:
    befpos = pos
    pos = heapq.heappop(stops)
    if befpos != pos:
        if current:
            befh = current[-1]
        else:
            befh = 0
    if leftsort and leftsort[0][0] == pos:
        l, h, r = heapq.heappop(leftsort)
        heapq.heappush(passing, (r, h))
        bisect.insort(current, h)

    if passing and passing[0][0] == pos:
        r,h = heapq.heappop(passing)
        current.remove(h)
    
    if current:
        afth = current[-1]
    else:
        afth = 0
    
    if befh != afth and ((not stops) or (stops and stops[0] != pos)):
        ans += str(pos) + ' ' + str(afth) + ' '

print(ans)


