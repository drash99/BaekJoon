n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

dp = dict() # fi, d : (len)

ones = []

ans = 0

for i in A:
    tmp = []
    for j in dp.keys():
        if i == j[0] + j[1]:
            tmp.append(((i,j[1]),dp[j]+1))
    for j in tmp:
        if j[0] in dp.keys():
            dp[j[0]] = max(j[1], dp[j[0]])
        else:
            dp[j[0]] = j[1]
    for j in ones:
        if not (i,i-j) in dp.keys():
            dp[(i,i-j)] = 2
    ones.append(i)

if len(dp.values()) > 0:
    print(max(dp.values()))
else:
    print(1)


