import sys
import math

n = int(input())
nsq = math.ceil(math.sqrt(n))

nums = list(map(int, input().split()))

m = int(input())


class answer():
    def __init__(self, ansdict) -> None:
        self.ansdict = ansdict
        if len(ansdict) >0:
            self.maxvalue = max(ansdict.value())
        else:
            self.maxvalue = 0
    def add(self, value):
        if value in self.ansdict:
            self.ansdict[value] +=1
            if self.ansdict[value] > self.maxvalue:
                self.maxvalue +=1
        else:
            self.ansdict[value] = 1
            if self.maxvalue == 0:
                self.maxvalue = 1
    def delete(self, start, end):
        for i in range(start ,end+1):
            if nums[i] in self.ansdict:
                self.ansdict[nums[i]] -=1
                if self.ansdict[nums[i]] == 0:
                    self.ansdict.pop(nums[i])
        self.maxvalue = max(self.ansdict.values())

        
def findit(start, end):
    answ = answer(dict())
    for i in range(start, end+1):
        answ.add(nums[i])
    return answ

queries = []

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    queries.append((s-1,e-1))

ans = dict()

qsorted = sorted(queries, key= lambda x: (x[0]//nsq, x[1]))

befans = answer(dict())
befstart = -1
befend = -1


def adddict(dest, start, end):
    for i in range(start, end+1):
        dest.add(nums[i])

for i in qsorted:
    if befstart > i[0]:
        adddict(befans, i[0], befstart-1)
    elif befstart < i[0] and i[0] < befend :
        befans.delete(befstart, i[0]-1)

    if befend < i[1] and i[0] < befend :
        adddict(befans, befend+1, i[1])
    elif befend > i[1]:
        befans.delete(i[1]+1, befend)
    elif befend <= i[0]:
        befans = findit(i[0], i[1])
    ans[i] = befans.maxvalue
    befstart = i[0]
    befend = i[1]

for q in queries:
    print(ans[q])