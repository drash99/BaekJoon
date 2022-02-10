visited = []

def solnhelper(A, start, end):
    if start > end:
        return 0
    if start == end:
        visited[start][end] = A[start-1] * A[start] * A[start+1]
        return A[start-1] * A[start] * A[start+1]
    maxi = 9876543211
    for i in range(start, end+1):
        temp = A[start-1] * A[i] * A[end+1]

        if visited[start][i-1] != 0:
            temp += visited[start][i-1]
        else:
            temp += solnhelper(A,start, i-1)
        if visited[i+1][end] != 0:
            temp += visited[i+1][end]
        else:
            temp += solnhelper(A, i+1, end)
        if temp < maxi:
            maxi = temp
    visited[start][end] = maxi
    #print(start, end, A[start:end+1], maxi)
    return maxi

def solution(A):
    """
    Find the maximum score.

    Input
    -----
    A: list of N+2 positive integers with A[0]=A[N+1]=1. max(A) <= 1000.

    Output
    ------
    Return the maximum score achievable.
    """
    # print(A)
    global visited
    visited = [[0]*len(A) for i in range(len(A))]
    return solnhelper(A, 1, len(A)-2)



n = int(input())
arr = []
for i in list(map(int, input().split())):
    arr.append(i)
for _ in range(1,n):
    a, tmp = map(int,input().split())
    arr.append(tmp)
print(solution(arr))
