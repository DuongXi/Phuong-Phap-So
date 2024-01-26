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

    return dlt

def HaiDiem(x0):
    k = x.index(x0)
    der = SaiPhanTien(y[k:k+2],1)/h
    return der

def BaDiem(x0):
    k = x.index(x0)
    if k == 0:
        der = (-3/2*y[k] + 2*y[k+1] - 1/2*y[k+2])/h
    elif k == len(x)-1:
        der = (3/2*y[k] - 2*y[k-1] + 1/2*y[k-2])/h
    else:
        der = (-1/2*y[k-1] + 1/2*y[k+1])/h
        
    return der

def BonDiem(x0):
    k = x.index(x0)
    if k == 0:
        der = (-11/6*y[k] + 3*y[k+1] - 3/2*y[k+2] + 1/3*y[k+3])
    elif k == 1 or k == len(x)-3:
        der = (-1/3*y[k-1] - 1/2*y[k] + y[k+1] - 1/6*y[k+2])
    elif k == 2 or k == len(x)-2:
        der = (1/6*y[k-2] - y[k-1] + 1/2*y[k] + 1/3*y[k+1])
    elif k == len(x)-1:
        der = (-1/3*y[k-3] + 3/2*y[k-2] - 3*y[k-1] + 11/6*y[k])
    else:
        der = (-1/3*y[k-1] - 1/2*y[k] + y[k+1] - 1/6*y[k+2])
    
    return der

def NamDiem(x0):
    k = x.index(x0)
    if k == 0:
        der = (-25/12*y[k] + 4*y[k+1] - 3*y[k+2] + 4/3*y[k+3] - 1/4*y[k+4])
        
    elif k == 1 or k == len(x)-4:
        der = (-1/4*y[k-1] + - 5/6*y[k] + 3/2*y[k+1] - 1/2*y[k+2] + 1/12*y[k+3])
        
    elif k == 3 or k == len(x)-2:
        der = (-1/12*y[k-3] + 1/2*y[k-2] - 3/2*y[k-1] + 5/6*y[k] + 1/4*y[k+1])
        
    elif k == 4 or k == len(x)-1:
        der = (1/4*y[k-4] - 4/3*y[k-3] + 3*y[k-2] - 4*y[k-1] + 25/12*y[k])
        
    else:
        der = (1/12*y[k-2] - 4/3*y[k-1] + 2/3*y[k+1] - 1/12*y[k+2])
    
    return der

def DaoHamBacMot(x0,k):
    if k == 2:
        return HaiDiem(x0)
    elif k == 3:
        return BaDiem(x0)
    elif k == 4:
        return BonDiem(x0)
    elif k == 5:
        return NamDiem(x0)
    
def DaoHamBacHai(x0):
    k = x.index(x0)
    der2 = (1/h**2)*(y[k+2]-2*y[k+1]-y[k])
    
    return der2

def SaiSo(f,n):
    k = n
    for i in range(1,n):
        k *= i
    eps = abs(f)*(h**(n-1))/(k)

x = []
y = []
LayData(x,y)

if __name__ == "__main__":
    h = x[1] - x[0]
    c = 0
    pts = int(input("Nhập số diểm của công thức: "))
    for i in x:
        print(f"f'(x_{c}) = ", DaoHamBacMot(i,pts))
        c+=1