import math

inputraw = input().strip().split(' ')
N = int(inputraw[0])
M = int(inputraw[1])

inputraw = input().strip().split(' ')
inputlist = []
for i in inputraw:
    inputlist.append(int(i))

inputlist.sort(reverse=True)

current = 0
cursor = 0

difflist = [0]
for i in range(len(inputlist)-1):
    difflist.append(inputlist[i]-inputlist[i+1])
difflist.append(2000000000)

while (M > difflist[cursor+1]*(cursor+1)):
    current += difflist[cursor+1]
    M -= difflist[cursor+1]*(cursor+1)
    cursor += 1


print(inputlist[0]-current-math.ceil(M/(cursor+1)))

