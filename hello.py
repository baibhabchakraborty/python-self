def gcd(m,n):
    fm=[]
    fn=[]
    for i in range(1,m):
        if m%i == 0:
            fm.append(i)
    for i in range(1,n):
        if n%i == 0:
            fn.append(i)
    cf=[]
    for f in fm:
            if f in fn:
                    cf.append(f)
    print(cf[-1])
gcd(12,8)



def gcd(m,n):
    ans=1
    if m>=n:
        (m,n)=(n,m)
    for i in range(1,m):
        if m%i==0 and n%i==0:
            ans=i
    print(ans)

gcd(12,8)


def gcd(m,n):
    if m>=n:
        (m,n)=(n,m)
    i=m
    while(i>1):
        if m%i==0 and n%i==0:
            return(i)
        i=i-1
print(gcd(12,8))

import math
print(math.gcd(12,8))
