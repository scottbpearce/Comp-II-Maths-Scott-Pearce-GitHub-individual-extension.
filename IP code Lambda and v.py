from math import log
#for finding lambda

def Rgrad2(p):
    return 8*p - 12*p**2 + 4*p**3

print( Rgrad2(0.381966) )



def Rgrad3(p):
    return 32*p - 144*p**2 + 272*p**3 - 280*p**4 + 168*p**5 - 56*p**6 + 8*p**7


print( Rgrad3(0.079432) )

#for finding v
print( log(2) / log(Rgrad2(0.381966)) )

print( log(2) / log(Rgrad3(0.079432)) )