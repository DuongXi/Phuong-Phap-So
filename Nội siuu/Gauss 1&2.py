import numpy as np

def LayData(x,y):
    with open('data.txt','r+') as f:
        for line in f.readlines():
            xi = float(line.split(' ')[0])
            yi = float(line.split(' ')[1])
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
    C = 1
    for i in range(k+1,n+1):
        C *= (i/(n-i+1))
    return round(C)

def SaiPhanTien(y,n):
    dlt = y[n]
    k = 1
    for i in range(1,n+1):
        dlt += ToHop(n,i)*y[n-i]*(-1)**(i)
        k *= i
    # print(dlt)
    return dlt/k

def Gauss1():
    global Pt
    h = x[1] - x[0]
    c = 1
    
    for i in range(n,len(y)):
        if i == n or i == len(y)-1:
            P = SaiPhanTien(y[2*n-i:i+2],c)*HornerNhan(round((x[i]-x[n])/h))
            Pt = np.insert(Pt,len(Pt),0)
            Pt = Pt + P
            c += 1
        else:
            P = SaiPhanTien(y[2*n-i:i+1],c)*HornerNhan(round((x[i]-x[n])/h))
            Pt = np.insert(Pt,len(Pt),0)
            Pt = Pt + P
            c+=1
            P = SaiPhanTien(y[2*n-i:i+2],c)*HornerNhan(-round((x[i]-x[n])/h))
            Pt = np.insert(Pt,len(Pt),0)
            Pt = Pt + P
            c += 1
    print("Hệ số của đa thức sử dụng Gauss 1: \n",Pt)

def Gauss2():
    global Pt
    h = x[1] - x[0]
    c = 1
    
    for i in range(n,len(y)):
        if i == n:
            P = SaiPhanTien(y[2*n-i-1:i+1],c)*HornerNhan(round((x[i]-x[n])/h))
            Pt = np.insert(Pt,len(Pt),0)
            Pt = Pt + P
            c += 1
        else:
            P = SaiPhanTien(y[2*n-i:i+1],c)*HornerNhan(-round((x[i]-x[n])/h))
            Pt = np.insert(Pt,len(Pt),0)
            Pt = Pt + P
            c += 1
            if(i != len(y)-1):
                P = SaiPhanTien(y[2*n-i-1:i+1],c)*HornerNhan(round((x[i]-x[n])/h))
                Pt = np.insert(Pt,len(Pt),0)
                Pt = Pt + P
                c += 1
    print("Hệ số của đa thức sử dụng Gauss 2: \n",Pt)

def TinhGiaTri(HeSo, val):
    result = 0
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i-=1
    
    print(f"f({val}) = ", result)
    return result

x = [1,2,3,4,5,6,7]
y = [3,4,5,6,5.6,7,9]

# layData(x,y)
HeSo = np.array([0])
HeSo = HeSo.astype(float)
Pt = np.array([y[int((len(y)-1)/2)]])
n = int((len(y)-1)/2)

# Gauss1()
Gauss2()
a = TinhGiaTri(Pt,-1.5)
