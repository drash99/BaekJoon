n = int(input())
inraw = input().strip().split(' ')
A = []
for r in inraw:
    A.append(int(r))

dp = [0 for _ in range(n)]

          

for i in range(n):
    dp[i] += A[i]
    for j in range(i+1):
        if A[j] < A[i]:
            if dp[j]+A[i] > dp[i]:
                dp[i] = dp[j] + A[i]

print(max(dp))


