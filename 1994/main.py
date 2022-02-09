n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
A.sort()

dp = dict() # fi, d : (len)

ones = set()

ans = 0

for i in A:

    if i in dp.keys():
        todos = dp[i]
        dp.pop(i)
        for j in ones:
            if 2*i-j in dp.keys():
                if not i-j in dp[2*i-j].keys():
                    dp[2*i-j][i-j] = 2
            else:
                dp[2*i-j] = {i-j:2}
        for j in todos.keys():
            if j == 0:
                dp[i][j] = todos[j]+1
                continue
            if i+j in dp.keys():
                if j in dp[i+j].keys():
                    dp[i+j][j] = max(dp[i+j][j]+1,todos[j]+1)
                else:
                    dp[i+j][j] = todos[j]+1
            else:
                dp[i+j] = {j:dp[i][j]+1}
    else:
        for j in ones:
            if 2*i-j in dp.keys():
                if not i-j in dp[2*i-j].keys():
                    dp[2*i-j][i-j] = 2
            else:
                dp[2*i-j] = {i-j:2}
    ones.add(i)


if len(dp.values()) > 0:
    answ = 0
    for i in dp.values():
        for j in i.keys():
            answ = max(i[j],answ)
    print(answ)
else:
    print(1)

