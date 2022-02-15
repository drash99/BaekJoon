n = int(input())

ab = list(map(int, input().split()))


cnt = 0

def mergesort(a):
    if len(a) <= 1:
        return a
    middle = len(a)//2
    left = mergesort(a[:middle])
    right = mergesort(a[middle:])
    cursorl = 0
    cursorr = 0
    global cnt
    while(len(left)>cursorl and len(right)>cursorr):
        if left[cursorl] > right[cursorr]:
            a[cursorl+cursorr] = right[cursorr]
            cnt += len(left)-cursorl
            cursorr+=1
        else:
            a[cursorl+cursorr] = left[cursorl]
            cursorl+=1
    if cursorl < len(left):
        for i in range(cursorl, len(left)):
            a[i+cursorr] = left[i]
    elif cursorr < len(right):
        for i in range(cursorr, len(right)):
            a[i+cursorl] = right[i]
    return a

mergesort(ab)
print(cnt)
