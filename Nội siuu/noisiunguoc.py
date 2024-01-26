import dathucLagrange as Lg
import mocCachDeu as Cd
import numpy as np
import math

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

def ToHop(n,k):
    if n >= k:
        C = 1
        for i in range(k+1,n+1):
            C *= (i/(n-i+1))
        return round(C)
    else:
        return -1;

def KhoangCachLy(y,Y):
    c = -1
    for i in range(len(y)):
        if i == len(y) - 1:
            break
        if ((y[i]-Y)*(y[i+1]-Y) < 0):
            kcl.append([])
            c += 1
            kcl[c].append(i)
            kcl[c].append(i+1)

def KhoangDonDieu(y):
    c = 0
    for i in range(1,len(y)):
        if i < len(y)-1:
            if y[i-1] < y[i] and y[i] > y[i+1]:
                kdd[c].append(i)
                kdd.append([])
                c += 1
            elif y[i-1] > y[i] and y[i] < y[i+1]:
                kdd[c].append(i)
                kdd.append([])
                c += 1
        kdd[c].append(i)

def HamNguoc(Kcl):
    for i in kdd:
        if Kcl[0] in i:
            check1 = Kcl[0] - i[0]
            check2 = i[len(i)-1] - Kcl[1]
            if check1 < check2:
                
                print("Các mốc nối suy sử dụng")
                print(x[i[0]:Kcl[1]+check1+1])
                P = Lg.Lagrange(y[i[0]:Kcl[1]+check1+1], x[i[0]:Kcl[1]+check1+1])
                print("Hệ số đa thức với biến y:\n",P)
                print("Nghiệm thuộc khoảng trên là: ",Lg.TinhGiaTri(P,Y))
                print()
                
            else:
                
                print("Các mốc nối suy sử dụng")
                print(x[Kcl[0]-check2:i[len(i)-1]+1])
                P = Lg.Lagrange(y[Kcl[0]-check2:i[len(i)-1]+1], x[Kcl[0]-check2:i[len(i)-1]+1])
                print("Hệ số đa thức với biến y:\n",P)
                print("Nghiệm thuộc khoảng trên là: ",Lg.TinhGiaTri(P,Y))
                print()

def TinhPhi():
    pass
               
def Lap(eps,Kcl):
    n = len(x)
    count = 0
    
    if Kcl[0] < n/2:
        print("Với khoảng cách ly sau sử dụng Newton tiến.")
        print(Kcl)
        t0 = (Y - y[Kcl[0]])/Cd.SaiPhanTien(y[Kcl[0]:],1)
        print(f"Lặp lần {count}: ", t0)
        
        print()
        
    else:
        print("Với khoảng cách ly sau sử dụng Newton lùi.")
        print(Kcl)
        deltayn = Cd.SaiPhanLui(y[:Kcl[1]+1],1)
        t0 = (Y - y[Kcl[1]])/deltayn
        t1 = 1e7
        p = t0
        print(f"Lặp lần {count}: ", t0)
        
        while abs(t1 - t0)*h > eps:
            count += 1
            t1 = t0
            P = t0
            init = 0
            
            for i in range (1,2):
                P *= (t0 + i)
                init += Cd.SaiPhanLui(y[:Kcl[1]+1],i+1)*P
                
            t0 = p - (1 / deltayn)*init
            print(f"Lần lặp {count}: ", t0)
            
        res = x[Kcl[1]] + t0*h
        print(res)

x = []
y = []
LayData(x,y)
x = np.asarray(x) 

Y = 3.26

kcl = []
kdd = [[0]]
P = []

h = x[1] - x[0]
spaced = True
eps = 0.01

KhoangCachLy(y,Y)
KhoangDonDieu(y)
    
print("Các khoảng cách ly nghiệm (index): \n",kcl)
print("Các khoảng đơn điệu trong dữ liệu (index): \n", kdd)
print()


for i in range (2,len(x)):
    temp = x[i]-x[i-1]
    if abs(temp - h) > 1e-7:
        spaced = False

if(spaced):
    for i in kcl:
        print("Ta sử dụng phương pháp lặp cho bộ dữ liệu đã cho.")
        Lap(eps,i)
else:
    for i in kcl:
        print("Ta sử dụng phương pháp hàm ngược cho bộ dữ liệu đã cho.")
        HamNguoc(i)