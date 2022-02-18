import sys

n, m, k = map(int, input().split())
modu = 1000000007


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
            self.sum = (self.left.sum*self.right.sum)%modu

    def findsum(self, start, end):
        if start == self.start and end == self.end:
            return self.sum

        half = (self.start+self.end)//2+1
        if start < half:
            if end < half:
                return self.left.findsum(start,end)
            else:
                return (self.left.findsum(start,half-1)*self.right.findsum(half,end))%modu
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
            self.sum = (self.left.sum*self.right.sum)%modu

    def __str__(self) -> str:
        tmp = f"start: {self.start} end:{self.end} sum:{self.sum}"
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
        segtree.updatesum(line[1]-1,line[2])
    else:
        print(segtree.findsum(line[1]-1,line[2]-1))