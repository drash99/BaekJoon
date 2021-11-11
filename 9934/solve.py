K = int(input())
inputraw = input().strip().split(' ')
inputlist = []
for num in inputraw:
    inputlist.append(int(num))
res = []
for i in range(K):
    res.append([])

def parsetree(listint, level):
    if len(listint) == 1:
        res[level].append(listint[0])
    else:
        middle = len(listint)//2
        parsetree(listint[:middle], level+1)
        res[level].append(listint[middle])
        parsetree(listint[middle+1:], level+1)

parsetree(inputlist, 0)

def printres(res):
    for i in res:
        temp = ""
        for j in i:
            temp += str(j)
            temp += " "
        print(temp)

printres(res)