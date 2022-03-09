import sys

input = sys.stdin.readline
class Configuration(object):
    """
    Configuration for test environment.

    Parameters
    ----------
    MAXIMUM_TEST_SET_NUMBER: an integer i
        where i is an element in {1,2,3,4}.
        Only the test set 1 to i will be tested and graded,
        and the remaining test sets will be ignored.
    """
    MAXIMUM_TEST_SET_NUMBER = 4


class rangeytree(object):
    def __init__(self, points):
        length = len(points)
        self.leaves = length
        if length == 1:
            self.value = points[0][1]
            self.isLeaf = True
        else:
            self.left = rangeytree(points[0:length // 2])
            self.right = rangeytree(points[length // 2:length])
            self.value = self.left.getmax()
            self.isLeaf = False

    def getmax(self):
        if self.isLeaf:
            return self.value
        rightmax = self.right.getmax()
        if self.value > rightmax:
            return self.value
        else:
            return rightmax

    def query(self, rect, vsplit):  # 0:none, 1: left, 2: right
        if self.isLeaf:
            if rect[1][0] <= self.value <= rect[1][1]:
                return 1
            else:
                return 0
        if vsplit == 1:
            if self.value >= rect[1][0]:
                return self.left.query(rect, 1) + self.right.leaves
            else:
                return self.right.query(rect, 1)
        elif vsplit == 2:
            if self.value <= rect[1][1]:
                return self.right.query(rect, 2) + self.left.leaves
            else:
                return self.left.query(rect, 2)
        else:
            if rect[0][0] == rect[0][1]:
                return self.left.query(rect, 0)+self.right.query(rect, 0)
            if self.value >= rect[1][0]:
                if self.value >= rect[1][1]:
                    return self.left.query(rect, 0)
                else:  # vsplit
                    return self.left.query(rect, 1)+self.right.query(rect, 2)
            else:
                return self.right.query(rect, 0)


class rangetree(object):

    def __init__(self, points):
        length = len(points)
        if length == 1:
            self.value = points[0][0]
            self.ytree = points[0][1]
            self.isLeaf = True
        else:
            self.left = rangetree(points[0:length // 2])
            self.right = rangetree(points[length // 2:length])
            self.value = self.left.getmax()
            self.isLeaf = False
            points2 = sorted(points, key=lambda x: x[1])
            self.ytree = rangeytree(points2)

    def getmax(self):
        if self.isLeaf:
            return self.value
        rightmax = self.right.getmax()
        if self.value > rightmax:
            return self.value
        else:
            return rightmax


    def getycount(self, rect):
        return self.ytree.query(rect,0)

    def getcount(self, rect):
        if self.isLeaf:
            if rect[0][0] <= self.value <= rect[0][1] and rect[1][0] <= self.ytree <= rect[1][1]:
                return 1
            else:
                return 0
        return self.getycount(rect)

    def query(self, rect, vsplit):  # 0:none, 1: left, 2: right
        if self.isLeaf:
            if rect[0][0] <= self.value <= rect[0][1] and rect[1][0] <= self.ytree <= rect[1][1]:
                return 1
            else:
                return 0
        if vsplit == 1:
            if self.value >= rect[0][0]:
                return self.left.query(rect, 1) + self.right.getcount(rect)
            else:
                return self.right.query(rect, 1)
        elif vsplit == 2:
            if self.value <= rect[0][1]:
                return self.right.query(rect, 2) + self.left.getcount(rect)
            else:
                return self.left.query(rect, 2)
        else:
            if rect[0][0] == rect[0][1]:
                return self.left.query(rect, 0)+self.right.query(rect, 0)
            if self.value >= rect[0][0]:
                if self.value >= rect[0][1]:
                    return self.left.query(rect, 0)
                else:  # vsplit
                    return self.left.query(rect, 1)+self.right.query(rect, 2)
            else:
                return self.right.query(rect, 0)


class Solution(object):

    def __init__(self, points):
        """
        Initialize this class instance.

        Parameters
        ----------
        points : list of integer coordinates, each of form [x,y], that is
                 [[x1,y1], [x2,y2], ... , [xN,yN]]
        """
        points.sort(key=lambda x: x[0])
        self.xs = rangetree(points)

    def query(self, rect) -> int:
        # print(hubo)
        ans = self.xs.query(rect,0)

        return ans


if __name__ == "__main__":
    # sample 1
    for _ in range(int(input())):
        points = []
        n, m = map(int, input().split())
        for _ in range(n):
            points.append(list(map(int,input().split())))
        sol = Solution(points)
        ans = 0
        for _ in range(m):
            a,b,c,d = map(int,input().split())
            ans += (sol.query([[a,b],[c,d]]))
        print(ans)