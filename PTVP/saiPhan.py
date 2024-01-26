import math
import barDuongCheo as bar
import numpy as np
import matplotlib.pyplot as plt
import MSE

def p(x):
    return 1+x**2

def q(x):
    return 4*x**3 - 6*x**2 + 2.25*x
    
def f(x):
    C = 1
    return C*(math.exp(-x**2)*(1.25*x**2 - 2.75*x - 2))

# ĐK biên loại 1
def DKLoai1():
    HeSo[0][0] = 1
    HeSo[size][size] = 1
    HeSo[0][size+1] = alpha
    HeSo[size][size+1] = beta

# ĐK biên loại 2
def DKLoai2():

    HeSo[0][0] = -p(x0+h/2) + (h**2)*q(x0)/2
    HeSo[0][1] = p(x0+h/2)

    HeSo[size][size-1] = -p(xN-h/2)
    HeSo[size][size] = p(xN-h/2) - h**2*q(xN)/2

    HeSo[0][size+1] = -h**2*f(x0)/2 - alpha*h
    HeSo[size][size+1] = h**2*f(xN)/2 - beta*h

def DKLoai3():
    
    HeSo[0][0] = -p(x0+h/2) + (h**2)*q(x0)/2 - h*sig1
    HeSo[0][1] = p(x0+h/2)

    HeSo[size][size-1] = -p(xN-h/2)
    HeSo[size][size] = p(xN-h/2) - h**2*q(xN)/2 - h*sig2

    HeSo[0][size+1] = -h**2*f(x0)/2 - alpha*h
    HeSo[size][size+1] = h**2*f(xN)/2 - beta*h
 
def DKHonHop():
    HeSo[0][0] = 1
    HeSo[0][size+1] = alpha
    
    HeSo[size][size-1] = -p(xN-h/2)
    HeSo[size][size] = p(xN-h/2) - h**2*q(xN)/2 - h*sig2
    HeSo[size][size+1] = h**2*f(xN)/2 - beta*h

alpha = -150
beta = -219.787667
sig1 = 0
sig2 = 0
h = 0.1
x0 = 0
xN = 3
size = int((xN - x0)/h)

HeSo = np.zeros((size+1,size+2))
x_val = np.zeros(size+1)
x_val[0] = x0
x_val[size] = xN
    
for i in range(1,size):
    x0 += h
    x_val[i] = x0
    HeSo[i][i-1] = p(x0-h/2)
    HeSo[i][i] = -(p(x0+h/2) + p(x0-h/2) + h**2*q(x0))
    HeSo[i][i+1] = p(x0+h/2)
    HeSo[i][size+1] = -h**2*f(x0)
# print(HeSo[1])
# print(HeSo[:,size+1])

choice = input("Giải theo điều kiện loại: ")
if choice == '1':
    DKLoai1()
elif choice == '2':
    DKLoai2()
elif choice == '3':
    DKLoai3()
elif choice == '4':
    DKHonHop()
else:
    print("invalid")

kq = bar.TruyDuoi(HeSo)
print("Hệ số: ", kq)
plt.plot(x_val,kq, marker = "o")
plt.show()

# BPTT để tìm dạng hàm xấp xỉ
# MSE.Menu(t_val,x_val)
# print(t_val)
# MSE.Menu(t_val,y_val)