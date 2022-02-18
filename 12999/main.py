import sys
import math

n,m = map(int, input().split())
nsq = math.ceil(math.sqrt(n))

nums = list(map(int, input().split()))



class answer():
    def __init__(self) -> None:
        self.ansdict = [0 for _ in range(200001)]
        self.cntmask = [0 for _ in range(200001//300)]
        self.cnts = [0 for _ in range(2000001)]
    def add(self, value):
        value+=100000
        self.cnts[self.ansdict[value]] = max(self.cnts[self.ansdict[value]]-1, 0) 
        self.cntmask[self.ansdict[value]//300] = max(self.cntmask[self.ansdict[value]//300] -1,0)
        self.ansdict[value] +=1
        self.cnts[self.ansdict[value]]+=1
        self.cntmask[self.ansdict[value]//300] +=1
        
    def delete(self, value):
        value+=100000
        assert self.ansdict[value] > 0

        self.cnts[self.ansdict[value]] = max(self.cnts[self.ansdict[value]]-1, 0) 
        self.cntmask[self.ansdict[value]//300] = max(self.cntmask[self.ansdict[value]//300] -1,0)
        self.ansdict[value] -=1
        self.cnts[self.ansdict[value]]+=1
        self.cntmask[self.ansdict[value]//300] +=1
    def getmax(self):
        cursor = 200001//300-1
        while(self.cntmask[cursor] == 0):
            cursor-=1
        for i in range(min((cursor+1)*300-1, 100000),cursor*300-1, -1):
            if self.cnts[i] != 0:
                return i
        return 0
        
def findit(start, end):
    answ = answer()
    for i in range(start, end+1):
        answ.add(nums[i])
    return answ

queries = []

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    queries.append((s-1,e-1))

ans = dict()

qsorted = sorted(queries, key= lambda x: (x[0]//nsq, x[1]))

befans = answer()
befstart = -1
befend = -1


def adddict(dest, start, end):
    for i in range(start, end+1):
        dest.add(nums[i])
def deletedict(dest, start, end):
    for i in range(start, end+1):
        dest.delete(nums[i])

for i in qsorted:
    if befstart > i[0]:
        adddict(befans, i[0], befstart-1)
    elif befstart < i[0] and i[0] < befend :
        deletedict(befans, befstart, i[0]-1)

    if befend < i[1] and i[0] < befend :
        adddict(befans, befend+1, i[1])
    elif befend > i[1]:
        deletedict(befans, i[1]+1, befend)
    elif befend <= i[0]:
        befans = findit(i[0], i[1])
    ans[i] = befans.getmax()
    befstart = i[0]
    befend = i[1]

for q in queries:
    print(ans[q])