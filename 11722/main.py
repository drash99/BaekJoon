input()
inraw = input().strip().split(' ')
A = []
for r in inraw:
    A.append(int(r))

dp = []

def adddp(num):
    if len(dp) == 0:
        dp.append([num])
        return
    for i in range(len(dp)-1,-1,-1):
        if num < dp[i][-1]:
            if i+1 == len(dp):
                tmp = dp[i][:]
                tmp.append(num)
                dp.append(tmp)
            elif dp[i+1][-1] < num:
                tmp = dp[i][:]
                tmp.append(num)
                dp[i+1] = tmp
        elif num > dp[i][-1]:
            if len(dp[i]) < 2:
                dp[i][-1] = num
            elif dp[i][-2] > num:
                dp[i][-1] = num
            

for i in A:
    adddp(i)

print(len(dp[-1]))
print(' '.join(str(dp[-1]).strip('[]').split(', ')))


