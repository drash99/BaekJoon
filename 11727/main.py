import sys
sys.setrecursionlimit(10**4)
ans = dict()
ans[3] = 5
ans[2] = 3
ans[1] = 1
ans[0] = 0

N = int(input())

def find(num):
    if num in ans.keys():
        return ans[num]
    if num %2 ==0:
        return (find(num/2-1)*find(num/2-1)*2 + find(num/2)*find(num/2))%10007
    else:
        return (find(num//2)*find(num//2) + 4*find(num//2-1)*find(num//2))%10007
    return (find(num-2) + find(num-1))%10007

#for i in range(1,N):
    #find(i)
print(find(N))
