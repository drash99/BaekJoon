import sys

n, m= map(int, input().split())


class lazytree():
    def __init__(self, nums, start, end):
        self.lazy = 0
        self.start = start
        self.end = end
        if start == end:
            self.sum = nums[start]
        else:
            self.left = lazytree(nums,start, (start+end)//2)
            self.right = lazytree(nums,(start+end)//2+1, end)
            self.sum = self.left.sum+self.right.sum
    def applylazy(self):
        if self.lazy != 0:
            if self.start != self.end:
                self.left.lazy += self.lazy
                self.left.lazy %= 2
                self.right.lazy += self.lazy
                self.right.lazy %= 2
            self.sum = (self.end-self.start+1) - self.sum
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
    def updatesum(self, start, end):
        self.applylazy()
        if start == self.start and end == self.end:
            if self.start != self.end:
                self.left.lazy += 1
                self.left.lazy %= 2
                self.right.lazy += 1
                self.right.lazy %= 2
                self.sum = (end-start+1) - self.sum
            else:
                self.sum += 1
                self.sum %= 2
        else:
            half = (self.start+self.end)//2+1
            if start < half:
                if end < half:
                    self.left.updatesum(start,end)
                    self.right.applylazy()
                else:
                    self.left.updatesum(start,half-1)
                    self.right.updatesum(half,end)
            else:
                self.left.applylazy()
                self.right.updatesum(start,end)
            self.sum = self.left.sum+self.right.sum


nums = [0]*n

segtree = lazytree(nums,0,len(nums)-1)

for _ in range(m):
    line = list(map(int, sys.stdin.readline().strip().split()))
    if line[0] == 0:
        segtree.updatesum(line[1]-1,line[2]-1)
    else:
        print(segtree.findsum(line[1]-1,line[2]-1))
