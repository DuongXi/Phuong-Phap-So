import matplotlib.pyplot as plt
import numpy as np
import barDuongCheo as bar

def TinhGiaTri(HeSo, val):
    result = 0
    i = len(HeSo)-1
    
    while i >= 0:
        result = HeSo[i] + val*result
        i -= 1
        
    return result

def SplineBac1():
    n = len(x)
    for i in range(n-1):
        ai = (y[i+1] - y[i]) / (x[i+1] - x[i])
        bi = ((y[i+1]*x[i+1] - y[i]*x[i]) / (x[i+1] - x[i]))
        S.append(ai*x[i]+bi)
    print(S)

def SplineBac2(x,y):
    n = len(x)
    h = np.diff(x)
    HeSo = np.zeros((n,n+1))
    HeSo[0,0] = 1
    HeSo[0,n] = 2
    # HeSo[n-1,n-1] = 3
    # HeSo[n-1,n] = 4
    for i in range(0,n-1):
        HeSo[i+1,i] = 1
        HeSo[i+1,i+1] = 1
        HeSo[i+1,n] = 2*(y[i+1] - y[i])/h[i]
    print(HeSo)
    alpha = bar.TruyDuoi(HeSo)
    S = []
    # s[i] = [a,b,c,d] = ax^3 + bx^2 + cx + d
    for i in range(n-1):
        S.append([])
        S[i].append((alpha[i+1] - alpha[i])/2*h[i])
        S[i].append((-alpha[i+1]*x[i] + alpha[i]*x[i+1])/h[i])
        S[i].append((alpha[i+1]*(x[i]**2) - alpha[i]*(x[i+1]**2))/2*h[i] + y[i] - alpha[i]*h[i]/2)
    print(S)
    
def SplineBac3(x,y):
    n = len(x)
    h = np.diff(x)
    HeSo = np.zeros((n,n+1))
    HeSo[0,0] = 1
    HeSo[0,n] = 2
    HeSo[n-1,n-1] = 3
    HeSo[n-1,n] = 4
    for i in range(0,n-2):
        HeSo[i+1,i] = h[i]/6
        HeSo[i+1,i+1] = (h[i]+h[i+1])/3
        HeSo[i+1,i+2] = h[i+1]/6
        HeSo[i+1,n] = (y[i+2] - y[i+1])/h[i+1] - (y[i+1] - y[i])/h[i]
    print(HeSo)
    alpha = bar.TruyDuoi(HeSo)
    S = []
    # s[i] = [a,b,c,d] = ax^3 + bx^2 + cx + d
    for i in range(n-1):
        S.append([])
        S[i].append((alpha[i+1] - alpha[i])/6*h[i])
        S[i].append((-3*alpha[i+1]*x[i] + 3*alpha[i]*x[i+1])/6*h[i])
        S[i].append((3*alpha[i+1]*(x[i]**2) - 3*alpha[i]*(x[i+1]**2))/6*h[i] + (y[i+1] - y[i])/h[i] - (alpha[i+1] - alpha[i])*h[i]/6)
        S[i].append((-alpha[i+1]*(x[i]**3) + alpha[i]*(x[i+1]**3))/6*h[i] - (y[i+1]*x[i] - y[i]*x[i+1])/h[i] + (alpha[i+1]*x[i] - alpha[i]*x[i+1])*h[i]/6)
    print("Hệ số các hàm ghép trơn",S)
    return S
'''
def SplineBac4():
    n = len(x)
    h = np.diff(x)
    HeSo = np.zeros((n,n+1))
    HeSo[0,0] = 1
    HeSo[0,n] = 2
    HeSo[n-1,n-1] = 3
    HeSo[n-1,n] = 4
    for i in range(0,n-2):
        HeSo[i+1,i] = h[i]/6
        HeSo[i+1,i+1] = (h[i]+h[i+1])/3
        HeSo[i+1,i+2] = h[i+1]/6
        HeSo[i+1,n] = (y[i+2] - y[i+1])/h[i+1] - (y[i+1] - y[i])/h[i]
    print(HeSo)
    alpha = bar.TruyDuoi(HeSo)
    S = []
    # s[i] = [a,b,c,d] = ax^3 + bx^2 + cx + d
    for i in range(n):
        S.append([])
        S[i].append((alpha[i+1] - alpha[i])/6*h[i])
        S[i].append((-3*alpha[i+1]*x[i] + 3*alpha[i]*x[i+1])/6*h[i])
        S[i].append((3*alpha[i+1]*(x[i]**2) - 3*alpha[i]*(x[i+1]**2))/6*h[i] + (y[i+1] - y[i])/h[i] - (alpha[i+1] - alpha[i])*h[i]/6)
        S[i].append((-alpha[i+1]*(x[i]**3) + alpha[i]*(x[i+1]**3))/6*h[i] - (y[i+1]*x[i] - y[i]*x[i+1])/h[i] + (alpha[i+1]*x[i] - alpha[i]*x[i+1])*h[i]/6)
'''

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

x = []
y = []
x0 = 1.2
LayData(x,y)
# SplineBac2(x,y)
S = SplineBac3(x,y)

for i in range(len(x)-1):
    if x[i] <= x0 and x0 <= x[i+1]:
        value = TinhGiaTri(S[i],x0)

print(value)

# x0=np.linspace(x[0], x[len(x)-1], 1000)
# plt.plot(x,S,marker = 'o')
# plt.show()