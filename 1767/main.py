import math

n = int(input())
m = int(input())
k = int(input())



dp = dict() #k -> [(wh, wv, imph, impv):n]

def finddp(i):
    if i in dp.keys():
        return dp[i]
    return dict()

dp[(1,0)] = {(m-1,n-1,0, 0):n*m}

for i in range(2,k+1):
    for j in range(0,i+1,2):
        dp[(i,j)] = dict()
        for l in finddp((i-1,j)).keys():
            tmp1 = l[0] - 1
            tmp2 = l[1] - 1
            tmp3 = l[2]
            tmp4 = l[3]
            tmp5 = (dp[(i-1,j)][l] * l[0] * l[1])
            if tmp5 > 0:
                if (tmp1,tmp2,tmp3,tmp4) in dp[(i,j)].keys():
                    dp[(i,j)][(tmp1,tmp2,tmp3,tmp4)] += tmp5
                else:
                    dp[(i,j)][(tmp1,tmp2,tmp3,tmp4)] = tmp5
        for l in finddp((i-1,j-2)).keys():
            if (n-l[1]-l[3])>0 :
                tmp1 = l[0] - 1
                tmp2 = l[1] 
                tmp3 = l[2] + 2
                tmp4 = l[3] + 1
                tmp5 = (dp[(i-1,j-2)][l] * (l[0]*(n-l[1]-l[3])))

                if tmp5 > 0:
                    if (tmp1,tmp2,tmp3,tmp4) in dp[(i,j)].keys():
                        dp[(i,j)][(tmp1,tmp2,tmp3,tmp4)] += tmp5
                    else:
                        dp[(i,j)][(tmp1,tmp2,tmp3,tmp4)] = tmp5
            if (m-l[2]-l[0])>0:
                tmp1 = l[0] 
                tmp2 = l[1] - 1
                tmp3 = l[2] + 1
                tmp4 = l[3] + 2
                tmp5 = (dp[(i-1,j-2)][l] * (l[1]*(m-l[0]-l[2])))

                if tmp5 > 0:
                    if (tmp1,tmp2,tmp3,tmp4) in dp[(i,j)].keys():
                        dp[(i,j)][(tmp1,tmp2,tmp3,tmp4)] += tmp5
                    else:
                        dp[(i,j)][(tmp1,tmp2,tmp3,tmp4)] = tmp5
        

ans = 0
for i in range(0,k+1,2):
    for j in finddp((k,i)).keys():
        ans += dp[(k,i)][j]
#print(dp)
print((ans//math.factorial(k))%1000001)

    
