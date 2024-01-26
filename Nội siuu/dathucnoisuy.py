from Gauss import *
import numpy as np

def layData(x,y):
    with open('value.txt','r+') as f:
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

def TinhGiaTri(HeSo, val):
    result = 0 
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i-=1
    
    print(f"f({val}) = ", result)
    return result

x = []
y = []
layData(x,y)
x = np.array(x)
size = len(x)
matrix = np.zeros((size,size+1))

for i in range(size+1):
    if i == 0:
        matrix[:,i] = 1  
    elif i == size:
        matrix[:,i] = y
    else:
        matrix[:,i] = x**i

gaussThuan(matrix)
HeSo = gaussNghich(matrix)
S = TinhGiaTri(HeSo,1)
print("Hệ số của đa thức nội suy là: \n", HeSo)