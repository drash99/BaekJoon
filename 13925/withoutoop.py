import sys
import os

modu = 1000000007
from io import BytesIO, IOBase
from operator import add, mod

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


# region LazySeg, Original source by kclee2172
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._depth = self._size.bit_length()
        self._lazy = [0] * (2 * _size)
        self._lazygop = [1] * (2 * _size)
        self._lazyval = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazygop[idx] = self._lazygop[idx], 1
        self._lazy[2 * idx] *= q
        self._lazy[2 * idx + 1] *= q
        self._lazygop[2 * idx] *= q
        self._lazygop[2 * idx + 1] *= q
        self._lazy[2 * idx] %= modu
        self._lazy[2 * idx + 1] %= modu
        self._lazygop[2 * idx] %= modu
        self._lazygop[2 * idx + 1] %= modu
        self.data[2 * idx] *= q #<< self._depth - (2 * idx).bit_length()
        self.data[2 * idx + 1] *= q #<< self._depth - (2 * idx + 1).bit_length()

        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q << self._depth - (2 * idx).bit_length()
        self.data[2 * idx + 1] += q << self._depth - (2 * idx + 1).bit_length()
        self.data[2 * idx] %= modu
        self.data[2 * idx+1] %= modu

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])*(self._lazygop[idx]) + (self._lazy[idx] << self._depth - idx.bit_length())
            self.data[idx] %= modu
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value << self._depth - start.bit_length()
                self.data[start] %= modu
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value << self._depth - stop.bit_length()
                self.data[stop] %= modu
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def gop(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazygop[start] *= value
                self._lazy[start] *= value
                self._lazygop[start] %= modu
                self._lazy[start] %= modu
                self.data[start] *= value# << self._depth - start.bit_length()
                self.data[start] %= modu
                start += 1
            if stop & 1:
                stop -= 1
                self._lazygop[stop] *= value
                self._lazy[stop] *= value
                self._lazygop[stop] *= modu
                self._lazy[stop] *= modu
                self.data[stop] *= value #<< self._depth - stop.bit_length()
                self.data[stop] %= modu
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)
    def val(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazygop[start] = 1
                self._lazy[start] = 0
                self.data[start] = value << self._depth - start.bit_length()
                self.data[start] %= modu
                start += 1
            if stop & 1:
                stop -= 1
                self._lazygop[stop] = 1
                self._lazy[stop] = 0
                self.data[stop] = value << self._depth - stop.bit_length()
                self.data[stop] %= modu
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)
    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])%modu
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])%modu
            start >>= 1
            stop >>= 1
        return res%modu

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)
# endregion

n= int(input())
a=list(map(lambda x: x%modu, map(int,input().split())))
k = int(input())
tr=LazySegmentTree(a,func = add)
for i in range(k):
    q=list(map(int,input().split()))
    if q[0]==1:
        tr.add(q[1]-1,q[2],q[3])
    elif q[0]==2:
        tr.gop(q[1]-1,q[2],q[3])
    elif q[0]==3:
        tr.val(q[1]-1,q[2],q[3])
    else:
        #print(tr.__repr__)
        print(tr.query(q[1]-1,q[2]))
