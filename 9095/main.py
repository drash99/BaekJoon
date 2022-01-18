import sys
sys.setrecursionlimit(10**4)
ans = dict()
ans[3] = 4
ans[2] = 2
ans[1] = 1
ans[0] = 0

T = int(input())

def find(num):
    if num in ans.keys():
        return ans[num]
    return find(num-3)+find(num-2)+find(num-1)

for i in range(T):
    N = int(input())
    print(find(N))
