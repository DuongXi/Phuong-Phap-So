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

def HornerNhanLe(x):
    global HeSoLe
    
    HeSoLe = np.insert(HeSoLe,len(HeSoLe),0)
    HeSoLe = np.insert(HeSoLe,len(HeSoLe),1)
    i = len(HeSoLe)-3
    
    while i > 0:
        HeSoLe[i] = HeSoLe[i-2] - HeSoLe[i]*x
        i -= 2
    HeSoLe[1] -= 1
    # print(HeSoLe)
    return HeSoLe

def HornerNhanChan(x):
    global HeSoChan
    
    HeSoChan = np.insert(HeSoChan,len(HeSoChan),0)
    HeSoChan = np.insert(HeSoChan,len(HeSoChan),1)
    i = len(HeSoChan)-2
    
    while i > 0:
        HeSoChan[i] = HeSoChan[i-2] - HeSoChan[i]*x
        i -= 1
    HeSoChan[1] -= 1
    # print(HeSoChan)
    return HeSoChan

def ToHop(n,k):
    C = 1
    for i in range(k+1,n+1):
        C *= (i/(n-i+1))
    return round(C)

def GiaiThua(n):
    k = 1
    for i in range(1,n+1):
        k *= i
    return k

def SaiPhan(yk,n,y):
    b = n+yk
    dlt = y[b]
    
    for i in range(1,n+1):
        dlt += ToHop(n,i)*y[b-i]*(-1)**(i)
    return dlt

def Sterling(n,xk):
    center = round((xk - x[0]) / h)
    step = int((n-1)/2)

    BSPLe = np.zeros((1,step+1))
    BSPLe[0][0] = y[center]
    BSPChan = np.zeros((1,step+1))
    BSPChan[0][0] = 0
    
    P = y[center - step:center+step+1]
    P = np.roll(P, -step, axis = 0)
    
    a = np.zeros((1,2*(step+1)))
    b = np.zeros((1,2*(step+1)+1))
    
    for i in range (1,step + 1):
        BSPLe[0][i] = SaiPhan(-i,2*i,P)/GiaiThua(2*i)
        hsl = HornerNhanLe(i**2)
        a[0][:2*(i+1)] = a[0][:2*(i+1)] + BSPLe[0][i] * hsl
        
        BSPChan[0][i] = (SaiPhan(-i+1,2*i-1,P) + SaiPhan(-i,2*i-1,P))/(2*GiaiThua(2*i-1))
        hsc = HornerNhanChan(i**2)
        b[0][:2*(i+1)+1] = b[0][:2*(i+1)+1] + BSPChan[0][i] * hsc 

    a = a[0]
    b[0][0] = P[0]
    b = b[0]
    a = np.insert(a,len(a),0)
    HeSo = a + b
    
    print("Hệ số lẻ: \n",a)
    print("\nHệ số chẵn: \n",b)
    
    print("\nHệ số đa thức: \n",HeSo)
    val = float(input("Nhập giá trị trong khoảng nội suy cần tìm giá trị: "))
    print(f"Giá trị hàm số tại x = {val}: ", TinhGiaTri(HeSo,(val-x[center])/h))

def Bessel(n,xk):
    center = x.index(xk)
    step = int(n/2)
    
    BSPLe = np.zeros((1,step))
    BSPLe[0][0] = y[center]
    BSPChan = np.zeros((1,step))
    BSPChan[0][0] = 0
    
    P = y[center - step:center+step+1]
    P = np.roll(P, -step, axis = 0)
    
    a = np.zeros((1,2*(step+1)))
    b = np.zeros((1,2*(step+1)+1))
    
    for i in range (1,step + 1):
        BSPLe[0][i] = SaiPhan(-i,2*i,P)/GiaiThua(2*i)
        hsl = HornerNhanLe(i**2)
        a[0][:2*(i+1)] = a[0][:2*(i+1)] + BSPLe[0][i] * hsl
        
        BSPChan[0][i] = (SaiPhan(-i+1,2*i-1,P) + SaiPhan(-i,2*i-1,P))/(2*GiaiThua(2*i-1))
        hsc = HornerNhanChan(i**2)
        b[0][:2*(i+1)+1] = b[0][:2*(i+1)+1] + BSPChan[0][i] * hsc

    a = a[0]
    b[0][0] = P[0]
    b = b[0]
    a = np.insert(a,len(a),0)
    HeSo = a + b
    
    print("Hệ số chẵn: \n",a)
    print("\nHệ số lẻ: \n",b)
    
    print("\nHệ số đa thức: \n",HeSo)
    val = float(input("Nhập giá trị trong khoảng nội suy cần tìm giá trị: "))
    print(f"Giá trị hàm số tại x = {val}: ", TinhGiaTri(HeSo,(val-x[0])/h))
    pass

def TinhGiaTri(HeSo, val):
    result = 0
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i -= 1
        
    return result

x = []
y = []

LayData(x,y)
h = x[1]-x[0]

HeSoLe = np.array([0,1])
HeSoChan = np.array([0,0,1])
HeSoLe = HeSoLe.astype(float)
HeSoChan = HeSoChan.astype(float)

Pt = []

pts = 9 #int(input("Nhập số mốc nội suy cần dùng: "))

value = 3.032 #float(input("Nhập giá trị cần tính: "))

if pts % 2 == 0:
    Bessel(pts,value)
else:
    Sterling(pts,value)

#TinhGiaTri(Pt,-1.5)
#  [ 2.21651000e+00  8.45240476e-02  5.27339952e-01 -8.50590446e-02
#  -5.32027365e-01  5.36651042e-04  4.69931250e-03 -1.66220238e-06
#  -1.19107143e-05  8.18452381e-09  1.09126984e-08]