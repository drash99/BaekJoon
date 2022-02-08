input()
inraw = input().strip().split(' ')
A = []
for r in inraw:
    A.append(int(r))

dp = []

def finddec(A):
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
        if i<=A[0]:
            adddp(i)
    return len(dp[-1])

ans = 0
ansdp = []

def adddp(num, j):
    if len(dp) == 0:
        dp.append([num])
        ansdp.append(1+finddec(A[j:]))
        return
    for i in range(len(dp)-1,-1,-1):
        if num > dp[i][-1]:
            if i+1 == len(dp):
                tmp = dp[i][:]
                tmp.append(num)
                dec = finddec(A[j:])
                ansdp.append(dec+len(tmp))
                dp.append(tmp)
            elif dp[i+1][-1] > num:
                tmp = dp[i][:]
                tmp.append(num)
                tmplen = finddec(A[j:]) + len(tmp)
                if tmplen > ansdp[i+1]:
                    ansdp[i+1] = tmplen
                dp[i+1] = tmp
        elif num < dp[i][-1]:
            if len(dp[i]) < 2:
                dp[i][-1] = num
            elif dp[i][-2] < num:
                dp[i][-1] = num
            

for i in range(len(A)):
    adddp(A[i],i)

print(max(ansdp)-1)


