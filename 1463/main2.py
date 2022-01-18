import sys
sys.setrecursionlimit(10**6)
finds = dict()
finds[10] = 3
def oldfind(num):
    if num in finds.keys():
        return finds[num]
    if num == 1:
        return 0
    ans = oldfind(num-1)+1
    if num % 3 == 0:
        ans = min(ans,oldfind(num/3) + 1)
    if num % 2 == 0:
        ans = min(ans,oldfind(num/2) + 1)
    finds[num] = ans
    return ans

N = int(input())
for i in range(1,N):
    oldfind(i)
print(oldfind(N))
    