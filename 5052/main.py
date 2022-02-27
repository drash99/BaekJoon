from collections import deque

class trie:
    def __init__(self) -> None:
        self.childs = dict()
        self.isleaf = False
    def put(self, strdeq:deque):
        if not strdeq:
            if self.childs:
                return False
            self.isleaf = True
            return True
        head = strdeq.popleft()
        if not head in self.childs:
            if self.isleaf:
                return False
            self.childs[head] = trie()
        return self.childs[head].put(strdeq)
       
    def dfs(self, depth:int) -> list:
        pref = '--'*depth
        childkey = list(self.childs.items())
        childkey.sort(key=lambda x: x[0])
        for child in childkey:
            print(pref + child[0])
            self.childs[child[0]].dfs(depth+1)

t=int(input())
for _ in range(t):
    n = int(input())
    tri = trie()
    isno = False
    for _ in range(n):
        ins = deque(list(input()))
        if not tri.put(ins):
            
            isno = True
            
    if isno:
        print('NO')
    else:
        print('YES')
    #print(tri.dfs(0))
