import heapq
n = int(input())
a = map(int, input().split())
pq = []
for idx, i in enumerate(a):
    heapq.heappush(pq, (i, idx))

ans = [0 for _ in range(n)]
j = 0
while pq:
    i = heapq.heappop(pq)
    ans[i[1]] = j
    j+=1

print(' '.join(map(str, ans)))