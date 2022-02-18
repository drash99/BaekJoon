
def findpat(st):
    if len(st) == 0:
        return True
    if st[0] == '1':
        if len(st) > 3 and st[1] == '0' and st[2] == '0':
            cursor = 3
            while len(st) > cursor and st[cursor] == '0':
                cursor+=1
            if len(st) > cursor and st[cursor] == '1':
                hasone = False
                if len(st) > cursor+1 and st[cursor+1] == '1':
                   hasone = True 
                while len(st) > cursor and  st[cursor] == '1':
                    cursor+=1
                if hasone:
                    res1 = findpat(st[cursor-1:])
                    res2 = findpat(st[cursor:])
                    return res1 or res2
                return findpat(st[cursor:])
            else:
                return False

    else:
        if len(st)>= 2 and st[1] == '1':
            return findpat(st[2:])
    return False

for _ in range(int(input())):
    st = list(input())
    print('YES' if findpat(st) else 'NO')
