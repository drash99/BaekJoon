N, M = map(int, input().split())

def printnm(start,m,current):
    if m == 1:
        for i in range(start+1,N+1):
            print(current+str(i))
        return
    else:
        for i in range(start+1,N+2-m):
            printnm(i,m-1,current+str(i)+' ')
        return

printnm(0,M,'')
