from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

arr = deque()

for _ in range(n):
    arr.append(input().strip())

t = []
def findclosest(arr, st):
    ls = 0
    rs = 0
    while(len(arr)>0 and arr[0] >= st):
        arr.popleft()
        ls+=1
    while(len(arr)>0 and arr[-1] >= st):
        arr.pop()
        rs+=1
    if arr:
        if ls>rs:
            return 1
        elif ls<rs:
            return 2
    return 0

def resolvecoll(arr): #0: stalemate, 1: remove all back 2:remove all forward 3: remove both
    if len(arr) == 1:
        return 1
    if len(arr) == 0:
        return 0
    assert arr[0] == arr[-1]
    st = arr[0]
    ls = 0
    rs = 0
    while(len(arr)>0 and arr[0] == st):
        arr.popleft()
        ls+=1
    while(len(arr)>0 and arr[-1] == st):
        arr.pop()
        rs+=1
    #print(ls,rs,st,arr,srcarr)
    
    if len(arr) == 1:
        return 1
    if len(arr) == 0:
        return 0
        
    if arr[0] < st and arr[-1] < st:
        if rs>ls:
            return 1
        elif ls<rs:
            return 2
        else:
            if arr[0] > arr[-1]:
                return 1
            elif arr[0] < arr[-1]:
                return 2

    closest = findclosest(deque(arr), st)
    if closest == 1:
        return 1
    elif closest == 2:
        return 2
        
    assert arr[0]!=st and arr[-1]!=st
    if arr[0] > arr[-1]:
        return 1
    elif arr[0] < arr[-1]:
        return 2
    assert arr[0] == arr[-1]
    if ls > rs:
        return 1
    elif ls < rs:
        return 2
    assert ls==rs and arr[0] ==arr[-1]

    cor = resolvecoll(arr)
    return cor


while arr:
    if len(arr)<=1:
        break
    if arr[0] < arr[-1]:
        t.append(arr.popleft())
    elif arr[0] > arr[-1]:
        t.append(arr.pop()) 
    else:
        st = arr[0]
        direc = resolvecoll(deque(arr))
        if direc == 0:
            break
        elif direc == 1:
            while(arr[-1]==st):
                t.append(arr.pop())
        elif direc == 2:
            while(arr[0]==st):
                t.append(arr.popleft())

if arr:
    while len(arr) > 1:
        t.append(arr.pop())
        t.append(arr.popleft())
    if arr:
        t.append(arr.pop())

ansstr = ''
for idx, i in enumerate(t):
    if idx%80==0 and idx > 0:
        ansstr+='\n'
    ansstr+=i

print(ansstr)