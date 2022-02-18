from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

arr = []

for _ in range(n):
    arr.append(input().strip())

t = []



i = 0
j = n-1
while i <= j:
    if arr[i] < arr[j]:
        t.append(arr[i])
        i+=1
    elif arr[i] > arr[j]:
        t.append(arr[j])
        j-=1 
    else:
        direc = 0
        ii = i
        jj = j
        while(ii<jj and arr[ii] == arr[jj]):
            ii+=1
            jj-=1
        if ii >= jj or arr[ii] < arr[jj]:
            t.append(arr[i])
            i+=1
        else:
            t.append(arr[j])
            j-=1



ansstr = ''
for idx, i in enumerate(t):
    if idx%80==0 and idx > 0:
        ansstr+='\n'
    ansstr+=i

print(ansstr)