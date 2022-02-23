import sys

n= int(input())

testarr = []

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
            self.sum = self.left.sum^self.right.sum
    def applylazy(self):
        if self.lazy != 0:
            if self.start != self.end:
                self.left.lazy ^= self.lazy
                self.right.lazy ^= self.lazy
            if (self.end-self.start+1 )%2 != 0:
                self.sum ^= self.lazy
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
                return self.left.findsum(start,half-1)^self.right.findsum(half,end)
        else:
            return self.right.findsum(start,end)
    def updatesum(self, start, end, v):
        self.applylazy()
        if self.start == self.end and start != end:
            print(testarr[0])
        if start == self.start and end == self.end:
            if self.start != self.end:
                self.left.lazy ^= v
                self.right.lazy ^= v
            if (end-start+1)%2 != 0:
                self.sum ^= v
        else:
            half = (self.start+self.end)//2+1
            if start < half:
                if end < half:
                    self.left.updatesum(start,end,v)
                    self.right.applylazy()
                else:
                    self.left.updatesum(start,half-1,v)
                    self.right.updatesum(half,end,v)
            else:
                self.left.applylazy()
                self.right.updatesum(start,end,v)
            self.sum = self.left.sum^self.right.sum

    def __str__(self) -> str:
        tmp = f"start: {self.start} end:{self.end} lazy:{self.lazy} sum:{self.sum}"
        if self.start != self.end:
            tmp+='\n'
            tmp += str(self.left)
            tmp+='\n'
            tmp += str(self.right )
        return tmp


nums = list(map(int, input().split()))

segtree = lazytree(nums,0,len(nums)-1)

for _ in range(int(input())):
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 1:
        segtree.updatesum(line[1],line[2],line[3])
    else:
        print(segtree.findsum(line[1],line[2]))
    print(segtree)
