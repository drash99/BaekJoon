n,m = map(int,input().split())

bwdict = {'B':0,'W':1}


board = []
for _ in range(n):
    board.append(list(input()))

def findit(x,y,board):
    wstart = 0
    bstart = 0
    for i in range(x,x+8):
        cursor = i%2
        for j in range(y,y+8):

            if bwdict[board[i][j]] == cursor:
                wstart+=1
            else:
                bstart+=1
            cursor+=1
            cursor%=2
    return min(wstart, bstart)

mini = 987654321

for i in range(0,n-7):
    for j in range(0,m-7):
        mini = min(mini, findit(i,j,board))


print(mini)