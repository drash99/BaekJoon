


hor = set() #R
ver = set() #U
import bisect
from collections import deque


def cdtpt(coord, xpts, ypts):
    return (bisect.bisect(xpts,coord[0]), bisect.bisect(ypts,coord[1]))
    
def drawway():
    #print(pos)
    n = int(input())
    xpts = []
    xset = set()
    ypts = []
    yset = set()
    queries = deque()
    for i in range(n):
        rawx, rawy = map(int,input().split())
        queries.append((rawx,rawy))
        if not rawx in xset:
            xset.add(rawx)
            xpts.append(rawx)
        if not rawy in yset:
            yset.add(rawy)
            ypts.append(rawy)
    xpts.sort()
    ypts.sort()
    
    pos = cdtpt(queries.popleft(), xpts,ypts)
    
    while queries:
        raw = queries.popleft()
        cdt = cdtpt(raw, xpts,ypts)
        if cdt[1] == pos[1]:
            if cdt[0] > pos[0]:
                for i in range(pos[0], cdt[0]):
                    hor.add((i,pos[1]))
            else:
                for i in range( cdt[0],pos[0]):
                    hor.add((i,pos[1]))
        elif cdt[0] == pos[0]:
            if cdt[1] > pos[1]:
                for i in range(pos[1], cdt[1]):
                    ver.add((pos[0],i))
            else:
                for i in range( cdt[1],pos[1]):
                    ver.add((pos[0],i))
        pos = cdt


RU = []
RD = dict()
LU = dict()
LD = dict()
rectpossible = []
realrect = 0


def find_point():
    
    for horz in hor:
        if horz in ver:
            RU.append(horz)
        if (horz[0]+1, horz[1]) in ver:
            if not horz[1] in LU.keys():
                LU[horz[1]] = [(horz[0]+1, horz[1])]
            else:
                LU[horz[1]].append((horz[0]+1, horz[1]))
        if (horz[0], horz[1]-1) in ver:
            if not horz[0] in RD.keys():
                RD[horz[0]] = [(horz[0], horz[1])]
            else:
                RD[horz[0]].append((horz[0], horz[1]))
        if (horz[0]+1, horz[1]-1) in ver:
            if not horz[1] in LD.keys():
                LD[horz[1]] = [(horz[0]+1, horz[1])]
            else:
                LD[horz[1]].append((horz[0]+1, horz[1]))

def find_rect():
    for rup in RU:
        if rup[1] in LU.keys():
            for lup in LU[rup[1]]:
                if rup[0] < lup[0] and rup[0] in RD.keys():
                    for rdp in RD[rup[0]]:
                        if rdp[1] > rup[1] and rdp[1] in LD.keys():
                            for ldp in LD[rdp[1]]:
                                if ldp[0] == lup[0] and ldp != lup and rdp != ldp:
                                    rectpossible.append([rup,lup,rdp,ldp])


def check_rect():
    global realrect
    for rect in rectpossible:
        isreal = True
        for j in range(rect[0][1]+1, rect[2][1]):
            if (rect[0][0],j) in hor:
                isreal = False
                break
            
        for i in range(rect[0][0]+1, rect[1][0]):
            if (i,rect[0][1]) in ver:
                isreal = False
                break
            for j in range(rect[0][1]+1, rect[2][1]):
                if (i,j) in hor:
                    isreal = False
                    break
            if not (i,rect[0][1]) in hor:
                isreal = False
                break
            if not (i,rect[2][1]) in hor:
                isreal = False
                break
        
        if not (rect[0][0],rect[0][1]) in hor:
            isreal = False
            break
        if not (rect[0][0],rect[2][1]) in hor:
            isreal = False
            break
    
        for i in range(rect[0][1], rect[2][1]):
            if not (rect[0][0],i) in ver:
                isreal = False
                break
            if not (rect[1][0], i) in ver:
                isreal = False
                break
        if isreal:
            realrect+=1


        
drawway()
find_point()
find_rect()
check_rect()
print(realrect)

    
    

