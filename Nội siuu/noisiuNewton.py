import numpy as np
import math
import mocToiUu as op

def LayData(x,y):
    with open('data.txt','r+') as f:
        for line in f.readlines():
            xi = float(line.split('\t')[0])
            yi = float(line.split('\t')[1])
            check = True
            for x_check in x:
                if x_check == xi:
                    check = False
                    break
            if check:
                x.append(xi)
                y.append(yi)

def HornerNhan(x):
    global HeSo
    
    HeSo = np.insert(HeSo,len(HeSo),1)
    i = len(HeSo)-2
    
    while i > 0:
        HeSo[i] = HeSo[i-1] - HeSo[i]*x
        i -= 1
    HeSo[0] = -x*HeSo[0]

    return HeSo

def TySaiPhan(xi,yi):
    c = 1
    S = 0 
    for i in range(len(yi)):
        for j in range(len(xi)):
            if i != j:
                c *= (xi[i] - xi[j])
        S += yi[i] / c
        c = 1
    print(f"Tỷ sai phân cấp{len(yi)-1}",S)
    return S

def TinhDaThuc(HeSo, val):
    result = 0 
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i-=1
    
    print(f"f({val}) = ", result)
    return result
            
def Newton():
    global tsp
    global Px
    
    for i in range(2,len(x)+1):
        tsp = np.insert(tsp,len(tsp),TySaiPhan(x[:i],y[:i]))
        
    for i in range(len(x)-1):
            P = tsp[i]*HornerNhan(x[i])
            Px = np.insert(Px,len(Px),0)
            Px = Px + P

HeSo = np.array([1])
HeSo = HeSo.astype(float)
tsp = np.asarray([])


if __name__ == "__main__":
    x = []
    y = []
    LayData(x,y)
    Px = np.array([y[0]])
    
    Newton()
    print("Hệ số đa thức Newton là: \n", Px)
    # value = 1.8
    # S = TinhDaThuc(Px,value)