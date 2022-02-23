import sys

n, q = map(int, input().split())


class lazytree():
    def __init__(self, nums, start, end):
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

    def findsum(self, start, end):
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
    def updatesum(self, start, v):
        if self.isleaf and start == self.start:
            self.sum = v
        else:
            half = (self.start+self.end)//2+1
            if start < half:
                self.left.updatesum(start,v)
            else:
                self.right.updatesum(start,v)
            self.sum = self.left.sum+self.right.sum

    def __str__(self) -> str:
        tmp = f"start: {self.start} end:{self.end} sum:{self.sum}"
        if not self.isleaf:
            tmp+='\n'
            tmp += str(self.left)
            tmp+='\n'
            tmp += str(self.right )
        return tmp


nums = []
nums = list(map(int, input().split()))

segtree = lazytree(nums,0,len(nums)-1)

for _ in range(q):
    x,y,a,b = map(int, sys.stdin.readline().split())
    if x>y:
        x,y = y,x
    print(segtree.findsum(x-1,y-1))
    segtree.updatesum(a-1,b)