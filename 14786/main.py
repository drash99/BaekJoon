import math
itr = 0

a,b,c= map(int,input().split())

class rati(object):
    def __init__(self, a:int,b:int):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a)+ '/'+ str(self.b)
    def tofloat(self):
        tmp = rati(round(1000000*self.a/self.b),1000000)
        if tmp > self and tmp-self > rati(5,10000000):
            tmp = tmp-rati(1,1000000)
        elif tmp < self and self-tmp > rati(5,10000000):
            tmp = tmp+rati(1,1000000)
        return tmp.a/tmp.b
    def __add__(self, in2):
        if self.a == 0:
            return rati(in2.a, in2.b)
        elif in2.a == 0:
            return rati(self.a, self.b)
        else:
            #print(self, in2)
            gcd:int = math.gcd(self.b, in2.b) 
            a:int = (self.a*in2.b+in2.a*self.b)//gcd
            b:int = in2.b*self.b//gcd
            #print(a,b)
            return rati(a,b)
    def __sub__(self, in2):
        return self.__add__(rati(-in2.a,in2.b))
    def __iadd__(self, in2):
        if self.a == 0:
            self.a = in2.a
            self.b = in2.b
            return self
        elif in2.a == 0:
            return self
        else:
            gcd = math.gcd(self.b, in2.b) 
            a:int = (self.a*in2.b+in2.a*self.b)//gcd
            b:int = in2.b*self.b//gcd
            self.a = a
            self.b = b
            return self
            
    def __mul__(self, in2):
        if self.a == 0 or in2.a == 0:
            return rati(0,1)
        if self.a == self.b:
            return rati(in2.a, in2.b)
        if in2.a == in2.b:
            return rati(self.a, self.b)
        a = self.a*in2.a
        b = self.b*in2.b
        gcd = math.gcd(a,b)
        return rati(a//gcd, b//gcd)
    def __imul__(self, in2):
        if self.a == 0 or in2.a == 0:
            self.a= 0
            self.b= 1
            return self
        if self.a == self.b:
            self.a = in2.a
            self.b = in2.b
            return self
        if in2.a == in2.b:
            return self
        a = self.a*in2.a
        b = self.b*in2.b
        gcd = math.gcd(a,b)
        self.a = a//gcd
        self.b = b//gcd
        return self
    def __gt__(self, in2):
        return self.a*in2.b > self.b*in2.a
    def __lt__(self, in2):
        return self.a*in2.b < self.b*in2.a
    def abs(self):
        if self.a >= 0:
            return rati(self.a, self.b)
        else:
            return rati(-self.a, self.b)
    def yuksu(self):
        return rati(self.b,self.a)
    
        

mi = rati((c-b),a)
ma = rati((c+b),a)
pi = rati(314159265358979323846264338327950288419716939937510, 10**50)
mpi = rati(-314159265358979323846264338327950288419716939937510, 10**50)

pi2 = rati(2*314159265358979323846264338327950288419716939937510, 10**50)



def rec(a:rati,i:int) -> rati:
    ans = rati(1,1)
    #print(ans, type(ans), a,i)
    for j in range(1,i+1):
        ans *= a*rati(1,j)
    #print(ans, type(ans), a,i)
    return ans

def isplus(i:int) -> rati:
    if i%2 == 0:
        return rati(1,1)
    else:
        return rati(-1,1)

b = rati(b,1)
c = rati(c,1)
def fn(mid:rati):
    ans:rati = rati(a,1)*mid
    ocha:rati = b
    mid= mid-(pi2*rati(round((mid *pi2.yuksu()).tofloat()),1))
    i=0
    #print(ans.tofloat(), ocha.tofloat(),'hi')
    while ocha > rati(1,10**25):
        tmp:rati = (b*isplus(i))
        tmp *= rec(mid,2*i+1)
        #print(ans.tofloat(), mid.tofloat(),tmp.tofloat())
        ans = ans+ tmp
        #print(ans)
        i+=1
        ocha:rati = tmp.abs()
        #print('ocha:',ocha)

    #print(ocha)
    return (ans<c,ocha)

ocha = rati(1,1)
while( (ma-mi) > rati(1,10**25)):
    mid = (mi+ma)*rati(1,2)
    r = fn(mid)
    if r[0]:
        mi = mid
    else:
        ma = mid
    ocha = r[1]
    #print(ocha)
    itr+=1

#print(mi,ma)
#print(mi.tofloat())
print(format(mi.tofloat(),'.6f'))