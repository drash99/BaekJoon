import sys
import bisect

n= map(int, input().split())

testarr = []


class lazytree():
    def __init__(self, nums, start, end):
        self.start = start
        self.end = end
        if start == end:
            self.isleaf = True
            self.sum = [nums[start]]
        else:
            self.isleaf = False
            self.left = lazytree(nums,start, (start+end)//2)
            self.right = lazytree(nums,(start+end)//2+1, end)
            self.mergechild()
    def mergechild(self):
        self.sum = []
        cx = 0
        cy = 0
        while(cx < len(self.left.sum) and cy < len(self.right.sum)):
            if self.left.sum[cx] > self.right.sum[cy]:
                self.sum.append(self.right.sum[cy])
                cy+=1
            else:
                self.sum.append(self.left.sum[cx])
                cx+=1
        if cx < len(self.left.sum):
            self.sum.extend(self.left.sum[cx:])
        elif cy < len(self.right.sum):
            self.sum.extend(self.right.sum[cy:])
        


    def findsum(self, start, end, x):
        if self.isleaf:
            if x<self.sum[0]:
                return 1
            else:
                return 0
        if start == self.start and end == self.end:
            ans = len(self.sum) - bisect.bisect(self.sum, x)
            return ans
        half = (self.start+self.end)//2+1
        if start < half:
            if end < half:
                return self.left.findsum(start,end,x)
            else:
                return self.left.findsum(start,half-1,x)+self.right.findsum(half,end,x)
        else:
            return self.right.findsum(start,end,x)


nums = list(map(int, input().split()))
m = int(input())
segtree = lazytree(nums,0,len(nums)-1)
lastans = 0
for _ in range(m):
    line = list(map(int, sys.stdin.readline().split()))
    i = line[0]^lastans
    j = line[1]^lastans
    k = line[2]^lastans
    lastans = segtree.findsum(i-1,j-1,k)
    print(lastans)