import heapq
n, k= map(int, input().split())

a = list(map(int, input().split()))
pq = []

ans = []
for i in a:
    if len(pq) == k+1:
        ans.append(heapq.heappop(pq))
    heapq.heappush(pq, i)

for _ in range(len(pq)):
    ans.append(heapq.heappop(pq))



print(' '.join(map(str, ans)))