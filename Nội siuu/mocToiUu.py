import math

def MocToiUu(x,a,b):
    if a < b: 
        n = len(x)
        c = (b-a)/2
        d = (a+b)/2
        for i in range (len(x)):
            x[i] = c*math.cos((math.pi/(2*n))+ i*math.pi/n) + d
        return x