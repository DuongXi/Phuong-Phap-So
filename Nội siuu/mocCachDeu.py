import numpy as np

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

def ToHop(n,k):
    if n >= k:
        C = 1
        for i in range(k+1,n+1):
            C *= (i/(n-i+1))
        return round(C)
    else:
        return -1;

def SaiPhanTien(y,n):
    dlt = y[n]
    k = 1
    
    for i in range(1,n+1):
        dlt += ToHop(n,i)*y[n-i]*(-1)**(i)
        k *= i
    
    return dlt/k
 
def SaiPhanLui(y,n):
    dlt = y[len(y)-1]
    k = 1
    
    for i in range(1,n+1):
        dlt += ToHop(n,i)*y[len(y)-1-i]*(-1)**(i)
        k *= i

    return dlt/k
 

def NewtonTien():
    global Pt
    h = x[1] - x[0]
    for i in range(0,n-1):
        P = SaiPhanTien(y[:i+2],i+1)*HornerNhan(round((x[i]-x[0])/h))
        Pt = np.insert(Pt,len(Pt),0)
        Pt = Pt + P

def NewtonLui():
    global Pt
    h = x[1] - x[0]
    
    for i in range(0,n-1):
        P = SaiPhanLui(y[n-i-1:],i+1)*HornerNhan(round((x[i]-x[0])/h))
        Pt = np.insert(Pt,len(Pt),0)
        Pt = Pt + P

def TinhGiaTri(HeSo, val):
    result = 0
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i-=1
    
    print(f"f({val}) = ", result)
    return result
if __name__ == "__main__":
    x = []
    y = []

    LayData(x,y)

    n = len(x)
    HeSo = np.array([0])
    Pt = np.array([y[0]])
    HeSo = HeSo.astype(float)

    NewtonTien()
    print("Hệ só đa thức Newton cách đều là: \n",Pt)
    # a = TinhGiaTri(Pt,1.5)
    # NewtonLui()
