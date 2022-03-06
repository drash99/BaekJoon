import sys, os
modu = 1000000007
from io import BytesIO, IOBase
from operator import add



# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
#endregion

n= int(input())


class lazytree():
    def __init__(self, nums, start, end):
        self.lazysum = 0
        self.start = start
        self.end = end
        if start == end:
            self.sum = nums[start]
        else:
            self.left = lazytree(nums,start, (start+end)//2)
            self.right = lazytree(nums,(start+end)//2+1, end)
            self.sum = 0#(self.left.sum+self.right.sum)%modu
    def applylazy(self):
        if self.lazysum != 0:
            if self.start != self.end:
                self.left.lazysum ^= self.lazysum
                self.right.lazysum ^= self.lazysum
            else:
                self.sum ^= self.lazysum
            #self.sum += self.lazysum*(self.end-self.start+1)
            self.lazysum = 0
        self.sum %= modu
    def findsum(self, start, end):
        self.applylazy()
        self.sum %= modu
        if start == self.start and end == self.end:
            return self.sum

        half = (self.start+self.end)//2+1
        if start < half:
            if end < half:
                return self.left.findsum(start,end)
            else:
                return (self.left.findsum(start,half-1)+self.right.findsum(half,end))%modu
        else:
            return self.right.findsum(start,end)
    def updatesum(self, start, end, v):
        self.applylazy()
        if start == self.start and end == self.end:
            if self.start != self.end:
                self.left.lazysum ^= v
                self.right.lazysum ^= v
                #self.sum += v*(end-start+1)
            else:
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
            #self.sum = self.left.sum+self.right.sum
        #self.sum %= modu


nums = list(map(lambda x: int(x)%modu ,sys.stdin.readline().split()))


segtree = lazytree(nums,0,len(nums)-1)

m = int(input())
for _ in range(m):
    line = list(map(int, input().split()))
    if line[0] == 1:
        segtree.updatesum(line[1],line[2],line[3])
    else:
        print(segtree.findsum(line[1],line[1]))
