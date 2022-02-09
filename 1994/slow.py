n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

dp = dict() # fi, d : (len)

ones = []

ans = 0

for i in A:
    tmp = dict()
    for j in dp.keys():
        if i == j[0] + j[1]:
            tmp[(i,j[1])] = dp[j]+1
        else:
            tmp[j] = dp[j]

    for j in ones:
        if not (i,i-j) in tmp.keys():
            tmp[(i,i-j)] = 2
    ones.append(i)
    dp = tmp

if len(dp.values()) > 0:
    print(max(dp.values()))
else:
    print(1)


