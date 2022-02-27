from collections import deque
import sys
input = sys.stdin.readline

class trie:
    def __init__(self,idx) -> None:
        self.childs = dict()
        self.idx = idx
        self.lazy = None
        self.lazyidx = 0
    def applylazy(self):
        deq = deque(self.lazy)
        self.lazy = None
        head = deq.popleft()
        self.childs[head] = trie(self.lazyidx)
        self.childs[head].put(self.lazyidx,deq)

    def put(self,idx, strdeq:deque):
        if not strdeq:
            return 
        if self.lazy:
            self.applylazy()
        if not self.childs and len(strdeq) > 1:
            self.lazy = strdeq
            self.lazyidx = idx
            return
        head = strdeq.popleft()
        if not head in self.childs:
            self.childs[head] = trie(idx)
        return self.childs[head].put(idx, strdeq)
       
    def search(self, strdeq:deque):
        print(''.join(strdeq))
        if not strdeq:
            return self.idx
        if self.lazy:
            tmp = deque(self.lazy)
            print(''.join(tmp)+'tmp')
            if len(tmp) < len(strdeq):
                return -1
            while strdeq:
                if tmp.popleft() != strdeq.popleft():
                    return -1
            return self.idx                

        head = strdeq.popleft()
        if not head in self.childs:
            return -1
        return self.childs[head].search(strdeq)

    def dfs(self, depth:int) -> list:
        pref = '--'*depth
        childkey = list(self.childs.items())
        childkey.sort(key=lambda x: x[0])
        for child in childkey:
            print(pref + child[0])
            self.childs[child[0]].dfs(depth+1)


tri = trie(0)
tri.put(0,deque(["1"]))
tmp1 = 1
tmp2 = 1
for i in range(2,100000):
    tmp3 = tmp1+tmp2
    tmp1 = tmp2
    tmp2 = tmp3
    if tmp3 > 10**70:
        tmp1//=10
        tmp2//=10
    tri.put(i,deque(str(tmp3)[:40]))

t=int(input())
for i in range(t):
    n = deque(input().strip())
    print(f"Case #{i+1}: {tri.search(n)}")
    #tri.dfs(0)
