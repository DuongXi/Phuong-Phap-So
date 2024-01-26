import math as m
def layData(x,y):
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
                y.append(yi*(yi-25))

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

def SimpSon():
    Sum = 0
    for i in range(0,len(x)-1,2):
        Sum += (y[i] + 4*y[i+1] + y[i+2])*h/3
    print(Sum)
    return Sum

def SimpSon2h():
    Sum = 0
    for i in range(0,len(x)-1,4):
        Sum += (y[i] + 4*y[i+2] + y[i+4])*(2*h)/3
    print(Sum)
    return Sum

def HinhThang():
    Sum = 0
    Sum += 1/2*(y[0] + y[len(y)-1])
    
    for i in range(1,len(y)-1):
        Sum += y[i]
        
    Sum *= h
    return Sum

def NewtonKotez(k):
    n = 0
    Sum = 0
    
    for i in range (0,len(y)-k+1,k):
        Sumi = 0
        c = 0
        for j in range(i,i+k+1):
            Sumi += (y[j]*H[k-1][c])
            c+=1
        Sum += Sumi * h
        
    print(Sum)
    return Sum

def SaiSoHinhThang():
    pass

def SaiSoSimpson(Ih):
    I2h = SimpSon()
    print(f"Sai số Simpson là : {32/31*abs(Ih - I2h)}")

def SaiSoNewtonCotez(Ih,n):
    # n = input("Nhập giá trị n: ")
    Ih2 = NewtonKotez(int(n/2))
    print(f"Sai số Newton Cotez với n = {n} là : {Ih - Ih2}")
    

def KiemTraCachDeu(x):
    denta = x[1] - x[0]
    for i in range(2, len(x)):
        if abs(x[i] - x[i - 1] - denta) > 1e-7:
            return 0
    return denta


H   =  [[1/2,      1/2],
        [1/3,      4/3,        1/3],
        [3/8,      9/8,        9/8,        3/8],
        [14/45,    64/45,      8/15,       64/45,      14/45],
        [95/288,   125/96,     125/144,     125/144,     125/96,     95/288],
        [41/140,   54/35,      27/140,     68/35,      27/140,     54/35,      41/140]]

x = []
y = []

layData(x,y)
h = x[1] - x[0]
print(y)
print("Cách đều: ",KiemTraCachDeu(x))

print("1. Hình thang")
print("2. Simpson")
print("3. Newton-Cotez")

n = int(input("Lựa chọn công thức: "))

# if n == 1 :
#     print("Giá trị tích phân: ", HinhThang())
# elif n == 2:
#     SimpSon2h()
# elif n == 3:
#     NewtonKotez(5)
    
SaiSoSimpson(SimpSon2h())