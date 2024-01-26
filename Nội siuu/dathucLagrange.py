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

def HornerNhan(x,Heso):
    # P_n(x)*(x-c) = (a_n*x^n + a_n-1*x^(n-1) + ... + a_1*x + a_0)*(x-c) 
    #              = b_n+1*x^(n+1) + b_n*x^n + ... + b_1*x + b_0)
    # b_n+1 = a_n
    # b_k = a_k-1 - a_k*c
    # b_0 = -c*a_0
    
    Heso.append(1)
    i = len(Heso)-2
    
    while i > 0:
        Heso[i] = Heso[i-1] - Heso[i]*x
        i -= 1
        
    Heso[0] = -x*Heso[0]

def HornerChia(x,Heso):
    # P_n(x)/(x-c) = (a_n*x^n + a_n-1*x^(n-1) + ... + a_1*x + a_0)/(x-c) 
    #              = b_n+1*x^(n+1) + b_n*x^n + ... + b_1*x + b_0)
    # b_n-1 = b_n-2*c + a_n-1 
    # b_k = b_k-1*c + a_k
    # b_0 = a_0
    
    heso = Heso.copy()
    i = len(heso) - 2
    
    while i >= 0:
        heso[i] = heso[i+1]*x + heso[i]
        i-=1
    
    return heso[1:len(heso)]

def TinhGiaTri(HeSo, val):
    result = 0 
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i-=1
    
    print(f"f({val}) = ", result)
    return result

def Lagrange(x,y):
    HeSo = [1]
    P = []
    c = []
    w = []
    for i in range(0,len(x)):
        HornerNhan(x[i], HeSo)

    for i in range(len(x)):
        c.append(1)
        for j in range(len(x)):
            if i != j:
                c[i] *= 1 / (x[i]-x[j])

    for i in range(len(x)):
        w.append(HornerChia(x[i],HeSo))
        
    for i in range(len(x)):
        P.append(0)
        for j in range(len(x)):
            P[i] +=  y[j]*c[j]*w[j][i]

    # print(P)
    return P
            
if __name__ == "__main__":
    x = []
    y = []
    LayData(x,y)
    
    print(y)
    P = Lagrange(x,y)
    # value = 1
    # S = tinhDaThuc(P,value)
    
    print("Hệ số của đa thức Lagrange là: \n",P)