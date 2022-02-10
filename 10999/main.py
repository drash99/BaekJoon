import sys

n, m, k = map(int, input().split())

testarr = []

class lazytree():
    def __init__(self, nums, start, end):
        self.lazy = 0
        self.start = start
        self.end = end
        if start == end:
            self.isleaf = True
            self.sum = nums[start]
        else:
            self.isleaf = False
            self.left = lazytree(nums,start, (start+end)//2)
            self.right = lazytree(nums,(start+end)//2+1, end)
            self.sum = self.left.sum+self.right.sum
    def applylazy(self):
        if self.lazy != 0:
            if not self.isleaf:
                self.left.lazy += self.lazy
                self.right.lazy += self.lazy
            self.sum += self.lazy*(self.end-self.start+1)
            self.lazy = 0
    def findsum(self, start, end):
        self.applylazy()
        if start == self.start and end == self.end:
            return self.sum

        half = (self.start+self.end)//2+1
        if start < half:
            if end < half:
                return self.left.findsum(start,end)
            else:
                return self.left.findsum(start,half-1)+self.right.findsum(half,end)
        else:
            return self.right.findsum(start,end)
    def updatesum(self, start, end, v):
        self.applylazy()
        if start == self.start and end == self.end:
            if not self.isleaf:
                self.left.lazy += v
                self.right.lazy += v
            self.sum += v*(end-start+1)
        else:
            half = (self.start+self.end)//2+1
            if start < half:
                if end < half:
                    self.left.updatesum(start,end,v)
                else:
                    self.left.updatesum(start,half-1,v)
                    self.right.updatesum(half,end,v)
            else:
                self.right.updatesum(start,end,v)
            self.sum = self.left.sum+self.right.sum

    def __str__(self) -> str:
        tmp = f"start: {self.start} end:{self.end} lazy:{self.lazy} sum:{self.sum}"
        if not self.isleaf:
            tmp+='\n'
            tmp += str(self.left)
            tmp+='\n'
            tmp += str(self.right )
        return tmp


nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

segtree = lazytree(nums,0,len(nums)-1)

for _ in range(m+k):
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 1:
        segtree.updatesum(line[1]-1,line[2]-1,line[3])
    else:
        print(segtree.findsum(line[1]-1,line[2]-1))
    print(segtree)
