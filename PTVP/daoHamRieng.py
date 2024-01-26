import math as m
import numpy as np
import matplotlib.pyplot as plt
import MSE

def f(x,t):
    return (1+4*(m.pi**2))*m.exp(t)*m.sin(2*m.pi*x)

def phi(x):
    return m.sin(2*m.pi*x)

def p(t):
    return 0
def q(t):
    return 0

def ucx(x,t):
    return m.exp(t)*m.sin(2*m.pi*x)

l = 1
t = 1
M = 20
N = 800
h = l/M
k = t/N
c=1
lamda=(c*c*k)/(h*h)

X = np.linspace(0, 1, M+1)
T = np.linspace(0, t, N+1)
U = np.zeros((M+1,N+1))
print(X)

for j in range(1,N+1):
    U[0,j] = p(T[j])
    U[M,j] = q(T[j])

for i in range(0,M):
    U[i,0]=phi(X[i])
for j in range(1,N):
    for i in range (1,M):
        # print(i)
        U[i,j+1] = lamda*U[i-1,j] + (1-2*lamda)*U[i,j] + lamda*U[i+1,j] + k*f(X[i],T[j])
        

V = np.zeros(M+1)
for i in range (0,M+1):
    V[i]= U[i,N]
print(V)

plt.plot(X,V)
plt.show()

# BPTT để tìm dạng hàm xấp xỉ
# MSE.Menu(t_val,x_val)
# print(t_val)
# MSE.Menu(t_val,y_val)