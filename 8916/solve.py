import math

def Comb(num1, num2):
    return math.comb(num1+num2, num1)%9999991

def findnum(numlist):
    if(len(numlist) == 0):
        return 1
    less = []
    more = []
    for i in numlist[1:]:
        if i<numlist[0]:
            less.append(i)
        else:
            more.append(i)
    return (findnum(less)*findnum(more)*Comb(len(less), len(more)))%9999991


K = int(input())
for a in range(K):
    input()
    inputraw = input().strip().split(' ')
    inputlist = []
    for num in inputraw:
        inputlist.append(int(num))
    print(findnum(inputlist))
