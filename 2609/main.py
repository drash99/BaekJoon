inputraw = input().strip().split()
a = int(inputraw[0])
b = int(inputraw[1])

def gcd(a,b):
    if(a%b==0):
        return b
    elif(b%a==0):
        return a

    if(a>b):
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))