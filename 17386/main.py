x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

def line(x,y):
    return (y4-y3)*(x-x4) - (x4-x3)*(y-y4)

def line2(x,y):
    return (y2-y1)*(x-x2) - (x2-x1)*(y-y2)

def findxy():
    if (line(x1,y1)* line(x2,y2)<=0 and line2(x3,y3)* line2(x4,y4)<=0):
        pass
    else:
        print(0)
        return
    a = (y4-y3)*(x2-x1)
    b = (x4-x3)*(y2-y1)
    c = (x4-x3)*(y2-y4)*(x2-x1)
    if a-b != 0:
        print(1)
        x = (a*x4-b*x2+c)/(a-b)
        if x4-x3 != 0:
            y = (y4-y3)*(x-x4)/(x4-x3) + y4
        else:
            y = (y2-y1)*(x-x2)/(x2-x1) + y2
        print(x,y)
    else:
        if x3 > max(x2,x1) and x4 > max(x2,x1):
            print(0)
            return
        elif x3 < min(x2,x1) and x4 < min(x2,x1):
            print(0)
            return
        elif y3 > max(y2,y1) and y4 > max(y2,y1):
            print(0)
            return
        elif y3 < min(y2,y1) and y4 < min(y2,y1):
            print(0)
            return
        print(1)
        if x2==x3 and y2==y3:
            if x2>=x1 and x3<=x4:
                print(x2,y2)
            elif x2<=x1 and x3 >=x4:
                print(x2,y2)
        elif x2==x4 and y2==y4:
            if x2>=x1 and x3>=x4:
                print(x2,y2)
            elif x2<=x1 and x3<=x4:
                print(x2,y2)
        elif x1==x3 and y1==y3:
            if x2<=x1 and x3<=x4:
                print(x1,y1)
            elif x2>=x1 and x3 >=x4:
                print(x1,y1)
        elif x1==x4 and y1==y4:
            if x2<=x1 and x3>=x4:
                print(x1,y1)
            elif x2>=x1 and x3<=x4:
                print(x1,y1)
                
findxy()