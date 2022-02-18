import bisect
import sys
input = sys.stdin.readline

arr = [('1',0)]

tmp1 = 1
tmp2 = 1
for i in range(2,100000):
    tmp3 = tmp1+tmp2
    tmp1 = tmp2
    tmp2 = tmp3
    if tmp3 > 10**44:
        tmp1//=10
        tmp2//=10
    arr.append((str(tmp3)[:40],i))

arr.sort()
for _ in range(int(input())):
    s = int(input().strip())
    a = bisect.bisect_left(arr, (str(s),0))
    b = bisect.bisect_left(arr, (str(s+1),0))
    print(arr[a-5:a+5])
    print(arr[b-5:b+5])
