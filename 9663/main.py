n = int(input())

possible = []



answ = 0

def findsafe(status, pos):
    y = len(status)
    for i in range(y):
        if pos == status[i]:
            return False
        elif pos - status[i] == y-i:
            return False
        elif pos - status[i] == i-y:
            return False
    return True


def placeq(status, recurse): # status: [7 1 4 0 2 ] like
    if recurse == n:
        return 1
    tmp = 0
    for i in range(n):
        if findsafe(status,i):
            tmparr = status[:]
            tmparr.append(i)
            tmp += placeq(tmparr, recurse+1)
    return tmp

print(placeq(possible, 0))