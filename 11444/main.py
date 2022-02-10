import math
n = int(input())

class rati(object):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a/self.b)
    def tofloat(self):
        return self.a/self.b

def addrati(in1, in2):
    if in1.a == 0:
        return in2
    if in2.a == 0:
        return in1
    gcd = math.gcd(in1.b, in2.b)
    return rati((in1.a*in2.b+in2.a*in1.b)//gcd, in2.b*in1.b//gcd)

def multrati(in1, in2):
    if in1.a == 0 or in2.a == 0:
        return rati(0,1)
    
    if in1.a == in1.b:
        return in2
    if in2.a == in2.b:
        return in1
    a = in1.a*in2.a
    b = in1.b*in2.b
    gcd = math.gcd(a,b)
    return rati(a//gcd,b//gcd)
class oneroot(object):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a)+'+sqrt(5)*'+str(self.b)
def rnmult(in1, in2):
    return oneroot(addrati(multrati(in1.a, in2.a), multrati(rati(5,1),multrati(in1.b, in2.b))),addrati(multrati(in1.a,in2.b),multrati(in2.a,in1.b)))

def rnadd(in1,in2):
    return oneroot(addrati(in1.a, in2.a), addrati(in1.b,in2.b))

def rnpower(in1, exponent):
    if exponent == 0:
        return oneroot(rati(1,1),rati(0,1))
    if exponent == 1:
        return in1
    if exponent%2==0:
        return rnmult(rnpower(in1, exponent//2), rnpower(in1,exponent//2))
    else:
        return rnmult(rnmult(rnpower(in1, exponent//2), rnpower(in1,exponent//2)), in1)


l1 = oneroot(rati(1,2), rati(1,2))
l2 = oneroot(rati(1,2), rati(-1,2))
print(multrati(rnpower(l1,n).b, rati(2,1)).a%1000000007)