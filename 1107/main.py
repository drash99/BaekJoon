current = 100
N = input()
brokennum = int(input())
button = [0,1,2,3,4,5,6,7,8,9]
if(brokennum>0):
    inputraw = input().strip().split(' ')
    for i in inputraw:
        button.remove(int(i))
pushed = 0

def getpush(a,b ):
    return len(a) + (b-int(a))

def getlessoreq(a):
    res = 0
    for i in range(len(a)):
        if(int(a[i]) in button):
            res=res*10+int(a[i])
        else:
            


def makenear(N):



if(N == "100"):
    print(0)
else:
