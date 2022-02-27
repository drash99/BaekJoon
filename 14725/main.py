from collections import deque
n = int(input())

class trie:
    def __init__(self) -> None:
        self.childs = dict()
    def put(self, strdeq:deque):
        if not strdeq:
            return
        head = strdeq.popleft()
        if not head in self.childs:
            self.childs[head] = trie()
        self.childs[head].put(strdeq)
    def dfs(self, depth:int) -> list:
        pref = '--'*depth
        childkey = list(self.childs.items())
        childkey.sort(key=lambda x: x[0])
        for child in childkey:
            print(pref + child[0])
            self.childs[child[0]].dfs(depth+1)

tri = trie()
for _ in range(n):
    tri.put(deque(input().split()[1:]))

ans = tri.dfs(0)

